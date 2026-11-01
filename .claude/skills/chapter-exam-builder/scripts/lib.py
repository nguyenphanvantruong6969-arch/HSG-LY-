"""Shared layout library: Vietnamese exam-style DOCX with native Word equations (OMML)."""
import copy, re, subprocess, tempfile, zipfile, os, hashlib
from lxml import etree
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
FONT = 'Times New Roman'

# ------------------------------------------------------------------ math
class MathCache:
    def __init__(self):
        self.cache = {}

    @staticmethod
    def norm(latex):
        latex = latex.strip()
        latex = re.sub(r'(?<=\d),(?=\d)', '{,}', latex)
        latex = re.sub(r'_\{([A-Za-zđ]{2,})\}', r'_{\\mathrm{\1}}', latex)
        return latex

    def load(self, items):
        """items: iterable of (display, latex). Convert all missing ones in one pandoc call."""
        todo = []
        for disp, lt in items:
            key = (disp, self.norm(lt))
            if key not in self.cache and key not in todo:
                todo.append(key)
        if not todo:
            return
        md = []
        for disp, lt in todo:
            md.append(('$$' + lt + '$$') if disp else ('$' + lt + '$'))
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, 'm.md'); out = os.path.join(d, 'm.docx')
            open(src, 'w', encoding='utf-8').write('\n\n'.join(md) + '\n')
            subprocess.run(['pandoc', '-f', 'markdown+tex_math_dollars', '-t', 'docx', src, '-o', out], check=True)
            xml = zipfile.ZipFile(out).read('word/document.xml')
        root = etree.fromstring(xml)
        body = root.find('{%s}body' % W_NS)
        paras = body.findall('{%s}p' % W_NS)
        assert len(paras) == len(todo), (len(paras), len(todo))
        for key, p in zip(todo, paras):
            disp, lt = key
            el = p.find('{%s}oMathPara' % M_NS) if disp else p.find('{%s}oMath' % M_NS)
            if el is None:
                el = p.find('.//{%s}oMath' % M_NS)
            assert el is not None, key
            self.cache[key] = el

    def get(self, display, latex):
        return copy.deepcopy(self.cache[(display, self.norm(latex))])

MATH = MathCache()
TOKEN = re.compile(r'(\$\$.+?\$\$|\$.+?\$|\*\*.+?\*\*|__.+?__)', re.S)

LEAD_OPS = [('\\Leftrightarrow', '⇔'), ('\\Rightarrow', '⇒'), ('\\approx', '≈'), ('\\geq', '≥'), ('\\leq', '≤'),
            ('\\ge', '≥'), ('\\le', '≤'), ('=', '=')]

def split_lead(lt):
    s = lt.strip()
    for op, ch in LEAD_OPS:
        if s.startswith(op) and (not op.startswith('\\') or not s[len(op):len(op) + 1].isalpha()):
            return ch, s[len(op):].strip()
    return None, lt

def scan_math(obj, out):
    """collect every math snippet from nested str/list/dict content"""
    if isinstance(obj, str):
        for tok in TOKEN.findall(obj):
            if tok.startswith('$$'):
                out.append((True, tok[2:-2]))
            elif tok.startswith('$'):
                out.append((False, split_lead(tok[1:-1])[1]))
            elif tok.startswith('**') or tok.startswith('__'):
                scan_math(tok[2:-2], out)
    elif isinstance(obj, dict):
        for v in obj.values(): scan_math(v, out)
    elif isinstance(obj, tuple) and len(obj) == 2 and obj[0] == 'eq':
        out.append((True, obj[1]))
    elif isinstance(obj, (list, tuple)):
        for v in obj: scan_math(v, out)
    return out

# ------------------------------------------------------------------ run helpers
def _set_fonts(run, size=None, bold=None, italic=None):
    rpr = run._r.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), FONT)
    if size: run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic

