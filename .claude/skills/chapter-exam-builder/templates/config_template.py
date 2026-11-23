# -*- coding: utf-8 -*-
"""Mau cau hinh. Sao chep sang thu muc lam viec moi, doi ten cac module noi dung va chuoi tieu de.

Che do chay thu mau nay (khong sua gi):
  export EXAM_OUT_DIR=/tmp/exam_demo && mkdir -p $EXAM_OUT_DIR/figs
  FIGDIR=$EXAM_OUT_DIR/figs PYTHONPATH=scripts python3 templates/figs_template.py
  python3 scripts/build_exam.py templates/config_template.py
  python3 scripts/build_solutions.py templates/config_template.py
"""
import os
OUT_DIR = os.environ.get('EXAM_OUT_DIR', './out')     # noi ghi .docx
FIG_DIR = os.path.join(OUT_DIR, 'figs')               # noi chua hinh .png (do figs_*.py tao)

# Dau trang trung tinh: KHONG ghi ten co quan nha nuoc, KHONG ghi "De thi chinh thuc".
HEAD_LEFT = [('ĐỀ LUYỆN TẬP', True, False), ('<TÊN KÌ THI / LỚP>', True, False), ('(Đề có {N} trang)', False, True)]

EXAMS = [
 # ---- De 1: trac nghiem (hai cot) + tu luan. LETTERS trong module noi dung phai du 5/5/5/5 hoac can bang.
 dict(kind='mcq_essay', module='content_exam1_template', out='de1.docx', code='101', footer='Mã đề thi 101',
      short='Đề 1', sol_title='ĐỀ 1 (MÃ ĐỀ 101)',
      left=HEAD_LEFT,
      right=[('KIỂM TRA CHƯƠNG <N>', True, False), ('Bài thi: <MÔN> - <TÊN CHƯƠNG>', True, False),
             ('Thời gian làm bài: 60 phút, không kể thời gian phát đề', False, True)],
      intro=r'Cho biết: <hằng số cần thiết>, ví dụ $g=10$ m/s². Thí sinh không sử dụng tài liệu.',
      part1_title='PHẦN I. TRẮC NGHIỆM', part1_sub='({n_mcq} câu; mỗi câu chỉ chọn một phương án)',
      part2_title='PHẦN II. TỰ LUẬN', part2_sub='({n_ess} câu; trình bày lời giải đầy đủ)',
      closing='Thí sinh không được sử dụng tài liệu. Giám thị không giải thích gì thêm.',
      extra_math=['g=10'],
      # ban anh xa: so cau -> (kien thuc chinh, muc on lai trong tai lieu)
      map={1: ('<kiến thức câu 1>', '<mục trong tài liệu>'), 2: ('<kiến thức câu 2>', '<mục trong tài liệu>')}),
 # ---- De 2: kieu de that, DOK2/DOK3, mot cot.
 dict(kind='dok', module='content_exam2_template', out='de2.docx', code='201', footer='Mã đề thi 201',
      short='Đề 2', sol_title='ĐỀ 2 (MÃ ĐỀ 201)',
      left=HEAD_LEFT,
      right=[('KIỂM TRA CHUYÊN SÂU CHƯƠNG <N>', True, False), ('Bài thi: <MÔN> - <TÊN CHƯƠNG>', True, False),
             ('Thời gian làm bài: 180 phút, không kể thời gian phát đề', False, True)],
      intro='Đề gồm <số câu> câu, tổng 20 điểm. Thí sinh được dùng máy tính cầm tay, không dùng tài liệu.',
      closing='Thí sinh không được sử dụng tài liệu. Giám thị không giải thích gì thêm.',
      sol_note='Thang điểm: <ghi điểm từng câu>. Tổng 20 điểm. Số liệu đọc từ đồ thị là giá trị gần đúng.',
      map={1: ('<kiến thức câu 1>', '<mục trong tài liệu>'), 2: ('<kiến thức câu 2>', '<mục trong tài liệu>')}),
]

SOL = dict(
 out='dap_an_loi_giai.docx', footer='Đáp án và lời giải',
 left=[('ĐỀ LUYỆN TẬP', True, False), ('<TÊN KÌ THI / LỚP>', True, False), ('(Gồm {N} trang)', False, True)],
 right=[('ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT', True, False), ('<TÊN CHƯƠNG>', True, False),
        ('Mã đề thi 101 và Mã đề thi 201', False, True)],
 box='Đáp án',
 intro='Tài liệu này chứa lời giải; chỉ mở sau khi đã làm bài.',
 map_note='Cột cuối chỉ mục cần ôn lại trong tài liệu chương.',
 extra_math=[],
)
