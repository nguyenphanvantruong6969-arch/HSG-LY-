# -*- coding: utf-8 -*-
import os, re, subprocess
from lib import *

FIG = os.environ.get('FIGDIR')

def est_len(s):
    n = 0
    for part in re.split(r'(\$.+?\$)', s):
        if part.startswith('$'):
            n += len(re.sub(r'\\[a-zA-Z]+', 'x', part[1:-1])) * 0.6
        else:
            n += len(part)
    return n

def order_options(opts, letter):
    k = 'ABCD'.index(letter)
    rest = list(opts[1:])
    out = []
    for i in range(4):
        out.append(opts[0] if i == k else rest.pop(0))
    return out

def mcq(D, n, item, letter):
    p = D.p('**Câu %d:** %s' % (n, item['q']), keep_next=True, after=2, align=None)
    if item.get('fig'):
        f, w, cap = item['fig']
        D.figure(os.path.join(FIG, f), min(w, D.col_w - 0.3), cap, after=3)
    opts = order_options(item['opts'], letter)
    L = max(est_len(o) for o in opts)
    lay = item.get('layout') or ('4x1' if L <= 5 else '2x2' if L <= 14 else '1')
    labels = 'ABCD'
    if lay == '4x1':
        para = D.d.add_paragraph(); pf = para.paragraph_format
        pf.space_after = Pt(5)
        w = D.col_w / 4
        for i in range(1, 4):
            pf.tab_stops.add_tab_stop(Cm(w * i))
        for i, o in enumerate(opts):
            rich(para, '**%s.** %s' % (labels[i], o))
            if i < 3: para.add_run('\t')
    elif lay == '2x2':
        for r in range(2):
            para = D.d.add_paragraph(); pf = para.paragraph_format
            pf.space_after = Pt(1 if r == 0 else 5)
            pf.keep_with_next = (r == 0)
            pf.tab_stops.add_tab_stop(Cm(D.col_w / 2))
            rich(para, '**%s.** %s' % (labels[2 * r], opts[2 * r])); para.add_run('\t')
            rich(para, '**%s.** %s' % (labels[2 * r + 1], opts[2 * r + 1]))
    else:
        for i, o in enumerate(opts):
            para = D.p('**%s.** %s' % (labels[i], o), after=(5 if i == 3 else 1), left=0.55, first=-0.55, keep_next=(i < 3))

def boxed(D, text, size=11.5, after=4):
    para = D.p(text, size=size, after=after, align=None, left=0.3)
    pPr = para._p.get_or_add_pPr(); bd = OxmlElement('w:pBdr')
    for e in ('top', 'left', 'bottom', 'right'):
        x = OxmlElement('w:' + e); x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '4'); x.set(qn('w:space'), '4'); x.set(qn('w:color'), '000000'); bd.append(x)
    pPr.append(bd)
    para.paragraph_format.right_indent = Cm(0.3)
    return para

def data_table(D, tb, size=11.5):
    rows = [tb['header']] + tb['rows']
    return D.table(rows, tb['widths'], header=True, size=size, align=['c'] * len(tb['widths']), shade_header=True)

def essay(D, n, item, show_pts=True, show_level=False):
    head = '**Câu %d.**' % n
    if show_pts:
        head += ' (%s điểm)' % ('%g' % item['pts']).replace('.', ',')
    if show_level and item.get('level'):
        head += ' [%s]' % item['level']
    if item.get('passage'):
        D.p(head, keep_next=True, after=3)
        boxed(D, item['passage'])
        D.p(item['stem'], keep_next=True, after=3, align=None)
    else:
        D.p('%s %s' % (head, item['stem']), keep_next=True, after=3, align=None)
    if item.get('given'):
        D.p(item['given'], after=3, align=None, keep_next=True)
    if item.get('table'):
        if item.get('table_caption'):
            D.p(item['table_caption'], size=11, bold=True, align='c', after=2, keep_next=True)
        data_table(D, item['table'])
    if item.get('fig'):
        f, w, cap = item['fig']
        D.figure(os.path.join(FIG, f), w, cap, after=4)
    labels = 'abcdefgh'
    for i, (txt, pt) in enumerate(item['parts']):
        suffix = ' (%s đ)' % ('%g' % pt).replace('.', ',') if show_pts else ''
        D.p('%s) %s%s' % (labels[i], txt, suffix), left=0.9, first=-0.5, after=3, align=None, keep_next=(i < len(item['parts']) - 1))

def pages_of(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', out).group(1))

def to_pdf(docx_path, outdir):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx_path],
                   capture_output=True, timeout=240)
    return os.path.join(outdir, os.path.splitext(os.path.basename(docx_path))[0] + '.pdf')


def sol_items(D, items, left=0.9):
    for it in items:
        if isinstance(it, tuple) and it[0] == 'eq':
            D.display(it[1], after=3)
        elif isinstance(it, tuple) and it[0] == 'table':
            data_table(D, it[1], size=11)
        else:
            D.p(it, left=left, after=3, align=None)

def remap_wrong(text, perm_letters):
    """text begins with 'B: ' or 'B, D: ' in original order (A = correct); map to shuffled letters."""
    m = re.match(r'^([A-D](?:, [A-D])*): (.*)$', text, re.S)
    if not m:
        return text
    letters = [perm_letters[x] for x in m.group(1).split(', ')]
    return '%s: %s' % (', '.join(sorted(letters)), m.group(2))

def perm_map(correct_letter):
    """original index -> shuffled letter, consistent with order_options"""
    k = 'ABCD'.index(correct_letter)
    mp = {'A': correct_letter}
    others = [c for c in 'ABCD' if c != correct_letter]
    for orig, dst in zip('BCD', others):
        mp[orig] = dst
    return mp