def rich(p, text, size=None, bold=False, italic=False):
    """Append text with **bold**, __italic__ and $math$ / $$display$$ to paragraph p."""
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            r = p.add_run(text[pos:m.start()]); _set_fonts(r, size, bold or None, italic or None)
        tok = m.group(0)
        if tok.startswith('$$'):
            p._p.append(MATH.get(True, tok[2:-2]))
        elif tok.startswith('$'):
            ch, rest = split_lead(tok[1:-1])
            if ch:
                r = p.add_run(ch + ' '); _set_fonts(r, size, bold or None, italic or None)
            p._p.append(MATH.get(False, rest))
        elif tok.startswith('**'):
            rich(p, tok[2:-2], size, True, italic)
        else:
            rich(p, tok[2:-2], size, bold, True)
        pos = m.end()
    if pos < len(text):
        r = p.add_run(text[pos:]); _set_fonts(r, size, bold or None, italic or None)
    return p

def add_field(p, instr, cached='1', size=None, bold=None):
    def mk(kind):
        r = p.add_run(); _set_fonts(r, size, bold)
        fc = OxmlElement('w:fldChar'); fc.set(qn('w:fldCharType'), kind); r._r.append(fc)
        return r
    mk('begin')
    r = p.add_run(); _set_fonts(r, size, bold)
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = ' %s ' % instr; r._r.append(it)
    mk('separate')
    r = p.add_run(cached); _set_fonts(r, size, bold)
    mk('end')

