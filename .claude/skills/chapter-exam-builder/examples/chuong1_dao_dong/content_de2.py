# -*- coding: utf-8 -*-
"""De 2: kieu de that (DOK2 / DOK3), 9 cau, 20 diem, 180 phut."""

TABLE3 = dict(
 header=[r"$\ell$ (m)", r"$t_{10}$ (s)", r"$T$ (s)", r"$T^2$ (s²)"],
 rows=[["0,300", "11,0", "", ""], ["0,400", "12,8", "", ""], ["0,500", "14,1", "", ""],
       ["0,600", "15,6", "", ""], ["0,700", "16,7", "", ""], ["0,800", "18,0", "", ""]],
 widths=[3.0, 3.0, 3.0, 3.0],
)
TABLE3_FILLED = dict(
 header=TABLE3['header'],
 rows=[["0,300", "11,0", "1,100", "1,210"], ["0,400", "12,8", "1,280", "1,638"], ["0,500", "14,1", "1,410", "1,988"],
       ["0,600", "15,6", "1,560", "2,434"], ["0,700", "16,7", "1,670", "2,789"], ["0,800", "18,0", "1,800", "3,240"]],
 widths=TABLE3['widths'],
)

ESS = [
# ------------------------------------------------------------------ 1
dict(pts=2, level="DOK2",
 stem=r"Một vật nhỏ gắn vào lò xo treo thẳng đứng dao động điều hoà. Một cảm biến chuyển động ghi lại độ cao $h$ của vật so với mặt đất theo thời gian; máy tính vẽ đồ thị $h-t$ và $a-t$ (gia tốc thẳng đứng, chiều dương hướng lên) như Hình 1. Đồ thị vận tốc $v-t$ bị bỏ trống.",
 fig=("d2_c1.png", 9.6, "Hình 1"),
 parts=[
  (r"Từ đồ thị $h-t$, xác định biên độ, chu kì, tần số, tần số góc của dao động và độ cao của vị trí cân bằng.", 0.5),
  (r"Xác định pha ban đầu và viết phương trình $h(t)$ dưới dạng $h=h_{CB}+A\cos(\omega t+\varphi)$. Chứng minh tốc độ cực đại của vật xấp xỉ $1{,}2$ m/s.", 0.5),
  (r"Hoàn thành đồ thị $v-t$ trên khung trống của Hình 1 bằng cách đánh dấu các điểm đặc biệt trong khoảng $0\le t\le1{,}6$ s.", 0.5),
  (r"Mô tả và thực hiện một phép kiểm tra định lượng (có số liệu đọc từ hai đồ thị $h-t$ và $a-t$) để chứng tỏ chuyển động là dao động điều hoà. So sánh giá trị tìm được với giá trị tính từ chu kì.", 0.5),
 ],
 sol=[
  ("a", 0.5, [r"$h_{max}=0{,}75$ m, $h_{min}=0{,}45$ m nên $A=\dfrac{0{,}75-0{,}45}{2}=0{,}15$ m và $h_{CB}=\dfrac{0{,}75+0{,}45}{2}=0{,}60$ m.", r"Hai đỉnh liên tiếp ở $t\approx0{,}13$ s và $t\approx0{,}93$ s nên $T=0{,}80$ s; $f=\dfrac1T=1{,}25$ Hz; $\omega=\dfrac{2\pi}{T}=2{,}5\pi\approx7{,}85$ rad/s."]),
  ("b", 0.5, [r"Tại $t=0$: $h\approx0{,}675$ m nên $\cos\varphi=\dfrac{0{,}675-0{,}60}{0{,}15}=0{,}5$, $\varphi=\pm\dfrac\pi3$. Đồ thị đang đi lên ($v>0$) nên $\varphi<0$: $\varphi=-\dfrac\pi3$.", ("eq", r"h=0{,}60+0{,}15\cos\left(2{,}5\pi t-\dfrac\pi3\right)\ \text{m}"), r"$v_{max}=\omega A=7{,}85\cdot0{,}15\approx1{,}18$ m/s $\approx1{,}2$ m/s."]),
  ("c", 0.5, [r"$v=-\omega A\sin\left(\omega t-\dfrac\pi3\right)=1{,}18\cos\left(2{,}5\pi t+\dfrac\pi6\right)$ (m/s): $v$ sớm pha $\dfrac\pi2$ so với $h$. Các điểm cần đánh dấu: $v(0)\approx+1{,}02$ m/s; $v=0$ tại $t\approx0{,}13;\ 0{,}53;\ 0{,}93;\ 1{,}33$ s (khi $h$ ở đỉnh hoặc đáy); $v=-1{,}18$ m/s tại $t\approx0{,}33$ s và $1{,}13$ s; $v=+1{,}18$ m/s tại $t\approx0{,}73$ s và $1{,}53$ s (khi $h=h_{CB}$). Đường cong hình sin chu kì $0{,}8$ s (xem hình đáp án)."]),
  ("d", 0.5, [r"Dao động điều hoà khi $a=-\omega^2x$, tức $\dfrac ax$ là hằng số âm với $x=h-h_{CB}$. Lấy ba thời điểm: $t=0$: $x=+0{,}075$ m, $a\approx-4{,}6$ m/s² nên $\dfrac ax\approx-61{,}7$ s⁻²; $t=0{,}13$ s: $x=+0{,}15$ m, $a\approx-9{,}3$ m/s² nên $\dfrac ax\approx-61{,}7$ s⁻²; $t=0{,}53$ s: $x=-0{,}15$ m, $a\approx+9{,}3$ m/s² nên $\dfrac ax\approx-61{,}7$ s⁻².", r"Giá trị tính từ chu kì: $\omega^2=\left(\dfrac{2\pi}{0{,}8}\right)^2=61{,}7$ s⁻², trùng với $-\dfrac ax$ (và $\dfrac{a_{max}}{A}=\dfrac{9{,}25}{0{,}15}=61{,}7$ s⁻²). Tỉ số không đổi và khớp với $\omega^2$ nên chuyển động là dao động điều hoà; hai đồ thị $h$ và $a$ ngược pha cũng phù hợp."]),
 ],
 common=[r"Đọc chu kì từ khoảng cách đỉnh - đáy; quên nhân $\omega$ khi tính $v_{max}$; chọn $\varphi=+\dfrac\pi3$ do bỏ qua dấu của $v$ lúc $t=0$."],
 ans_figs=[("a_c1.png", 9.6, "Hình đáp án Câu 1: đồ thị v - t hoàn chỉnh (khung dưới cùng)")],
),
# ------------------------------------------------------------------ 2
dict(pts=2, level="DOK2",
 passage=r"**Gờ giảm tốc và dao động của xe.** Trên nhiều tuyến đường vào khu dân cư, người ta đặt các gờ giảm tốc cách đều nhau để buộc xe chạy chậm. Mỗi khi bánh xe đi qua một gờ, thân xe nhận một cú đẩy qua hệ treo. Nếu các gờ cách đều nhau thì các cú đẩy lặp lại tuần hoàn, với chu kì bằng thời gian xe đi hết khoảng cách giữa hai gờ liên tiếp. Hệ treo gồm lò xo và bộ giảm xóc; nếu bỏ qua lực cản thì thân xe dao động trên lò xo với chu kì riêng $T_0=2\pi\sqrt{m/k}$. Người ngồi trên xe cảm thấy xe nảy mạnh nhất ở một tốc độ nhất định, và êm hơn khi xe chạy nhanh hơn hoặc chậm hơn nhiều so với tốc độ đó.",
 stem=r"Xét một xe tải nhỏ có khối lượng được lò xo đỡ $m=1000$ kg, độ cứng tổng cộng của hệ lò xo $k=1{,}6\cdot10^5$ N/m. Các gờ giảm tốc cách nhau $L=3{,}0$ m (Hình 2). Lấy $\pi^2=10$.",
 fig=("d2_c2.png", 11.0, "Hình 2"),
 parts=[
  (r"Tính chu kì riêng $T_0$ và tần số riêng $f_0$ của thân xe.", 0.5),
  (r"Giải thích vì sao thân xe chịu tác dụng của một lực cưỡng bức tuần hoàn. Viết biểu thức chu kì và tần số của lực này theo $L$ và tốc độ $v$ của xe.", 0.5),
  (r"Tính tốc độ (m/s và km/h) để xe rung mạnh nhất. Gọi tên hiện tượng.", 0.5),
  (r"Đoạn đường quy định giới hạn tốc độ 20 km/h. Hãy nhận xét về thiết kế này. Xe chạy 36 km/h thì tần số lực cưỡng bức là bao nhiêu và biên độ dao động lớn hơn hay nhỏ hơn so với ở ý c? Đề xuất hai biện pháp làm giảm biên độ dao động của xe.", 0.5),
 ],
 sol=[
  ("a", 0.5, [r"$T_0=2\pi\sqrt{\dfrac mk}=2\pi\sqrt{\dfrac{1000}{1{,}6\cdot10^5}}=\dfrac{2\pi}{\sqrt{160}}$. Với $\pi^2=10$: $T_0=2\sqrt{\dfrac{10}{160}}=0{,}5$ s, $f_0=\dfrac1{T_0}=2$ Hz."]),
  ("b", 0.5, [r"Mỗi lần xe đi qua một gờ, bánh xe bị nâng lên và truyền cho thân xe một cú đẩy qua hệ treo. Các gờ cách đều nhau nên các cú đẩy lặp lại sau những khoảng thời gian bằng nhau, tức tạo thành một ngoại lực tuần hoàn.", r"Thời gian giữa hai cú đẩy là thời gian xe đi hết $L$: $T=\dfrac Lv$ và $f=\dfrac vL$."]),
  ("c", 0.5, [r"Cộng hưởng xảy ra khi $f=f_0$, tức $\dfrac Lv=T_0$:", ("eq", r"v=\dfrac{L}{T_0}=\dfrac{3{,}0}{0{,}5}=6\text{ m/s}=21{,}6\text{ km/h}"), r"Hiện tượng: cộng hưởng (biên độ dao động cưỡng bức đạt cực đại)."]),
  ("d", 0.5, [r"Giới hạn 20 km/h $\approx5{,}6$ m/s rất gần tốc độ cộng hưởng $6$ m/s: xe chạy đúng giới hạn lại rung mạnh nhất, thiết kế này không hợp lí. Nên chọn $L$ để tốc độ cộng hưởng $v=Lf_0$ khác xa tốc độ cho phép.", r"Với $36$ km/h $=10$ m/s: $f=\dfrac vL=\dfrac{10}{3}\approx3{,}3$ Hz, lệch khỏi $f_0=2$ Hz khá nhiều nên biên độ nhỏ hơn nhiều so với khi $v=6$ m/s.", r"Biện pháp: (1) tăng lực cản của bộ giảm xóc (đường cộng hưởng thấp và tù hơn); (2) thay đổi $L$ hoặc $k$, $m$ để $f_0$ không trùng $f$ ứng với tốc độ cho phép; (3) cho xe qua gờ nhanh để thời gian gần cộng hưởng ngắn, biên độ chưa kịp tăng."]),
 ],
 common=[r"Dùng $L$ làm quãng đường xe đi trong một chu kì dao động riêng; quên đổi m/s sang km/h; cho rằng cộng hưởng xảy ra khi tốc độ càng lớn thì biên độ càng lớn."],
),
# ------------------------------------------------------------------ 3
dict(pts=2, level="DOK2",
 stem=r"Một nhóm học sinh đo chu kì của con lắc đơn có chiều dài $\ell$ thay đổi được bằng cách đo thời gian $t_{10}$ của 10 dao động toàn phần bằng đồng hồ bấm giây (độ phân giải $0{,}1$ s). Biên độ góc ban đầu là $8^\circ$. Kết quả đo được ghi ở Bảng 3, và các điểm $(\ell,T^2)$ đã tính được biểu diễn ở Hình 3. Lấy $\pi=3{,}14$.",
 table=TABLE3, table_caption="Bảng 3",
 fig=("d2_c3.png", 7.0, "Hình 3"),
 parts=[
  (r"Hoàn thành hai cột $T$ và $T^2$ của Bảng 3.", 0.5),
  (r"Từ công thức con lắc đơn dao động nhỏ, dự đoán dạng đồ thị $T^2$ theo $\ell$. Vẽ đường thẳng phù hợp nhất với các điểm ở Hình 3, xác định hệ số góc và tính gia tốc trọng trường $g$.", 0.5),
  (r"Giải thích vì sao nên đo thời gian 10 dao động thay vì 1 dao động. Tính sai số tương đối của $T$ trong hai cách đo với $\ell=0{,}800$ m (coi sai số của mỗi lần bấm là $0{,}1$ s).", 0.5),
  (r"Khi biên độ góc $\alpha_0$ không quá nhỏ, chu kì thực của con lắc là $T\approx T_0\left(1+\dfrac{\alpha_0^2}{16}\right)$ với $T_0=2\pi\sqrt{\ell/g}$ ($\alpha_0$ tính bằng rad). Với $\alpha_0=8^\circ$, giá trị $g$ tính bằng công thức góc nhỏ bị sai lệch bao nhiêu phần trăm so với giá trị thật? Điều này có đáng kể so với sai số ở ý c không?", 0.5),
 ],
 sol=[
  ("a", 0.5, [r"$T=\dfrac{t_{10}}{10}$ và $T^2$ như bảng sau:", ("table", TABLE3_FILLED)]),
  ("b", 0.5, [r"Từ $T=2\pi\sqrt{\dfrac\ell g}$ suy ra $T^2=\dfrac{4\pi^2}{g}\,\ell$: đồ thị $T^2$ theo $\ell$ là đường thẳng đi qua gốc toạ độ với hệ số góc $s=\dfrac{4\pi^2}{g}$.", r"Đường thẳng phù hợp nhất (xem hình đáp án) có hệ số góc $s\approx4{,}0$ s²/m (đọc đồ thị trong khoảng $3{,}95$ đến $4{,}10$). Khi đó:", ("eq", r"g=\dfrac{4\pi^2}{s}=\dfrac{4\cdot3{,}14^2}{4{,}01}\approx9{,}8\ \text{m/s}^2")]),
  ("c", 0.5, [r"Sai số do thời gian phản ứng khi bấm đồng hồ gần như cố định (khoảng $0{,}1$ s) nên chia cho số dao động $N$: sai số của $T$ giảm $N$ lần.", r"Với $\ell=0{,}800$ m: một dao động $T=1{,}80$ s nên $\dfrac{\Delta T}{T}=\dfrac{0{,}1}{1{,}80}\approx5{,}6\%$; mười dao động $t_{10}=18{,}0$ s nên $\dfrac{\Delta T}{T}=\dfrac{0{,}1}{18{,}0}\approx0{,}56\%$. Sai số tương đối của $g$ (do $g\propto T^{-2}$) gấp đôi, khoảng $1{,}1\%$."]),
  ("d", 0.5, [r"$\alpha_0=8^\circ=0{,}1396$ rad nên $1+\dfrac{\alpha_0^2}{16}\approx1{,}0012$: chu kì thực lớn hơn $T_0$ khoảng $0{,}12\%$. Dùng công thức góc nhỏ cho $T$ đo được: $g_{tính}=\dfrac{4\pi^2\ell}{T^2}=\dfrac{g_{thật}}{(1{,}0012)^2}\approx0{,}9976\,g_{thật}$, thấp hơn khoảng $0{,}24\%$ (khoảng $0{,}02$ m/s²).", r"Giá trị này nhỏ hơn nhiều so với sai số $\approx1{,}1\%$ ở ý c, nên xấp xỉ góc nhỏ ở $8^\circ$ là chấp nhận được; tuy nhiên chu kì không phụ thuộc biên độ chỉ đúng gần đúng."]),
 ],
 common=[r"Quên bình phương khi lập $T^2$; vẽ đường thẳng không đi qua gốc nhưng lại dùng công thức $g=4\pi^2/s$; nhầm sai số của 1 dao động với của 10 dao động."],
 ans_figs=[("a_c3.png", 7.0, "Hình đáp án Câu 3: đường thẳng phù hợp nhất của T² theo ℓ")],
),
# ------------------------------------------------------------------ 4
dict(pts=2, level="DOK3",
 stem=r"Một đĩa khối lượng $M=0{,}7$ kg gắn chặt vào đầu trên của một lò xo nhẹ thẳng đứng, độ cứng $k=100$ N/m, đầu dưới cố định; hệ đang đứng yên ở vị trí cân bằng. Từ độ cao $h=0{,}2$ m so với đĩa, một viên bột nhão khối lượng $m=0{,}3$ kg rơi tự do không vận tốc đầu xuống đĩa và dính chặt vào đĩa (va chạm mềm, xảy ra rất nhanh). Chọn trục $Ox$ thẳng đứng hướng xuống, gốc $O$ tại vị trí cân bằng mới của hệ (đĩa và viên bột), gốc thời gian $t=0$ là lúc ngay sau va chạm (Hình 4). Lấy $g=10$ m/s².",
 fig=("d2_c4.png", 4.2, "Hình 4"),
 parts=[
  (r"Tính vận tốc viên bột ngay trước va chạm, vận tốc của hệ ngay sau va chạm và phần cơ năng bị mất trong va chạm.", 0.5),
  (r"Vị trí cân bằng mới dịch xuống bao nhiêu so với vị trí cân bằng cũ? Tìm li độ của hệ lúc $t=0$ và tần số góc của dao động mới.", 0.5),
  (r"Tính biên độ và viết phương trình dao động $x(t)$ (pha ban đầu $\varphi$ thoả $-\pi<\varphi\le\pi$).", 0.5),
  (r"Tính độ nén lớn nhất của lò xo, độ lớn lực đàn hồi cực đại và cơ năng dao động (mốc thế năng tại vị trí cân bằng mới).", 0.5),
 ],
 sol=[
  ("a", 0.5, [r"$v_0=\sqrt{2gh}=\sqrt{2\cdot10\cdot0{,}2}=2$ m/s. Va chạm mềm, động lượng theo phương thẳng đứng bảo toàn (nội lực rất lớn so với các lực khác trong thời gian rất ngắn): $mv_0=(M+m)V$, nên", ("eq", r"V=\dfrac{mv_0}{M+m}=\dfrac{0{,}3\cdot2}{1{,}0}=0{,}6\ \text{m/s}"), r"Cơ năng mất: $\Delta W=\dfrac12mv_0^2-\dfrac12(M+m)V^2=0{,}6-0{,}18=0{,}42$ J (70%, đúng bằng $\dfrac{M}{M+m}$ phần động năng ban đầu)."]),
  ("b", 0.5, [r"Cân bằng cũ: lò xo nén $\dfrac{Mg}{k}=7$ cm; cân bằng mới: nén $\dfrac{(M+m)g}{k}=10$ cm. Vị trí cân bằng mới thấp hơn cũ $\Delta=\dfrac{mg}{k}=3$ cm.", r"Ngay sau va chạm đĩa vẫn ở vị trí cân bằng cũ, tức ở trên $O$ là $3$ cm: $x_0=-3$ cm, $v_0=+60$ cm/s (hướng xuống, cùng chiều $Ox$). $\omega=\sqrt{\dfrac{k}{M+m}}=\sqrt{\dfrac{100}{1{,}0}}=10$ rad/s."]),
  ("c", 0.5, [r"$A=\sqrt{x_0^2+\dfrac{v_0^2}{\omega^2}}=\sqrt{3^2+6^2}=3\sqrt5\approx6{,}71$ cm.", r"$\cos\varphi=\dfrac{x_0}{A}=-\dfrac{1}{\sqrt5}$; vật đang đi theo chiều dương nên $\varphi<0$: $\varphi=-\arccos\left(-\dfrac1{\sqrt5}\right)\approx-2{,}03$ rad.", ("eq", r"x=3\sqrt5\cos\left(10t-2{,}03\right)\ \text{cm}"), r"Kiểm tra: $x(0)=6{,}71\cos(-2{,}03)=-3{,}0$ cm; $v(0)=-10\cdot6{,}71\sin(-2{,}03)=+60$ cm/s."]),
  ("d", 0.5, [r"Độ nén lớn nhất ở biên dưới: $10+6{,}71=16{,}7$ cm. Lực đàn hồi cực đại: $F_{max}=k\cdot0{,}1671\approx16{,}7$ N.", r"Cơ năng dao động: $W=\dfrac12kA^2=\dfrac12\cdot100\cdot(0{,}0671)^2\approx0{,}225$ J. Kiểm tra bằng $\dfrac12(M+m)V^2+\dfrac12kx_0^2=0{,}18+0{,}045=0{,}225$ J."]),
 ],
 common=[r"Lấy vị trí cân bằng cũ làm gốc (bỏ qua dịch chuyển $mg/k$); lấy $\omega=\sqrt{k/M}$; cho rằng va chạm mềm bảo toàn cơ năng."],
),
# ------------------------------------------------------------------ 5
dict(pts=2, level="DOK3",
 stem=r"Vật $M=300$ g được gắn chặt vào lò xo nhẹ có độ cứng $k=200$ N/m. Vật $m=200$ g đặt lên $M$ (không dính). Lấy $g=10$ m/s². Xét hai cách bố trí (Hình 5): (a) lò xo thẳng đứng, đầu dưới cố định; (b) lò xo nằm ngang trên mặt phẳng ngang nhẵn, giữa $m$ và $M$ có hệ số ma sát nghỉ $\mu$. Trong cả hai trường hợp, hệ dao động điều hoà theo phương của lò xo.",
 fig=("d2_c5.png", 10.5, "Hình 5"),
 parts=[
  (r"Cách bố trí (a): tính tần số góc của hệ và độ nén của lò xo ở vị trí cân bằng.", 0.5),
  (r"Cách bố trí (a): lập biểu thức độ lớn lực $N$ do $M$ tác dụng lên $m$ theo li độ $x$ ($Ox$ hướng xuống). Tìm điều kiện của biên độ $A$ để $m$ không rời khỏi $M$.", 0.5),
  (r"Cách bố trí (a) với $A=2{,}0$ cm: tính giá trị lớn nhất và nhỏ nhất của $N$.", 0.5),
  (r"Cách bố trí (b) với biên độ $2{,}0$ cm: tìm giá trị nhỏ nhất của $\mu$ để $m$ không trượt trên $M$.", 0.5),
 ],
 sol=[
  ("a", 0.5, [r"$m$ và $M$ cùng dao động nên $\omega=\sqrt{\dfrac{k}{M+m}}=\sqrt{\dfrac{200}{0{,}5}}=20$ rad/s. Ở vị trí cân bằng, lò xo nén $\Delta\ell=\dfrac{(M+m)g}{k}=\dfrac{0{,}5\cdot10}{200}=2{,}5$ cm."]),
  ("b", 0.5, [r"Với $Ox$ hướng xuống, gia tốc của $m$ là $a=-\omega^2x$. Định luật II Newton cho $m$ (trọng lực xuống, phản lực $N$ lên): $mg-N=ma$, nên", ("eq", r"N=m(g-a)=m(g+\omega^2x)"), r"$m$ không rời $M$ khi $N\ge0$ với mọi $x\in[-A;A]$. Nhỏ nhất ở $x=-A$ (điểm cao nhất): $g-\omega^2A\ge0$, suy ra", ("eq", r"A\le\dfrac{g}{\omega^2}=\dfrac{10}{400}=2{,}5\ \text{cm}")]),
  ("c", 0.5, [r"$N_{max}=m(g+\omega^2A)=0{,}2\,(10+400\cdot0{,}02)=3{,}6$ N (ở điểm thấp nhất, $x=+A$). $N_{min}=m(g-\omega^2A)=0{,}2\,(10-8)=0{,}4$ N (ở điểm cao nhất)."]),
  ("d", 0.5, [r"Gia tốc cực đại của hệ: $a_{max}=\omega^2A=400\cdot0{,}02=8$ m/s² ($\omega$ vẫn bằng $20$ rad/s vì cùng $k$ và cùng tổng khối lượng). Chỉ lực ma sát nghỉ truyền gia tốc này cho $m$: $\mu mg\ge ma_{max}$, nên", ("eq", r"\mu\ge\dfrac{a_{max}}{g}=\dfrac{8}{10}=0{,}8")]),
 ],
 common=[r"Chọn chiều dương hướng lên rồi vẫn dùng $N=m(g+\omega^2x)$; dùng $\omega=\sqrt{k/M}$ thay cho $\sqrt{k/(M+m)}$; quên rằng ma sát nghỉ là lực duy nhất làm $m$ dao động ở cách bố trí (b)."],
),
# ------------------------------------------------------------------ 6
dict(pts=3, level="DOK3",
 stem=r"Con lắc lò xo nằm ngang gồm vật nhỏ khối lượng $m=200$ g gắn với lò xo nhẹ có độ cứng $k=20$ N/m. Hệ số ma sát giữa vật và mặt phẳng ngang là $\mu=0{,}1$ (coi ma sát nghỉ cực đại bằng ma sát trượt). Lấy $g=10$ m/s². Kéo vật khỏi vị trí $O$ lúc lò xo không biến dạng một đoạn $A_0=9$ cm rồi thả nhẹ (Hình 6). Chọn trục $Ox$ theo chiều kéo ban đầu, gốc $O$.",
 fig=("d2_c6.png", 10.0, "Hình 6"),
 parts=[
  (r"Tính độ lệch $x_0=\dfrac{\mu mg}{k}$ của vị trí cân bằng tạm thời so với $O$. Chứng minh trong nửa chu kì đầu vật dao động điều hoà quanh điểm đó, tính tốc độ lớn nhất của vật và vị trí đạt tốc độ ấy.", 0.5),
  (r"Chứng minh biên độ (so với $O$) tại cuối các nửa chu kì liên tiếp giảm đều: $A_n=A_0-2nx_0$. Nêu điều kiện để vật dừng hẳn.", 0.75),
  (r"Vật dừng hẳn ở vị trí nào, sau bao lâu, đã đi qua $O$ mấy lần? Tính tổng quãng đường vật đi được bằng hai cách.", 1.0),
  (r"Giữ nguyên $m$, $k$, $A_0=9$ cm. Tìm khoảng giá trị của $\mu$ để vật chỉ thực hiện đúng một nửa chu kì rồi dừng lại.", 0.75),
 ],
 sol=[
  ("a", 0.5, [r"$x_0=\dfrac{\mu mg}{k}=\dfrac{0{,}1\cdot0{,}2\cdot10}{20}=0{,}01$ m $=1$ cm. Khi vật đi theo chiều âm (từ $x=+9$ cm về phía $O$), lực ma sát hướng chiều dương, có độ lớn $F_{ms}=\mu mg$. Phương trình chuyển động $mx''=-kx+F_{ms}=-k(x-x_0)$. Đặt $u=x-x_0$ thì $u''=-\dfrac km u$, đây là dao động điều hoà quanh $x=+x_0$ với $\omega=\sqrt{\dfrac km}=10$ rad/s, biên độ $A_0-x_0=8$ cm.", r"Tốc độ lớn nhất khi qua $x=+x_0=+1$ cm: $v_{max}=\omega(A_0-x_0)=10\cdot8=80$ cm/s $=0{,}8$ m/s."]),
  ("b", 0.75, [r"Nửa chu kì đầu: dao động quanh $+x_0$ với biên độ $A_0-x_0$ nên đến vị trí $x_1=x_0-(A_0-x_0)=-(A_0-2x_0)$; biên độ so với $O$ là $A_1=A_0-2x_0$. Sang nửa chu kì thứ hai, lực ma sát đổi chiều nên vật dao động quanh $-x_0$ với biên độ $A_1-x_0$, đến $x_2=+(A_1-2x_0)$. Quy nạp:", ("eq", r"A_n=A_0-2nx_0"), r"Giảm đều $2x_0=2$ cm sau mỗi nửa chu kì (cấp số cộng, không phải cấp số nhân như tắt dần nhớt).", r"Vật dừng hẳn khi tại biên lực đàn hồi không thắng được ma sát nghỉ: $kA_n\le\mu mg$, tức $A_n\le x_0$."]),
  ("c", 1.0, [r"Dãy biên độ ở các điểm dừng tạm thời: $9\to7\to5\to3\to1$ cm. Tại $A_4=1$ cm $=x_0$: $kA_4=0{,}2$ N $=\mu mg$ nên vật dừng hẳn. Số nửa chu kì: $4$. Vị trí dừng: $x=+1$ cm (dấu cộng vì các biên liên tiếp có li độ $+9$, $-7$, $+5$, $-3$, $+1$ cm).", r"Thời gian: $t=4\cdot\dfrac T2=2T=2\cdot\dfrac{2\pi}{10}=0{,}4\pi\approx1{,}26$ s. Mỗi nửa chu kì vật đều đi qua $O$ một lần nên qua $O$ đúng $4$ lần.", r"Quãng đường cách 1 (cộng từng đoạn): $16+12+8+4=40$ cm. Cách 2 (công của ma sát): $\dfrac12kA_0^2-\dfrac12kx_f^2=\mu mg\,S$, nên $S=\dfrac{\frac12\cdot20\,(0{,}09^2-0{,}01^2)}{0{,}2}=\dfrac{0{,}08}{0{,}2}=0{,}4$ m $=40$ cm."]),
  ("d", 0.75, [r"Vật chỉ bắt đầu chuyển động khi $kA_0>\mu mg$, tức $x_0<A_0$. Sau nửa chu kì đầu vật đến điểm có $|x_1|=|A_0-2x_0|$ và phải dừng ngay ở đó: $|A_0-2x_0|\le x_0$, tức $x_0\le A_0\le3x_0$. Kết hợp: $\dfrac{A_0}{3}\le x_0<A_0$, hay $3\text{ cm}\le x_0<9\text{ cm}$.", r"Vì $\mu=\dfrac{kx_0}{mg}=10\,x_0$ (với $x_0$ tính bằng mét) nên", ("eq", r"0{,}3\le\mu<0{,}9")]),
 ],
 common=[r"Dùng công thức tắt dần nhớt (nhân với hệ số $e^{-\alpha T}$) cho ma sát trượt; quên rằng vị trí cân bằng tạm thời đổi bên sau mỗi nửa chu kì; tính số lần qua $O$ bằng số chu kì thay vì số nửa chu kì."],
 ans_figs=[("a_c6.png", 9.0, "Hình đáp án Câu 6: li độ theo thời gian (biên độ giảm đều 2 cm mỗi nửa chu kì)")],
),
# ------------------------------------------------------------------ 7
dict(pts=2, level="DOK3",
 stem=r"Một ống chữ U tiết diện đều $S=1{,}0$ cm² chứa chất lỏng không nhớt, khối lượng riêng $\rho=1000$ kg/m³; tổng chiều dài cột chất lỏng (đo dọc theo ống) là $\ell=80$ cm. Ban đầu chất lỏng đứng yên, mực hai nhánh ngang nhau (đường nét đứt $O$). Làm mực chất lỏng ở nhánh trái dâng cao hơn $O$ một đoạn $y$ (nhánh phải thấp hơn $O$ đoạn $y$) rồi buông ra (Hình 7). Bỏ qua ma sát, sức căng bề mặt và áp suất khí quyển không đổi. Lấy $g=10$ m/s².",
 fig=("d2_c7.png", 4.0, "Hình 7"),
 parts=[
  (r"Lập phương trình chuyển động của $y$ (bằng định luật II Newton cho toàn bộ cột chất lỏng hoặc bằng bảo toàn cơ năng). Chứng minh chất lỏng dao động điều hoà, tìm $\omega$ và $T$. Chu kì có phụ thuộc $\rho$ và $S$ không?", 0.75),
  (r"Lúc $t=0$ mực nhánh trái ở $y=+3$ cm và đang đi xuống với tốc độ $20$ cm/s. Viết phương trình $y(t)$ (chiều dương hướng lên).", 0.5),
  (r"Tính tốc độ lớn nhất của chất lỏng và cơ năng dao động. Chỉ ra độ cứng tương đương $k_{eq}$ và khối lượng tương đương của hệ lò xo - vật có cùng dao động.", 0.5),
  (r"Thay chất lỏng bằng thuỷ ngân ($\rho\approx13600$ kg/m³) với cùng chiều dài cột chất lỏng. Chu kì thay đổi thế nào? Giải thích.", 0.25),
 ],
 sol=[
  ("a", 0.75, [r"Khối lượng cả cột chất lỏng $m=\rho S\ell$. Khi mực nhánh trái cao hơn $O$ đoạn $y$ thì hai mực chênh nhau $2y$. Hợp lực kéo cột chất lỏng về vị trí cân bằng bằng trọng lượng của cột chất lỏng có chiều cao $2y$ tiết diện $S$: $F=-\rho gS\cdot2y$. Định luật II Newton (chuyển động của cả cột):", ("eq", r"\rho S\ell\,y''=-2\rho gS\,y\;\Rightarrow\;y''=-\dfrac{2g}{\ell}\,y"), r"Đây là phương trình $y''=-\omega^2y$ nên chất lỏng dao động điều hoà với", ("eq", r"\omega=\sqrt{\dfrac{2g}{\ell}}=\sqrt{\dfrac{20}{0{,}8}}=5\ \text{rad/s},\qquad T=\dfrac{2\pi}{5}\approx1{,}26\ \text{s}"), r"(Bằng năng lượng: $W=\dfrac12\rho S\ell\,y'^2+\rho gS\,y^2$; $W$ không đổi nên $\dfrac{dW}{dt}=0$ cho cùng kết quả.) $\rho$ và $S$ triệt tiêu nên $T$ không phụ thuộc $\rho$, $S$; chỉ phụ thuộc $\ell$ và $g$."]),
  ("b", 0.5, [r"$A=\sqrt{y_0^2+\dfrac{v_0^2}{\omega^2}}=\sqrt{3^2+4^2}=5$ cm. $\cos\varphi=\dfrac35$; vật đang đi xuống ($v_0<0$) nên $\varphi>0$: $\varphi=\arccos0{,}6\approx0{,}927$ rad.", ("eq", r"y=5\cos\left(5t+0{,}927\right)\ \text{cm}")]),
  ("c", 0.5, [r"$v_{max}=\omega A=5\cdot5=25$ cm/s $=0{,}25$ m/s. Khối lượng cột chất lỏng $m=\rho S\ell=1000\cdot10^{-4}\cdot0{,}8=0{,}08$ kg. Cơ năng $W=\dfrac12mv_{max}^2=\dfrac12\cdot0{,}08\cdot0{,}25^2=2{,}5$ mJ (kiểm tra: $\rho gSA^2=1000\cdot10\cdot10^{-4}\cdot0{,}05^2=2{,}5$ mJ).", r"Hệ lò xo - vật tương đương: $k_{eq}=2\rho gS=2$ N/m, khối lượng $m=0{,}08$ kg, vì $\omega=\sqrt{\dfrac{k_{eq}}{m}}=\sqrt{\dfrac{2}{0{,}08}}=5$ rad/s."]),
  ("d", 0.25, [r"Chu kì không đổi: khi thay $\rho$, cả khối lượng $m=\rho S\ell$ lẫn độ cứng tương đương $k_{eq}=2\rho gS$ cùng tăng $\dfrac{13600}{1000}$ lần nên tỉ số $\dfrac{k_{eq}}{m}=\dfrac{2g}{\ell}$ không đổi."]),
 ],
 common=[r"Dùng chiều cao $y$ thay cho $2y$ trong lực kéo về; lấy $\ell$ là chiều dài một nhánh thay vì tổng chiều dài cột chất lỏng; cho rằng chu kì phụ thuộc loại chất lỏng."],
),
# ------------------------------------------------------------------ 8
dict(pts=2, level="DOK3",
 stem=r"Một con lắc đơn gồm vật nhỏ khối lượng $m=200$ g treo vào sợi dây nhẹ, không dãn, dài $\ell=1{,}25$ m. Lấy $g=10$ m/s² và $\pi^2=10$.",
 fig=("d2_c8.png", 10.0, "Hình 8"),
 parts=[
  (r"Con lắc treo trong một toa xe đang tăng tốc đều trên đường nằm ngang với gia tốc $a=7{,}5$ m/s² (Hình 8a). Ở trạng thái cân bằng tương đối so với xe, dây lệch khỏi phương thẳng đứng góc $\beta$. Tìm $\beta$, trọng lực hiệu dụng (gia tốc trọng trường hiệu dụng $g'$) và chu kì $T'$ của dao động nhỏ so với xe.", 0.75),
  (r"Kéo con lắc lệch thêm một góc nhỏ $\alpha_0=0{,}08$ rad so với vị trí cân bằng tương đối rồi thả nhẹ. Tính tốc độ cực đại (so với xe) và cơ năng của dao động (mốc thế năng tại vị trí cân bằng tương đối, trong hệ quy chiếu gắn với xe).", 0.75),
  (r"Đưa con lắc vào thang máy đang đi lên nhanh dần đều với gia tốc $2{,}5$ m/s² (Hình 8b). Tính chu kì dao động nhỏ và so sánh với $T'$. Viết công thức tổng quát của chu kì dao động nhỏ khi điểm treo chuyển động với gia tốc $\vec a$, và giải thích vì sao hai kết quả bằng nhau.", 0.5),
 ],
 sol=[
  ("a", 0.75, [r"Trong hệ quy chiếu gắn với xe, ngoài trọng lực $m\vec g$ còn có lực quán tính $-m\vec a$. Trọng lực hiệu dụng $m\vec g'$ với $\vec g'=\vec g-\vec a$ ($\vec a\perp\vec g$):", ("eq", r"g'=\sqrt{g^2+a^2}=\sqrt{10^2+7{,}5^2}=12{,}5\ \text{m/s}^2,\qquad\tan\beta=\dfrac ag=0{,}75\Rightarrow\beta\approx36{,}9^\circ"), r"Dao động nhỏ quanh vị trí cân bằng tương đối giống con lắc đơn trong trường hiệu dụng $g'$:", ("eq", r"T'=2\pi\sqrt{\dfrac{\ell}{g'}}=2\pi\sqrt{\dfrac{1{,}25}{12{,}5}}=\dfrac{2\pi}{\sqrt{10}}=2\ \text{s}\quad(\pi^2=10)")]),
  ("b", 0.75, [r"$\omega'=\sqrt{\dfrac{g'}{\ell}}=\sqrt{10}$ rad/s; biên độ cung $S_0=\ell\alpha_0=1{,}25\cdot0{,}08=0{,}1$ m. Tốc độ cực đại:", ("eq", r"v_{max}=\omega'S_0=\sqrt{10}\cdot0{,}1\approx0{,}316\ \text{m/s}"), r"Cơ năng: $W=\dfrac12mv_{max}^2=\dfrac12\cdot0{,}2\cdot0{,}1=0{,}01$ J $=10$ mJ (kiểm tra bằng $\dfrac12mg'\ell\alpha_0^2=\dfrac12\cdot0{,}2\cdot12{,}5\cdot1{,}25\cdot0{,}0064=10$ mJ)."]),
  ("c", 0.5, [r"Thang máy đi lên nhanh dần: $\vec a$ hướng lên nên $\vec g'=\vec g-\vec a$ hướng xuống với độ lớn $g'=g+a=12{,}5$ m/s². Do đó", ("eq", r"T''=2\pi\sqrt{\dfrac{\ell}{12{,}5}}=2\ \text{s}=T'"), r"Công thức tổng quát: $T=2\pi\sqrt{\dfrac{\ell}{|\vec g-\vec a|}}$. Ở (a), $|\vec g-\vec a|=\sqrt{g^2+a^2}=12{,}5$; ở (b), $|\vec g-\vec a|=g+a=12{,}5$. Hai trường hợp khác hướng nhưng cùng độ lớn của trọng lực hiệu dụng nên chu kì bằng nhau: chu kì chỉ phụ thuộc độ lớn $g'$, không phụ thuộc hướng hay khối lượng."]),
 ],
 common=[r"Dùng $g'=g+a$ cho trường hợp xe tăng tốc ngang (cộng đại số thay vì cộng véctơ); tính góc $\beta$ bằng $\tan\beta=g/a$; cho rằng biên độ góc đo từ phương thẳng đứng."],
),
# ------------------------------------------------------------------ 9
dict(pts=3, level="DOK3",
 stem=r"Mô hình đơn giản của hệ treo ô tô: thân xe là chất điểm khối lượng $m=400$ kg nối với bánh xe bằng lò xo nhẹ độ cứng $k=1{,}6\cdot10^5$ N/m và bộ giảm chấn gây lực nhớt $-\lambda\vec v$ với $\lambda=400$ kg/s (Hình 9). Xe chạy với tốc độ $v$ trên mặt đường lượn sóng có chu kì không gian $L=5{,}0$ m. Mô hình coi như bánh xe tác dụng lên thân xe một lực cưỡng bức $F=F_0\cos\omega t$ với $F_0=800$ N, tần số góc $\omega=\dfrac{2\pi v}{L}$.",
 given=r"**Cho biết.** Đặt $\alpha=\dfrac{\lambda}{2m}$ và $\omega_0=\sqrt{\dfrac km}$. Dao động tắt dần tự do có dạng $z=Ae^{-\alpha t}\cos(\Omega t+\varphi)$ với $\Omega=\sqrt{\omega_0^2-\alpha^2}$. Dao động cưỡng bức ổn định có dạng $z=B\cos(\omega t+\delta)$ với biên độ $B=\dfrac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\alpha^2\omega^2}}$; tại $\omega=\omega_0$ thì $\delta=-\dfrac\pi2$.",
 fig=("d2_c9.png", 9.0, "Hình 9"),
 parts=[
  (r"Tính $\alpha$, $\omega_0$, $\Omega$ và chu kì $T=\dfrac{2\pi}{\Omega}$ của dao động tắt dần tự do. Sau mỗi chu kì biên độ giảm bao nhiêu phần trăm?", 0.5),
  (r"Tìm tốc độ $v$ của xe (m/s và km/h) để xảy ra cộng hưởng ($\omega=\omega_0$) và tính biên độ $B_{max}$ của dao động cưỡng bức khi đó.", 0.75),
  (r"Xe chạy $36$ km/h: tính biên độ $B$ và so sánh với $B_{max}$ và với độ dịch tĩnh $B_{st}=\dfrac{F_0}{k}$. Tính hệ số phẩm chất $Q=\dfrac{\omega_0}{2\alpha}$ và chứng tỏ $\dfrac{B_{max}}{B_{st}}=Q$.", 0.75),
  (r"Khi cộng hưởng, tính công suất trung bình mà lực cưỡng bức cung cấp cho hệ và công suất tiêu hao bởi lực nhớt. Chúng có bằng nhau không? Giải thích.", 0.5),
  (r"Với $k$ và $m$ không đổi, tìm hệ số nhớt $\lambda_c$ để bộ giảm chấn ở chế độ tắt dần tới hạn ($\Omega=0$) và so sánh với $\lambda$ đã cho. Vì sao nhà thiết kế không chọn giảm chấn quá lớn?", 0.5),
 ],
 sol=[
  ("a", 0.5, [r"$\alpha=\dfrac{\lambda}{2m}=\dfrac{400}{800}=0{,}5$ s⁻¹; $\omega_0=\sqrt{\dfrac{1{,}6\cdot10^5}{400}}=20$ rad/s; $\Omega=\sqrt{400-0{,}25}\approx19{,}99$ rad/s; $T=\dfrac{2\pi}{\Omega}\approx0{,}314$ s.", r"Sau một chu kì biên độ nhân với $e^{-\alpha T}=e^{-0{,}157}\approx0{,}855$: giảm khoảng $14{,}5\%$."]),
  ("b", 0.75, [r"Lực cưỡng bức có tần số góc $\omega=\dfrac{2\pi v}{L}$. Cộng hưởng ($\omega=\omega_0$):", ("eq", r"v=\dfrac{\omega_0L}{2\pi}=\dfrac{20\cdot5{,}0}{2\pi}\approx15{,}9\ \text{m/s}\approx57\ \text{km/h}"), r"Biên độ khi đó: $B_{max}=\dfrac{F_0/m}{2\alpha\omega_0}=\dfrac{800/400}{2\cdot0{,}5\cdot20}=0{,}10$ m $=10$ cm."]),
  ("c", 0.75, [r"$v=36$ km/h $=10$ m/s nên $\omega=\dfrac{2\pi\cdot10}{5}=4\pi\approx12{,}57$ rad/s, $\omega^2\approx157{,}9$. Khi đó", ("eq", r"B=\dfrac{2}{\sqrt{(400-157{,}9)^2+4\cdot0{,}25\cdot157{,}9}}=\dfrac{2}{242{,}4}\approx8{,}3\cdot10^{-3}\ \text{m}\approx0{,}83\ \text{cm}"), r"$\dfrac{B_{max}}{B}\approx12$: biên độ nhỏ hơn khoảng 12 lần. Độ dịch tĩnh $B_{st}=\dfrac{800}{1{,}6\cdot10^5}=5$ mm $=0{,}5$ cm.", r"$Q=\dfrac{\omega_0}{2\alpha}=\dfrac{20}{2\cdot0{,}5}=20$ và $\dfrac{B_{max}}{B_{st}}=\dfrac{10}{0{,}5}=20=Q$ (suy từ $B_{max}=\dfrac{F_0}{2m\alpha\omega_0}=\dfrac{F_0}{k}\cdot\dfrac{\omega_0}{2\alpha}$ vì $m\omega_0^2=k$)."]),
  ("d", 0.5, [r"Khi cộng hưởng $\delta=-\dfrac\pi2$ (dao động trễ pha $\dfrac\pi2$ so với lực), nên vận tốc cùng pha với lực. Công suất trung bình của lực cưỡng bức: $P_F=\dfrac12F_0\,\omega_0B_{max}=\dfrac12\cdot800\cdot20\cdot0{,}1=800$ W.", r"Công suất tiêu hao do lực nhớt: $P_c=\dfrac12\lambda\omega_0^2B_{max}^2=\dfrac12\cdot400\cdot400\cdot0{,}01=800$ W.", r"Hai giá trị bằng nhau ($=\dfrac{F_0^2}{2\lambda}$): ở trạng thái ổn định cơ năng của hệ không đổi nên năng lượng nạp vào mỗi chu kì đúng bằng năng lượng bị lực nhớt lấy đi."]),
  ("e", 0.5, [r"Tắt dần tới hạn khi $\Omega=0$, tức $\alpha=\omega_0$:", ("eq", r"\lambda_c=2m\omega_0=2\cdot400\cdot20=1{,}6\cdot10^4\ \text{kg/s}=40\lambda"), r"Giảm chấn quá lớn làm hệ gần như “cứng”: lực nhớt $\lambda v$ lớn truyền xung lực mạnh lên thân xe khi bánh xe đi qua mấp mô, xe xóc và mất êm ái. Do đó thường chọn $\dfrac{\alpha}{\omega_0}$ trong khoảng $0{,}3$ đến $0{,}7$ để vừa dập tắt dao động nhanh vừa êm."]),
 ],
 common=[r"Lấy $\Omega=\omega_0$ làm cộng hưởng khi tính biên độ nhưng quên $2\alpha\omega$ trong mẫu số; tính công suất bằng $F_0\omega B$ (thiếu hệ số $\frac12$ của giá trị trung bình); nhầm $\alpha=\lambda/m$."],
 ans_figs=[("a_c9.png", 9.0, "Hình đáp án Câu 9: biên độ cưỡng bức theo tần số góc (thang logarit)")],
),
]
