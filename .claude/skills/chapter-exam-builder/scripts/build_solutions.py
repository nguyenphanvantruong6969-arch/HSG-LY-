# -*- coding: utf-8 -*-
"""Dung file dap an + loi giai gop cho tat ca de trong config.py.

  python3 build_solutions.py path/to/config.py [--tmp DIR]

config.py can: OUT_DIR, FIG_DIR, EXAMS (cung danh sach voi build_exam.py), SOL (dict, xem template).
Moi exam co them: short, sol_title, map ({so_cau: (kien thuc, muc on lai)}), sol_note (tuy chon).
"""
import sys, os, argparse, importlib, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render
from render import *
from build_exam import load_config

def f1(x): return ('%g' % x).replace('.', ',')

def letters_of(i): return 'ABCDEFGH'[i]

def block_mcq_essay(D, ex, C, part_letter):
    D.p('PHẦN %s. %s' % (part_letter, ex['sol_title']), bold=True, size=13, before=8, after=3, keep_next=True)
    D.p('**%s.1. Bảng đáp án trắc nghiệm** (Phần I)' % part_letter, after=3, keep_next=True)
    L = C.LETTERS; n = len(L)
    rows = []
    for s in range(0, n, 10):
        chunk = range(s, min(s + 10, n))
        r1 = ['Câu'] + [str(i + 1) for i in chunk] + [''] * (10 - len(chunk))
        r2 = ['Đáp án'] + [L[i] for i in chunk] + [''] * (10 - len(chunk))
        rows += [r1, r2]
    D.table(rows, [2.3] + [1.5] * 10, header=False, size=11.5, align=['c'] * 11, bold_first_col=True)
    D.p('**%s.2. Lời giải chi tiết Phần I**' % part_letter, after=3, keep_next=True)
    for i, it in enumerate(C.MCQ, 1):
        k = L[i - 1]; mp = perm_map(k)
        D.p('**Câu %d.** Đáp án **%s**.' % (i, k), after=1, keep_next=True, before=3)
        sol_items(D, it['sol'])
        for w in it['wrong']:
            D.p('Phương án nhiễu — ' + remap_wrong(w, mp), left=0.9, size=11, after=1)
    a, b = n + 1, n + len(C.ESS)
    D.p('**%s.3. Lời giải Phần II (Câu %d-%d)**' % (part_letter, a, b), after=3, before=6, keep_next=True)
    for j, e in enumerate(C.ESS, a):
        D.p('**Câu %d.** (%s điểm)' % (j, f1(e['pts'])), after=1, keep_next=True, before=3)
        solution_parts(D, e)
        figs = list(e.get('ans_figs', []))
        if e.get('ans_fig'): figs.append(e['ans_fig'])
        for f, w, cap in figs:
            D.figure(os.path.join(render.FIG, f), w, cap, after=3)
        if e.get('common'):
            D.p('**Lỗi thường gặp:** ' + e['common'][0], left=0.9, size=11, after=3)

def solution_parts(D, e):
    for lab, pt, items in e['sol']:
        D.p('**%s)** (%s đ)' % (lab, f1(pt)), left=0.5, after=1, keep_next=True)
        sol_items(D, items)

def block_dok(D, ex, C, part_letter):
    D.p('PHẦN %s. %s' % (part_letter, ex['sol_title']), bold=True, size=13, before=10, after=3, keep_next=True)
    if ex.get('sol_note'):
        D.p(ex['sol_note'], size=11.5, italic=True, after=4)
    for n, e in enumerate(C.ESS, 1):
        lv = (' [%s]' % e['level']) if e.get('level') else ''
        D.p('**Câu %d.** (%s điểm)%s' % (n, f1(e['pts']), lv), after=1, keep_next=True, before=5)
        solution_parts(D, e)
        for f, w, cap in e.get('ans_figs', []):
            D.figure(os.path.join(render.FIG, f), w, cap, after=3)
        if e.get('common'):
            D.p('**Lỗi thường gặp:** ' + e['common'][0], left=0.9, size=11, after=3)

def build(cfg, mods, npages):
    S = cfg.SOL
    D = Doc()
    D.footer(S['footer'])
    D.exam_header('', S['left'], S['right'], npages, box=S.get('box', 'Đáp án'))
    if S.get('intro'):
        D.p(S['intro'], size=11.5, italic=True, after=6, align='c')
    for i, (ex, C) in enumerate(zip(cfg.EXAMS, mods)):
        pl = letters_of(i)
        (block_mcq_essay if ex['kind'] == 'mcq_essay' else block_dok)(D, ex, C, pl)
    pl = letters_of(len(cfg.EXAMS))
    D.p('PHẦN %s. BẢNG ÁNH XẠ KIẾN THỨC' % pl, bold=True, size=13, before=10, after=3, keep_next=True)
    if S.get('map_note'):
        D.p(S['map_note'], size=11.5, after=4)
    for ex in cfg.EXAMS:
        rows = [['Câu', 'Kiến thức chính', 'Mục ôn lại']]
        for n, (a, b) in ex['map'].items():
            rows.append(['%s - Câu %d' % (ex['short'], n), a, b])
        D.table(rows, [2.6, 7.4, 7.4], header=True, size=10.5, shade_header=True)
    D.p('-------- HẾT --------', align='c', bold=True, before=6, after=0)
    return D

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('config'); ap.add_argument('--tmp')
    a = ap.parse_args()
    cfg = load_config(a.config)
    mods = [importlib.import_module(ex['module']) for ex in cfg.EXAMS]
    items = [(False, s) for s in cfg.SOL.get('extra_math', [])]
    for C in mods:
        for attr in ('MCQ', 'ESS'):
            if hasattr(C, attr): scan_math(getattr(C, attr), items)
    for key in ('intro', 'map_note'):
        if cfg.SOL.get(key): scan_math(cfg.SOL[key], items)
    for ex in cfg.EXAMS:
        if ex.get('sol_note'): scan_math(ex['sol_note'], items)
    MATH.load(items)
    tmp = a.tmp or tempfile.mkdtemp(prefix='exam_pdf_'); os.makedirs(tmp, exist_ok=True)
    out = os.path.join(cfg.OUT_DIR, cfg.SOL['out']); os.makedirs(cfg.OUT_DIR, exist_ok=True)
    n = cfg.SOL.get('pages_guess', 12)
    for _ in range(3):
        D = build(cfg, mods, n); D.save(out)
        n2 = pages_of(to_pdf(out, tmp))
        if n2 == n: break
        n = n2
    print('%s: %d trang -> %s' % (cfg.SOL['out'], n, out))
