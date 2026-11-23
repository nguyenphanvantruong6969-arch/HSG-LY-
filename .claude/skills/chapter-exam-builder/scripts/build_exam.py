# -*- coding: utf-8 -*-
"""Dung cac file de (docx) tu config.py.

  python3 build_exam.py path/to/config.py [--tmp DIR]

config.py phai dinh nghia OUT_DIR, FIG_DIR, EXAMS (xem templates/config_template.py).
Moi phan tu cua EXAMS co kind = 'mcq_essay' hoac 'dok'.
"""
import sys, os, argparse, importlib, importlib.util, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render
from render import *

def load_config(path):
    path = os.path.abspath(path)
    sys.path.insert(0, os.path.dirname(path))
    spec = importlib.util.spec_from_file_location('exam_config', path)
    cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
    render.FIG = cfg.FIG_DIR
    return cfg

def fill(s, **kw):
    for k, v in kw.items():
        s = s.replace('{%s}' % k, str(v))
    return s

def header(D, ex, npages):
    D.footer(ex['footer'])
    D.exam_header(ex['code'], ex['left'], ex['right'], npages, box=ex.get('box'))

def build_mcq_essay(ex, C, npages):
    D = Doc()
    header(D, ex, npages)
    n_mcq, n_ess = len(C.MCQ), len(C.ESS)
    assert len(C.LETTERS) == n_mcq, 'LETTERS phai co do dai bang so cau trac nghiem'
    if ex.get('intro'):
        D.p(ex['intro'], size=11.5, italic=True, after=4, align='c')
    D.p(ex['part1_title'], bold=True, align='c', after=0, keep_next=True)
    D.p(fill(ex['part1_sub'], n_mcq=n_mcq), size=11.5, italic=True, align='c', after=4, keep_next=True)
    D.section(2)
    for i, item in enumerate(C.MCQ, 1):
        mcq(D, i, item, C.LETTERS[i - 1])
    D.section(1)
    D.p(ex['part2_title'], bold=True, align='c', after=0, before=4, keep_next=True)
    D.p(fill(ex['part2_sub'], n_ess=n_ess), size=11.5, italic=True, align='c', after=4, keep_next=True)
    for j, item in enumerate(C.ESS, n_mcq + 1):
        essay(D, j, item, show_pts=True, show_level=ex.get('show_level', False))
    D.p('-------- HẾT --------', align='c', bold=True, before=6, after=0)
    if ex.get('closing'):
        D.p(ex['closing'], size=11, italic=True, align='c')
    return D

def build_dok(ex, C, npages):
    D = Doc()
    header(D, ex, npages)
    if ex.get('intro'):
        D.p(ex['intro'], size=11.5, italic=True, after=6, align='c')
    for n, item in enumerate(C.ESS, 1):
        essay(D, n, item, show_pts=True, show_level=ex.get('show_level', True))
        D.p('', after=2)
    D.p('-------- HẾT --------', align='c', bold=True, before=6, after=0)
    if ex.get('closing'):
        D.p(ex['closing'], size=11, italic=True, align='c')
    return D

BUILDERS = {'mcq_essay': build_mcq_essay, 'dok': build_dok}

def collect_math(C, ex):
    items = [(False, s) for s in ex.get('extra_math', [])]
    for attr in ('MCQ', 'ESS'):
        if hasattr(C, attr): scan_math(getattr(C, attr), items)
    for key in ('intro', 'closing', 'part1_sub', 'part2_sub'):
        if ex.get(key): scan_math(ex[key], items)
    return items

def build_one(cfg, ex, tmp):
    C = importlib.import_module(ex['module'])
    MATH.load(collect_math(C, ex))
    out = os.path.join(cfg.OUT_DIR, ex['out'])
    os.makedirs(cfg.OUT_DIR, exist_ok=True)
    n = ex.get('pages_guess', 5)
    for _ in range(3):
        D = BUILDERS[ex['kind']](ex, C, n); D.save(out)
        n2 = pages_of(to_pdf(out, tmp))
        if n2 == n: break
        n = n2
    print('%s: %d trang -> %s' % (ex['out'], n, out))
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('config'); ap.add_argument('--tmp')
    a = ap.parse_args()
    cfg = load_config(a.config)
    tmp = a.tmp or tempfile.mkdtemp(prefix='exam_pdf_')
    os.makedirs(tmp, exist_ok=True)
    for ex in cfg.EXAMS:
        build_one(cfg, ex, tmp)
    print('PDF xem truoc o:', tmp)
