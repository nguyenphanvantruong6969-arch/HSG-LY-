# -*- coding: utf-8 -*-
"""Mau noi dung De 2 (kieu de that). Cac truong tuy chon cua moi cau:
 passage  doan van (hien trong khung) - dung cho cau DOK2 doc hieu
 stem     de bai chinh
 given    "Cho biet" (cong thuc/dang nghiem cho san, nhu cau DOK3 kieu Olympic)
 table / table_caption   bang so lieu: dict(header=[...], rows=[[...]], widths=[cm,...])
 fig      (ten_file.png, rong_cm, "Hinh n")
 parts    [(noi dung y, diem), ...]; tong diem cac y = pts
 sol      [(nhan y, diem, [doan | ("eq", latex) | ("table", dict)]), ...]
 common   ["Loi thuong gap ..."]
 ans_figs [(ten_file.png, rong_cm, chu thich)]  hinh chi hien trong file dap an
"""
TABLE = dict(header=[r"$t$ (s)", r"$x$ (m)"], rows=[["0", "0"], ["2", "4"], ["4", "8"]], widths=[3.0, 3.0])

ESS = [
 dict(pts=2, level="DOK2",
  passage=r"**Tiêu đề đoạn văn.** Viết 5-8 dòng mô tả một tình huống thực tế liên quan đến kiến thức chương; nêu công thức nền nếu cần.",
  stem=r"Một vật chuyển động thẳng đều; số liệu ở Bảng 1 và đồ thị ở Hình 1.",
  table=TABLE, table_caption="Bảng 1",
  fig=("t_fig.png", 6.0, "Hình 1"),
  parts=[(r"Tính tốc độ của vật từ bảng số liệu.", 1.0), (r"Giải thích vì sao đồ thị là đường thẳng.", 1.0)],
  sol=[("a", 1.0, [r"$v=\dfrac{8-0}{4-0}=2$ m/s."]), ("b", 1.0, [r"Vì $x=vt$ với $v$ không đổi nên $x$ tỉ lệ bậc nhất với $t$."])],
  common=[r"Đọc đồ thị sai đơn vị."],
 ),
 dict(pts=3, level="DOK3",
  stem=r"Tình huống mới, yêu cầu tự lập công thức tổng quát và liên hệ nhiều chủ đề trong chương.",
  given=r"**Cho biết.** Nêu công thức hoặc dạng nghiệm cần dùng, ví dụ $x=A\cos(\omega t+\varphi)$.",
  parts=[(r"Lập phương trình chuyển động.", 1.5), (r"Tính đại lượng yêu cầu và nhận xét.", 1.5)],
  sol=[("a", 1.5, [r"Lời giải ý a.", ("eq", r"x=A\cos(\omega t+\varphi)")]), ("b", 1.5, [r"Lời giải ý b."])],
  common=[r"Lỗi thường gặp của câu này."],
 ),
]
