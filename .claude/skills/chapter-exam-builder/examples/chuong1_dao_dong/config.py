# -*- coding: utf-8 -*-
"""Cau hinh vi du: De luyen tap Chuong 1 Dao dong dieu hoa (Vat li 11, Olympic TP.HCM).

Chay (tu thu muc skill):
  export EXAM_OUT_DIR=/duong/dan/dau/ra
  FIGDIR=$EXAM_OUT_DIR/figs PYTHONPATH=scripts python3 examples/chuong1_dao_dong/figs_de1.py
  FIGDIR=$EXAM_OUT_DIR/figs PYTHONPATH=scripts python3 examples/chuong1_dao_dong/figs_de2.py
  python3 scripts/build_exam.py examples/chuong1_dao_dong/config.py
  python3 scripts/build_solutions.py examples/chuong1_dao_dong/config.py
"""
import os
OUT_DIR = os.environ.get('EXAM_OUT_DIR', './out')
FIG_DIR = os.path.join(OUT_DIR, 'figs')

EXAMS = [
 dict(kind='mcq_essay', module='content_de1', out='chuong1_de1_co_ban.docx', code='101', footer='Mã đề thi 101',
      short='Đề 1', sol_title='ĐỀ 1 (MÃ ĐỀ 101)',
      left=[('ĐỀ LUYỆN TẬP', True, False), ('OLYMPIC VẬT LÍ 11 - TP.HCM', True, False), ('(Đề có {N} trang)', False, True)],
      right=[('KIỂM TRA CHƯƠNG 1', True, False), ('Bài thi: VẬT LÍ 11 - DAO ĐỘNG ĐIỀU HOÀ', True, False),
             ('Thời gian làm bài: 60 phút, không kể thời gian phát đề', False, True)],
      intro=r'Cho biết: gia tốc trọng trường $g=10$ m/s²; khi đề yêu cầu thì lấy $\pi^2=10$. Thí sinh không sử dụng tài liệu.',
      part1_title='PHẦN I. TRẮC NGHIỆM', part1_sub='({n_mcq} câu, mỗi câu 0,25 điểm; mỗi câu chỉ chọn một phương án)',
      part2_title='PHẦN II. TỰ LUẬN', part2_sub='({n_ess} câu, tổng 5,0 điểm; trình bày lời giải đầy đủ)',
      closing='Thí sinh không được sử dụng tài liệu. Giám thị không giải thích gì thêm.',
      extra_math=['g=10', r'\pi^2=10'],
      map={
 1: ('Chu kì, tần số', 'I. Chứng minh 1'),
 2: ('Quãng đường, chiều dài quỹ đạo', 'I. Chứng minh 4'),
 3: ('Vận tốc, gia tốc tại VTCB', 'III. Chứng minh 8, 9'),
 4: ('Chuyển hoá năng lượng', 'IV. Chứng minh 12'),
 5: ('Điều kiện cộng hưởng', 'V. Chứng minh 20'),
 6: ('Đổi sin sang cos, pha ban đầu', 'I. Mục 6 (công thức lượng giác)'),
 7: ('Đồ thị x-t, độ lệch pha', 'II. Chứng minh 7'),
 8: ('Hệ thức độc lập với thời gian', 'III. Chứng minh 11'),
 9: ('Wđ = nWt, cơ năng', 'IV. Chứng minh 12, 14'),
 10: ('Lò xo treo: ω từ độ dãn', 'IV. Chứng minh 15'),
 11: ('Đường tròn pha, lần thứ n', 'I. Chứng minh 2, 3'),
 12: ('Đồ thị a-x, cơ năng', 'III. Chứng minh 9; IV. Chứng minh 12'),
 13: ('Quãng đường theo thời gian', 'I. Chứng minh 3, 4'),
 14: ('Lò xo đứng, chiều dài, lực đàn hồi', 'IV. Chứng minh 15'),
 15: ('Con lắc đơn góc nhỏ, đổi độ sang rad', 'IV. Chứng minh 16'),
 16: ('Tắt dần, % biên độ và năng lượng', 'V. Chứng minh 17'),
 17: ('Ma sát trượt, VTCB tạm thời', 'V. Chứng minh 18'),
 18: ('Đồ thị Wt-t, tần số 2ω', 'IV. Chứng minh 13'),
 19: ('Cộng hưởng khi xe qua rãnh', 'V. Chứng minh 19; IV. Chứng minh 15'),
 20: ('Va chạm mềm trên con lắc lò xo', 'IV. Chứng minh 12, 15 (+ bảo toàn động lượng)'),
 21: ('Viết phương trình, đường tròn pha', 'I. Chứng minh 2, 3, 6'),
 22: ('Lò xo ngang, đồ thị Wt-x, Wđ = nWt', 'IV. Chứng minh 12 - 15'),
 23: ('Lò xo đứng, thời gian nén', 'IV. Chứng minh 15; I. Chứng minh 3'),
 24: ('Tắt dần, công suất bù, cộng hưởng', 'V. Chứng minh 17, 20'),
}),
 dict(kind='dok', module='content_de2', out='chuong1_de2_dok_olympic.docx', code='201', footer='Mã đề thi 201',
      short='Đề 2', sol_title='ĐỀ 2 (MÃ ĐỀ 201)',
      left=[('ĐỀ LUYỆN TẬP', True, False), ('OLYMPIC VẬT LÍ 11 - TP.HCM', True, False), ('(Đề có {N} trang)', False, True)],
      right=[('KIỂM TRA CHUYÊN SÂU CHƯƠNG 1', True, False), ('Bài thi: VẬT LÍ 11 - DAO ĐỘNG ĐIỀU HOÀ', True, False),
             ('Thời gian làm bài: 180 phút, không kể thời gian phát đề', False, True)],
      intro=r'Đề gồm 9 câu, tổng 20 điểm (mức DOK2: Câu 1-3; mức DOK3: Câu 4-9). Thí sinh được dùng máy tính cầm tay, không dùng tài liệu. Khi đề không nói gì thêm, lấy $g=10$ m/s².',
      closing='Thí sinh không được sử dụng tài liệu. Giám thị không giải thích gì thêm.',
      extra_math=['g=10'],
      sol_note='Thang điểm: Câu 1-5, 7, 8: 2 điểm mỗi câu; Câu 6, 9: 3 điểm mỗi câu. Tổng 20 điểm. Các số liệu đọc từ đồ thị là giá trị gần đúng; chấp nhận sai lệch nhỏ.',
      map={
 1: ('Đọc đồ thị x-t, a-t; vẽ v-t; kiểm tra a = -ω²x', 'II; III. Chứng minh 8, 9, 10, 11'),
 2: ('Cộng hưởng, tốc độ nguy hiểm, giảm xóc', 'V. Chứng minh 19, 20'),
 3: ('Con lắc đơn, đồ thị T²-ℓ, sai số', 'IV. Chứng minh 16'),
 4: ('Va chạm mềm, VTCB dịch chuyển, phương trình', 'IV. Chứng minh 12, 15; I. Chứng minh 6'),
 5: ('Hai vật chồng nhau, điều kiện không rời, ma sát nghỉ', 'III. Chứng minh 9; IV. Chứng minh 15'),
 6: ('Ma sát trượt Coulomb, biên độ giảm đều', 'V. Chứng minh 18'),
 7: ('Cột chất lỏng chữ U, lập phương trình a = -ω²y', 'III. Chứng minh 9; IV. Chứng minh 15 (kĩ thuật tương tự)'),
 8: ('Con lắc đơn trong trường hiệu dụng', 'IV. Chứng minh 16'),
 9: ('Tắt dần nhớt, cưỡng bức, hệ số phẩm chất', 'V. Chứng minh 17, 20; Câu 17 trong PDF'),
}),
]

SOL = dict(
 out='chuong1_dap_an_loi_giai.docx', footer='Đáp án và lời giải',
 left=[('ĐỀ LUYỆN TẬP', True, False), ('OLYMPIC VẬT LÍ 11 - TP.HCM', True, False), ('(Gồm {N} trang)', False, True)],
 right=[('ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT', True, False), ('Chương 1: Dao động điều hoà', True, False),
        ('Mã đề thi 101 và Mã đề thi 201', False, True)],
 box='Đáp án',
 intro=r'Tài liệu này chứa lời giải; chỉ mở sau khi đã làm bài. Lấy $g=10$ m/s² và $\pi^2=10$ khi đề yêu cầu.',
 map_note='Cột cuối chỉ mục cần ôn lại trong tài liệu giải thích Chương 1 (chuong1_dao_dong_dieu_hoa.html) và phần tương ứng của PDF Olympic: I. Dao động điều hoà; II. Mô tả; III. Vận tốc, gia tốc; IV. Năng lượng, con lắc; V. Tắt dần, cưỡng bức, cộng hưởng.',
 extra_math=['g=10', r'\pi^2=10'],
)