# ------------------------------------------------------------------ document
class Doc:
    def __init__(self, margins=(1.7, 1.7, 1.8, 1.8)):
        self.d = Document()
        st = self.d.styles['Normal']
        st.font.name = FONT; st.font.size = Pt(12)
        rpr = st.element.get_or_add_rPr()
        rf = rpr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
        for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
            rf.set(qn(a), FONT)
        pf = st.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(3); pf.line_spacing = 1.08
        sec = self.d.sections[0]
        sec.page_width = Cm(21); sec.page_height = Cm(29.7)
        sec.top_margin = Cm(margins[0]); sec.bottom_margin = Cm(margins[1])
        sec.left_margin = Cm(margins[2]); sec.right_margin = Cm(margins[3])
        sec.footer_distance = Cm(0.8)
        self.text_w = 21 - margins[2] - margins[3]
        self.col_gap = 0.9

    # ---- footer
    def footer(self, label):
        sec = self.d.sections[0]
        p = sec.footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in list(p.runs): r._r.getparent().remove(r._r)
        rich(p, 'Trang ', 10)
        add_field(p, 'PAGE', '1', 10)
        rich(p, '/', 10)
        add_field(p, 'NUMPAGES', '5', 10)
        rich(p, ' - ' + label, 10)

    # ---- paragraphs
    def p(self, text='', size=None, bold=False, italic=False, align=None, left=None, first=None,
          after=None, before=None, keep_next=False, keep_lines=True, spacing=None):
        para = self.d.add_paragraph()
        rich(para, text, size, bold, italic)
        pf = para.paragraph_format
        if align == 'c': para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif align == 'r': para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif align == 'j': para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if left is not None: pf.left_indent = Cm(left)
        if first is not None: pf.first_line_indent = Cm(first)
        if after is not None: pf.space_after = Pt(after)
        if before is not None: pf.space_before = Pt(before)
        if spacing is not None: pf.line_spacing = spacing
        pf.keep_with_next = keep_next
        pf.keep_together = keep_lines
        return para

    def display(self, latex, after=3):
        para = self.d.add_paragraph()
        para._p.append(MATH.get(True, latex))
        para.paragraph_format.space_after = Pt(after)
        return para

    def page_break(self):
        self.d.add_page_break()

    # ---- sections / columns
    def section(self, cols=1, gap=None):
        s = self.d.add_section(WD_SECTION.CONTINUOUS)
        sp = s._sectPr
        c = sp.find(qn('w:cols'))
        if c is None:
            c = OxmlElement('w:cols'); sp.append(c)
        c.set(qn('w:num'), str(cols))
        c.set(qn('w:space'), str(int((gap or self.col_gap) * 567)))
        if cols > 1:
            c.set(qn('w:equalWidth'), '1')
        return s

    @property
    def col_w(self):
        return (self.text_w - self.col_gap) / 2

    # ---- figure
    def figure(self, path, width_cm, caption=None, after=4, align='c'):
        para = self.d.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER if align == 'c' else WD_ALIGN_PARAGRAPH.LEFT
        para.paragraph_format.space_after = Pt(1 if caption else after)
        para.paragraph_format.keep_with_next = bool(caption)
        para.add_run().add_picture(path, width=Cm(width_cm))
        if caption:
            c = self.p(caption, size=11, italic=False, align='c', after=after)
        return para

    # ---- tables
    def table(self, rows, widths, header=False, size=11, align=None, borders=True, bold_first_col=False, shade_header=False):
        t = self.d.add_table(rows=len(rows), cols=len(widths))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        for j, wd in enumerate(widths):
            t.columns[j].width = Cm(wd)
        if borders:
            tblPr = t._tbl.tblPr
            b = OxmlElement('w:tblBorders')
            for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
                x = OxmlElement('w:' + e); x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '4'); x.set(qn('w:color'), '000000'); b.append(x)
            tblPr.append(b)
        for i, row in enumerate(rows):
            for j, txt in enumerate(row):
                cell = t.cell(i, j); cell.width = Cm(widths[j])
                para = cell.paragraphs[0]
                para.paragraph_format.space_after = Pt(1); para.paragraph_format.space_before = Pt(1)
                al = (align[j] if align else 'l')
                if al == 'c': para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                elif al == 'r': para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                rich(para, str(txt), size, bold=(header and i == 0) or (bold_first_col and j == 0))
                if header and i == 0 and shade_header:
                    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement('w:shd')
                    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), 'D9D9D9'); tcPr.append(sh)
        # prevent rows splitting
        for r in t.rows:
            trPr = r._tr.get_or_add_trPr(); cs = OxmlElement('w:cantSplit'); trPr.append(cs)
        self.d.add_paragraph().paragraph_format.space_after = Pt(2)
        return t

    # ---- exam header block (layout modelled on a Vietnamese national exam paper)
    def exam_header(self, ma_de, left, right, npages, box=None):
        t = self.d.add_table(rows=2, cols=2)
        t.autofit = False
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        wl, wr = 6.6, self.text_w - 6.6
        for r in t.rows:
            r.cells[0].width = Cm(wl); r.cells[1].width = Cm(wr)
        # top-left
        c = t.cell(0, 0); first = True
        for txt, b, it in left:
            para = c.paragraphs[0] if first else c.add_paragraph(); first = False
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER; para.paragraph_format.space_after = Pt(1)
            if '{N}' in txt:
                a, b2 = txt.split('{N}')
                rich(para, a, 11.5, b, it); add_field(para, 'NUMPAGES', str(npages), 11.5, b); rich(para, b2, 11.5, b, it)
            else:
                rich(para, txt, 11.5, b, it)
        # top-right
        c = t.cell(0, 1); first = True
        for txt, b, it in right:
            para = c.paragraphs[0] if first else c.add_paragraph(); first = False
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER; para.paragraph_format.space_after = Pt(1)
            rich(para, txt, 11.5, b, it)
        # bottom-left
        c = t.cell(1, 0)
        para = c.paragraphs[0]; para.paragraph_format.space_before = Pt(6)
        rich(para, '**Họ, tên thí sinh:** ' + '.' * 30, 11.5)
        para = c.add_paragraph(); rich(para, '**Số báo danh:** ' + '.' * 35, 11.5)
        # bottom-right: framed code box
        c = t.cell(1, 1)
        para = c.paragraphs[0]; para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.paragraph_format.left_indent = Cm(wr - 5.6); para.paragraph_format.space_before = Pt(6)
        pPr = para._p.get_or_add_pPr(); bd = OxmlElement('w:pBdr')
        for e in ('top', 'left', 'bottom', 'right'):
            x = OxmlElement('w:' + e); x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '8'); x.set(qn('w:space'), '3'); x.set(qn('w:color'), '000000'); bd.append(x)
        pPr.append(bd)
        rich(para, box or ('Mã đề thi %s' % ma_de), 12, True)
        self.d.add_paragraph().paragraph_format.space_after = Pt(0)
        return t

    def save(self, path):
        self.d.save(path)
