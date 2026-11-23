# -*- coding: utf-8 -*-
"""Kiem tra tu dong cac file docx: khong emoji, khong ro ri loi giai trong file de, dem cau/anh/cong thuc.

Cach dung:
  python3 verify_docs.py --exam de1.docx de2.docx --solutions dapan.docx
"""
import argparse, re, sys, zipfile
from docx import Document
from lxml import etree

M = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
RANGES = [(0x1F000, 0x1FAFF), (0x2600, 0x27BF), (0x2B00, 0x2BFF), (0xFE0F, 0xFE0F)]   # emoji, dingbats, symbols
BAD = re.compile('[' + ''.join('%s-%s' % (chr(a), chr(b)) for a, b in RANGES) + ']')

def alltext(path):
    z = zipfile.ZipFile(path); out = []
    for n in z.namelist():
        if n.endswith('.xml'):
            out.append(re.sub(r'<[^>]+>', '', z.read(n).decode('utf8', 'ignore')))
    return '\n'.join(out)

def check(path, is_exam):
    assert zipfile.ZipFile(path).testzip() is None, 'zip loi: ' + path
    d = Document(path)
    xml = etree.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    txt = alltext(path)
    emoji = BAD.findall(txt)
    body = '\n'.join(p.text for p in d.paragraphs)
    ncau = len(re.findall(r'^Câu \d+', body, re.M))
    res = dict(file=path, equations=len(xml.findall('.//' + M + 'oMath')),
               images=len(xml.findall('.//' + A + 'blip')), cau=ncau, emoji=emoji)
    ok = not emoji and '¿' not in txt
    if is_exam:
        leak = 'Lời giải' in txt or 'Đáp án' in txt
        res['leak'] = leak; ok = ok and not leak
    res['ok'] = ok
    return res

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--exam', nargs='*', default=[]); ap.add_argument('--solutions', nargs='*', default=[])
    a = ap.parse_args(); bad = False
    for f in a.exam: r = check(f, True); print(r); bad |= not r['ok']
    for f in a.solutions: r = check(f, False); print(r); bad |= not r['ok']
    sys.exit(1 if bad else 0)
