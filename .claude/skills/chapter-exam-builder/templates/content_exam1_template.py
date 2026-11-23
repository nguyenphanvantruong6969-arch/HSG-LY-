# -*- coding: utf-8 -*-
"""Mau noi dung De 1. Quy uoc:
- opts[0] LA DAP AN DUNG; trinh dung se hoan vi de dap an dung nam o chu cai trong LETTERS.
- wrong[i] giai thich opts[i+1], bat dau bang 'B: ', 'C: ', 'D: ' hoac 'B, D: ' (theo thu tu goc, A = dung);
  builder tu doi sang chu cai that sau khi hoan vi.
- So thap phan trong cong thuc: viet 0,5 (builder tu doi thanh 0{,}5). Don vi dung ky tu Unicode: m/s², cm³.
- KHONG bat dau mot doan $...$ bang dau '=' hoac '\\approx' (builder tu tach); khong dung ngoac khong can nhu (a;b].
"""
LETTERS = "BA"   # do dai = so cau trac nghiem; chia deu A-D khi co 20 cau (moi chu cai 5 lan)

MCQ = [
 dict(
  q=r"Một vật chuyển động thẳng đều đi được 30 m trong 6 s. Tốc độ của vật là",
  opts=[r"5 m/s", r"0,2 m/s", r"180 m/s", r"36 m/s"],
  sol=[r"$v=\dfrac{s}{t}=\dfrac{30}{6}=5$ m/s."],
  wrong=[r"B: lấy $t/s$ (đảo tỉ số).", r"C: nhân thay vì chia ($s\cdot t$).", r"D: cộng hai số liệu."],
 ),
 dict(
  q=r"Hình 1 là đồ thị $x-t$ của một chuyển động thẳng đều. Tốc độ của vật là",
  fig=("t_fig.png", 6.0, "Hình 1"),
  opts=[r"2 m/s", r"4 m/s", r"0,5 m/s", r"8 m/s"],
  sol=[r"Hệ số góc của đoạn thẳng: $v=\dfrac{\Delta x}{\Delta t}=\dfrac{8-0}{4-0}=2$ m/s."],
  wrong=[r"B: đọc nhầm $\Delta x$ thành 8 và $\Delta t$ thành 2.", r"C: đảo tỉ số.", r"D: lấy giá trị $x$ cuối."],
 ),
]

ESS = [
 dict(pts=1.25, level="DOK1",
  stem=r"Hai xe xuất phát cùng lúc từ hai địa điểm cách nhau 120 km, đi ngược chiều với tốc độ 40 km/h và 20 km/h.",
  parts=[(r"Viết phương trình chuyển động của mỗi xe.", 0.5), (r"Tìm thời điểm và vị trí hai xe gặp nhau.", 0.75)],
  sol=[
   ("a", 0.5, [r"Chọn gốc tại xe thứ nhất, chiều dương theo chiều đi của nó:", ("eq", r"x_1=40t,\qquad x_2=120-20t")]),
   ("b", 0.75, [r"Gặp nhau khi $x_1=x_2$: $40t=120-20t\Rightarrow t=2$ h; $x=80$ km."]),
  ],
  common=[r"Quên đổi dấu vận tốc của xe đi ngược chiều dương."],
 ),
]
