# -*- coding: utf-8 -*-
"""Noi dung De 1: 20 cau trac nghiem + 4 cau tu luan. opts[0] la dap an dung."""

LETTERS = "BDACACBDACDBACBDACBD"   # dap an dung cua tung cau (5 moi chu cai)

MCQ = [
# ---------------- Muc 1: nhan biet ----------------
dict(
 q=r"Một vật thực hiện 120 dao động toàn phần trong 1 phút. Chu kì $T$ và tần số $f$ của dao động lần lượt là",
 opts=[r"0,5 s; 2 Hz", r"2 s; 0,5 Hz", r"0,5 s; $4\pi$ Hz", r"2 s; 120 Hz"],
 sol=[r"Chu kì là thời gian thực hiện một dao động toàn phần: $T=\dfrac{\Delta t}{N}=\dfrac{60}{120}=0{,}5$ s. Tần số $f=\dfrac1T=2$ Hz."],
 wrong=[r"B: đảo ngược $T$ và $f$.", r"C: nhầm tần số góc $\omega=4\pi$ rad/s với tần số $f$.", r"D: lấy số dao động trong 1 phút làm tần số."],
),
dict(
 q=r"Một vật dao động điều hoà. Trong một chu kì, vật đi được quãng đường 28 cm. Chiều dài quỹ đạo và biên độ dao động lần lượt là",
 opts=[r"14 cm; 7 cm", r"28 cm; 14 cm", r"7 cm; 14 cm", r"14 cm; 28 cm"],
 sol=[r"Quãng đường trong một chu kì là $S=4A$, nên $A=S/4=7$ cm. Chiều dài quỹ đạo $L=2A=14$ cm."],
 wrong=[r"B: coi quãng đường một chu kì bằng chiều dài quỹ đạo ($L=S$).", r"C: đổi vai trò của biên độ và chiều dài quỹ đạo.", r"D: lấy $A=S$."],
),
dict(
 q=r"Khi vật dao động điều hoà đi qua vị trí cân bằng thì",
 opts=[r"độ lớn vận tốc cực đại, gia tốc bằng 0.", r"độ lớn vận tốc cực đại, độ lớn gia tốc cực đại.", r"vận tốc bằng 0, gia tốc bằng 0.", r"vận tốc bằng 0, độ lớn gia tốc cực đại."],
 sol=[r"Tại vị trí cân bằng $x=0$ nên $a=-\omega^2x=0$ và $|v|=\omega\sqrt{A^2-x^2}=\omega A$ là cực đại."],
 wrong=[r"B, D: nhầm vị trí cân bằng với vị trí biên (nơi $|a|=\omega^2A$ cực đại).", r"C: $v$ và $a$ không thể cùng bằng 0 tại vị trí cân bằng; chỉ $a=0$."],
),
dict(
 q=r"Con lắc lò xo dao động điều hoà. Khi vật chuyển động từ vị trí biên về vị trí cân bằng thì",
 opts=[r"động năng tăng, thế năng giảm, cơ năng không đổi.", r"động năng giảm, thế năng tăng, cơ năng không đổi.", r"động năng và thế năng cùng tăng.", r"cơ năng tăng dần."],
 sol=[r"Từ biên về vị trí cân bằng, vật nhanh dần nên $W_đ$ tăng; $|x|$ giảm nên $W_t=\frac12kx^2$ giảm; không có ma sát nên $W=W_đ+W_t$ không đổi."],
 wrong=[r"B: đúng với chiều ngược lại (từ VTCB ra biên).", r"C: vi phạm bảo toàn cơ năng.", r"D: cơ năng của dao động điều hoà là hằng số."],
),
dict(
 q=r"Biên độ của dao động cưỡng bức đạt giá trị cực đại khi",
 opts=[r"tần số của lực cưỡng bức bằng tần số riêng của hệ.", r"độ lớn của lực cưỡng bức đạt cực đại.", r"môi trường hoàn toàn không có lực cản.", r"biên độ của lực cưỡng bức rất lớn."],
 sol=[r"Hiện tượng cộng hưởng: biên độ dao động cưỡng bức cực đại khi $f=f_0$. Lực cưỡng bức có thể rất nhỏ; chỉ cần đúng nhịp."],
 wrong=[r"B, D: cộng hưởng không đòi hỏi lực lớn.", r"C: không có lực cản thì biên độ tăng mãi (đây là mô hình lí tưởng, không phải điều kiện cộng hưởng)."],
),
# ---------------- Muc 2: thong hieu ----------------
dict(
 q=r"Một vật dao động theo phương trình $x=-4\sin\left(5\pi t+\dfrac{\pi}{3}\right)$ cm ($t$ đo bằng giây). Biên độ $A>0$ và pha ban đầu $\varphi$ ($-\pi<\varphi\le\pi$) lần lượt là",
 opts=[r"4 cm; $5\pi/6$ rad", r"$-4$ cm; $\pi/3$ rad", r"4 cm; $-\pi/6$ rad", r"4 cm; $-5\pi/6$ rad"], layout='2x2',
 sol=[r"Dùng $-\sin\alpha=\cos\left(\alpha+\frac{\pi}{2}\right)$: $x=4\cos\left(5\pi t+\frac{\pi}{3}+\frac{\pi}{2}\right)=4\cos\left(5\pi t+\frac{5\pi}{6}\right)$ cm. Vậy $A=4$ cm, $\varphi=\frac{5\pi}{6}$ rad."],
 wrong=[r"B: để biên độ âm và không đổi dạng sin sang cos.", r"C: bỏ dấu trừ, chỉ đổi $\sin\alpha=\cos(\alpha-\frac\pi2)$.", r"D: sai dấu của pha sau khi đổi."],
),
dict(
 q=r"Hình 1 là đồ thị li độ theo thời gian của hai dao động điều hoà (1) và (2) cùng phương, cùng chu kì. Chu kì và độ lệch pha giữa hai dao động là",
 fig=("d1_q7.png", 6.9, "Hình 1"),
 opts=[r"1,2 s; dao động (1) sớm pha hơn dao động (2) góc $\pi/2$.", r"1,2 s; dao động (1) trễ pha hơn dao động (2) góc $\pi/2$.", r"0,6 s; hai dao động ngược pha.", r"1,2 s; hai dao động ngược pha."],
 sol=[r"Hai đỉnh liên tiếp của (1) ở $t=0{,}1$ s và $t=1{,}3$ s nên $T=1{,}2$ s. Đỉnh của (1) xuất hiện trước đỉnh của (2) (ở $t=0{,}4$ s) một khoảng $\Delta t=0{,}3$ s, nên (1) sớm pha hơn (2): $\Delta\varphi=\dfrac{2\pi}{T}\Delta t=\dfrac{2\pi}{1{,}2}\cdot0{,}3=\dfrac{\pi}{2}$."],
 wrong=[r"B: nhầm thứ tự sớm/trễ (dao động tới đỉnh trước thì sớm pha).", r"C: đọc khoảng cách hai đỉnh sai thành 0,6 s.", r"D: ngược pha cần $\Delta t=T/2=0{,}6$ s, ở đây chỉ là $0{,}3$ s."],
),
dict(
 q=r"Một vật dao động điều hoà với tần số góc 10 rad/s. Tại thời điểm vật có li độ 4 cm thì tốc độ của vật là 30 cm/s. Tại thời điểm vật có li độ 3 cm thì tốc độ của vật là",
 opts=[r"40 cm/s", r"50 cm/s", r"30 cm/s", r"$10\sqrt{34}$ cm/s"],
 sol=[r"$A=\sqrt{x^2+\dfrac{v^2}{\omega^2}}=\sqrt{4^2+3^2}=5$ cm. Tại $x=3$ cm: $|v|=\omega\sqrt{A^2-x^2}=10\sqrt{25-9}=40$ cm/s."],
 wrong=[r"B: lấy $v_{max}=\omega A=50$ cm/s.", r"C: cho rằng tốc độ không đổi.", r"D: dùng nhầm $\sqrt{A^2+x^2}$ thay cho $\sqrt{A^2-x^2}$."],
),
dict(
 q=r"Con lắc lò xo có vật nhỏ khối lượng 0,1 kg dao động điều hoà với tần số góc 10 rad/s, biên độ 6 cm. Tại vị trí động năng bằng 3 lần thế năng, độ lớn vận tốc và động năng của vật lần lượt là",
 opts=[r"$30\sqrt3$ cm/s; 13,5 mJ", r"$30\sqrt3$ cm/s; 4,5 mJ", r"30 cm/s; 13,5 mJ", r"60 cm/s; 18 mJ"],
 sol=[r"$W=\frac12m\omega^2A^2=\frac12\cdot0{,}1\cdot100\cdot0{,}06^2=18$ mJ. $W_đ=3W_t$ nên $W=4W_t$, $x=\pm A/2=\pm3$ cm. Khi đó $W_đ=\frac34W=13{,}5$ mJ và $|v|=\omega\sqrt{A^2-x^2}=10\sqrt{36-9}=30\sqrt3$ cm/s."],
 wrong=[r"B: 4,5 mJ là thế năng, không phải động năng.", r"C: vận tốc sai (lấy $v_{max}/2$).", r"D: giá trị cực đại tại VTCB, không phải tại $W_đ=3W_t$."],
),
dict(
 q=r"Một con lắc lò xo treo thẳng đứng, ở vị trí cân bằng lò xo dãn 2,5 cm. Kéo vật xuống dưới vị trí cân bằng 3 cm rồi thả nhẹ cho dao động điều hoà. Lấy $g=10$ m/s². Tốc độ cực đại của vật là",
 opts=[r"60 cm/s", r"110 cm/s", r"30 cm/s", r"6 cm/s"],
 sol=[r"$\omega=\sqrt{\dfrac{g}{\Delta\ell_0}}=\sqrt{\dfrac{10}{0{,}025}}=20$ rad/s. Thả nhẹ nên $A=3$ cm. $v_{max}=\omega A=20\cdot3=60$ cm/s."],
 wrong=[r"B: lấy nhầm $A=\Delta\ell_0+3=5{,}5$ cm.", r"C: dùng $\omega=10$ rad/s (sai $\Delta\ell_0$).", r"D: quên đổi $\Delta\ell_0$ sang mét: $\omega=\sqrt{10/2{,}5}=2$ rad/s."],
),
# ---------------- Muc 3: van dung, lien chu de ----------------
dict(
 q=r"Một vật dao động điều hoà với chu kì 0,6 s và biên độ 8 cm. Tại $t=0$ vật ở biên dương. Thời điểm vật qua vị trí $x=-4\sqrt3$ cm lần thứ ba là",
 opts=[r"0,85 s", r"0,25 s", r"0,35 s", r"0,95 s"],
 sol=[r"$\omega=\dfrac{2\pi}{0{,}6}=\dfrac{10\pi}{3}$ rad/s. $\cos\alpha=\dfrac{-4\sqrt3}{8}=-\dfrac{\sqrt3}{2}$ nên $\alpha=\dfrac{5\pi}{6}$ hoặc $\dfrac{7\pi}{6}$ (mod $2\pi$). Từ pha 0, các lần qua lần lượt ứng với góc $\dfrac{5\pi}{6},\dfrac{7\pi}{6},\dfrac{5\pi}{6}+2\pi,\dots$. Lần thứ ba: $\Delta\alpha=\dfrac{17\pi}{6}$, nên $t=\dfrac{\Delta\alpha}{\omega}=\dfrac{17\pi/6}{10\pi/3}=0{,}85$ s."],
 wrong=[r"B: 0,25 s là lần thứ nhất.", r"C: 0,35 s là lần thứ hai.", r"D: 0,95 s là lần thứ tư."],
),
dict(
 q=r"Hình 2 là đồ thị gia tốc theo li độ của một vật nhỏ khối lượng 0,1 kg dao động điều hoà. Cơ năng của dao động là",
 fig=("d1_q12.png", 5.2, "Hình 2"),
 opts=[r"50 mJ", r"100 mJ", r"25 mJ", r"0,5 mJ"],
 sol=[r"Đồ thị là đoạn thẳng $a=-\omega^2x$, đầu mút $(\pm5\text{ cm};\mp20\text{ m/s}^2)$ nên $A=0{,}05$ m và $\omega^2=\dfrac{20}{0{,}05}=400$ s⁻². $W=\frac12m\omega^2A^2=\frac12\cdot0{,}1\cdot400\cdot0{,}05^2=0{,}05$ J $=50$ mJ."],
 wrong=[r"B: quên hệ số $\frac12$.", r"C: tính $W=\frac14m\omega^2A^2$.", r"D: lấy $\omega^2=20/5=4$ do chưa đổi cm sang m."],
),
dict(
 q=r"Một vật dao động điều hoà theo phương trình $x=6\cos\left(\dfrac{10\pi}{3}t-\dfrac{\pi}{2}\right)$ cm. Quãng đường vật đi được từ $t=0$ đến $t=0{,}65$ s là",
 opts=[r"27 cm", r"26 cm", r"29,2 cm", r"30 cm"],
 sol=[r"$T=0{,}6$ s nên $\Delta t=0{,}65$ s $=T+\dfrac{T}{12}$. Một chu kì đi $4A=24$ cm. Lúc $t=0$ vật qua VTCB theo chiều dương; trong $\dfrac{T}{12}$ tiếp theo, góc quét $\dfrac{\pi}{6}$ đưa vật tới $x=A\sin\dfrac{\pi}{6}=3$ cm. Tổng quãng đường $24+3=27$ cm."],
 wrong=[r"B: giả sử quãng đường tỉ lệ với thời gian: $\frac{13}{12}\cdot24=26$ cm.", r"C: nhầm góc quét thành $\frac{\pi}{3}$ ($T/6$).", r"D: cho rằng $T/12$ vật đi được $A$ hoặc $T/4$ mới đi được $A$."],
),
dict(
 q=r"Con lắc lò xo treo thẳng đứng gồm vật nhỏ 0,1 kg, lò xo có độ cứng 40 N/m và chiều dài tự nhiên 30 cm. Kéo vật xuống dưới vị trí cân bằng 4 cm rồi thả nhẹ. Lấy $g=10$ m/s². Chiều dài cực tiểu của lò xo và độ lớn lực đàn hồi cực đại lần lượt là",
 opts=[r"28,5 cm; 2,6 N", r"28,5 cm; 1,6 N", r"26 cm; 2,6 N", r"32,5 cm; 1,6 N"],
 sol=[r"$\Delta\ell_0=\dfrac{mg}{k}=\dfrac{0{,}1\cdot10}{40}=2{,}5$ cm. $\ell_{CB}=30+2{,}5=32{,}5$ cm, $A=4$ cm nên $\ell_{min}=32{,}5-4=28{,}5$ cm (nhỏ hơn $\ell_0$: ở đó lò xo bị nén 1,5 cm). $F_{max}=k(\Delta\ell_0+A)=40\cdot0{,}065=2{,}6$ N."],
 wrong=[r"B: lấy $F_{max}=kA$, quên $\Delta\ell_0$.", r"C: lấy $\ell_{min}=\ell_0-A$ (nhầm chiều dài tự nhiên với chiều dài ở VTCB).", r"D: lấy chiều dài ở VTCB và $F=kA$."],
),
dict(
 q=r"Một con lắc đơn dài 1,0 m, vật nặng 0,1 kg, ở nơi có $g=\pi^2$ m/s². Kéo con lắc lệch khỏi phương thẳng đứng góc $9^\circ$ rồi thả nhẹ. Tốc độ cực đại và cơ năng của con lắc lần lượt là",
 opts=[r"0,49 m/s; 12,2 mJ", r"0,98 m/s; 48,7 mJ", r"0,16 m/s; 1,2 mJ", r"0,49 m/s; 24,4 mJ"],
 sol=[r"$\omega=\sqrt{g/\ell}=\pi$ rad/s. $\alpha_0=9^\circ=\dfrac{\pi}{20}$ rad nên $S_0=\ell\alpha_0=0{,}157$ m. $v_{max}=\omega S_0=\dfrac{\pi^2}{20}\approx0{,}49$ m/s. $W=\frac12mv_{max}^2=\frac12\cdot0{,}1\cdot0{,}2435\approx12{,}2$ mJ."],
 wrong=[r"B: nhân đôi tốc độ (dùng $\omega=2\pi$), cơ năng tăng gấp 4.", r"C: lấy $v_{max}=S_0$, quên nhân $\omega$.", r"D: đúng tốc độ nhưng quên hệ số $\frac12$ khi tính cơ năng."],
),
# ---------------- Muc 4: van dung cao, 3 chu de ----------------
dict(
 q=r"Một con lắc lò xo dao động tắt dần chậm, biên độ ban đầu 10 cm và cơ năng ban đầu 40 mJ. Sau mỗi chu kì, biên độ giảm 4% so với biên độ của chu kì liền trước. Sau 3 chu kì, biên độ và cơ năng còn lại lần lượt là",
 opts=[r"8,85 cm; 31,3 mJ", r"8,85 cm; 35,4 mJ", r"8,80 cm; 35,2 mJ", r"7,83 cm; 31,3 mJ"],
 sol=[r"Biên độ sau 3 chu kì: $A_3=10\cdot0{,}96^3=8{,}85$ cm. Cơ năng tỉ lệ $A^2$: $W_3=40\cdot(0{,}96^3)^2=40\cdot0{,}96^6\approx31{,}3$ mJ."],
 wrong=[r"B: quên bình phương khi suy ra cơ năng ($40\cdot0{,}96^3$).", r"C: cộng tuyến tính $3\cdot4\%=12\%$ cho cả biên độ và cơ năng.", r"D: áp dụng $0{,}96^6$ cho biên độ."],
),
dict(
 q=r"Con lắc lò xo nằm ngang gồm vật nhỏ 0,25 kg và lò xo độ cứng 100 N/m. Hệ số ma sát trượt giữa vật và mặt phẳng là 0,2 (coi ma sát nghỉ cực đại bằng ma sát trượt); lấy $g=10$ m/s². Kéo vật khỏi vị trí lò xo không biến dạng 8 cm rồi thả nhẹ. Tốc độ lớn nhất của vật trong lần đầu về phía vị trí lò xo không biến dạng, và biên độ (so với vị trí đó) tại lần dừng lại đầu tiên lần lượt là",
 opts=[r"1,50 m/s; 7,0 cm", r"1,60 m/s; 7,0 cm", r"1,50 m/s; 7,5 cm", r"1,40 m/s; 6,0 cm"],
 sol=[r"Vị trí cân bằng tạm thời lệch $x_0=\dfrac{\mu mg}{k}=\dfrac{0{,}2\cdot0{,}25\cdot10}{100}=0{,}5$ cm. $\omega=\sqrt{k/m}=20$ rad/s. Nửa chu kì đầu vật dao động điều hoà quanh điểm đó với biên độ $A_0-x_0=7{,}5$ cm nên $v_{max}=\omega(A_0-x_0)=20\cdot0{,}075=1{,}5$ m/s. Biên độ cuối nửa chu kì: $A_1=A_0-2x_0=7$ cm."],
 wrong=[r"B: $v_{max}=\omega A_0$, bỏ qua ma sát.", r"C: $A_1=A_0-x_0$ (chỉ trừ một lần $x_0$).", r"D: trừ $2x_0$ cho tốc độ và $4x_0$ cho biên độ."],
),
dict(
 q=r"Hình 3 là đồ thị thế năng theo thời gian của một con lắc lò xo nằm ngang có vật nặng 200 g. Lấy $\pi^2=10$. Chu kì và biên độ dao động của con lắc là",
 fig=("d1_q18.png", 6.9, "Hình 3"),
 opts=[r"0,2 s; 2 cm", r"0,1 s; 1 cm", r"0,4 s; 4 cm", r"0,1 s; 2 cm"],
 sol=[r"Thế năng biến thiên với chu kì $T/2$. Đồ thị cho $T/2=0{,}1$ s nên $T=0{,}2$ s, $\omega=\dfrac{2\pi}{T}=10\pi$ rad/s, $\omega^2=1000$ (với $\pi^2=10$). Cơ năng bằng giá trị cực đại của $W_t$: $W=40$ mJ $=\frac12m\omega^2A^2$, suy ra $A^2=\dfrac{2\cdot0{,}04}{0{,}2\cdot1000}=4\cdot10^{-4}$ m², $A=2$ cm."],
 wrong=[r"B: lấy chu kì của thế năng làm chu kì dao động ($T=0{,}1$ s), suy ra $A=1$ cm.", r"C: cho rằng chu kì dao động bằng hai lần chu kì của thế năng.", r"D: đúng biên độ nhưng chu kì sai, mâu thuẫn với $W$ đã cho."],
),
dict(
 q=r"Một xe chạy trên đoạn đường lát các tấm bê tông dài 3 m; mỗi chỗ nối giữa hai tấm gây một cú xóc lên xe. Phần khung xe được đỡ bởi hệ lò xo có độ cứng tổng cộng $2{,}5\cdot10^5$ N/m, khối lượng được đỡ là 250 kg. Lấy $\pi^2=10$. Xe rung mạnh nhất khi chạy với tốc độ",
 opts=[r"54 km/h", r"15 km/h", r"108 km/h", r"27 km/h"],
 sol=[r"Chu kì riêng: $T_0=2\pi\sqrt{\dfrac mk}=2\pi\sqrt{\dfrac{250}{2{,}5\cdot10^5}}=0{,}2$ s. Chu kì của lực cưỡng bức là thời gian đi hết một tấm: $T=\dfrac Lv$. Cộng hưởng khi $\dfrac Lv=T_0$ nên $v=\dfrac{L}{T_0}=\dfrac{3}{0{,}2}=15$ m/s $=54$ km/h."],
 wrong=[r"B: ghi 15 nhưng quên đổi m/s sang km/h.", r"C: dùng $T_0/2$ (nhầm với tần số gấp đôi).", r"D: dùng $T_0=0{,}4$ s."],
),
dict(
 q=r"Con lắc lò xo nằm ngang không ma sát gồm vật nhỏ 0,3 kg và lò xo độ cứng 30 N/m, dao động điều hoà với biên độ 10 cm. Đúng lúc vật qua vị trí cân bằng, một vật nhỏ khác khối lượng 0,1 kg được đặt nhẹ lên vật và dính chặt vào nó. Biên độ và cơ năng của dao động sau đó là",
 opts=[r"$5\sqrt3$ cm; 112,5 mJ", r"10 cm; 150 mJ", r"7,5 cm; 84,4 mJ", r"$5\sqrt3$ cm; 150 mJ"],
 sol=[r"Trước: $\omega=\sqrt{30/0{,}3}=10$ rad/s, $v_{max}=\omega A=1$ m/s. Theo phương ngang động lượng được bảo toàn: $0{,}3\cdot1=0{,}4v'$ nên $v'=0{,}75$ m/s. Sau: $\omega'=\sqrt{30/0{,}4}=5\sqrt3$ rad/s, tại VTCB nên $A'=\dfrac{v'}{\omega'}=\dfrac{0{,}75}{5\sqrt3}=5\sqrt3$ cm $\approx8{,}66$ cm. Cơ năng $W'=\frac12kA'^2=\frac12\cdot30\cdot(0{,}0866)^2=112{,}5$ mJ (nhỏ hơn $150$ mJ ban đầu: va chạm mềm làm mất cơ năng)."],
 wrong=[r"B: cho rằng cơ năng và biên độ không đổi.", r"C: lấy $A'=A\cdot\dfrac{m}{m+\Delta m}$ (nhầm tỉ lệ vận tốc với tỉ lệ biên độ).", r"D: đúng biên độ nhưng cho rằng cơ năng không đổi."],
),
]

# ---------------- PHAN II: 4 cau tu luan ----------------
ESS = [
dict(
 pts=1.25, level="DOK1",
 stem=r"Một vật dao động điều hoà trên đoạn thẳng dài 20 cm, thực hiện 50 dao động toàn phần trong 30 s. Chọn gốc thời gian lúc vật qua vị trí $x=5$ cm theo chiều âm. Lấy $\pi=3{,}14$ khi cần tính số.",
 parts=[
  (r"Viết phương trình li độ của vật.", 0.5),
  (r"Tính vận tốc và gia tốc của vật tại thời điểm $t=0$.", 0.5),
  (r"Tính thời điểm đầu tiên vật qua vị trí $x=-5\sqrt3$ cm.", 0.25),
 ],
 sol=[
  ("a", 0.5, [r"$A=\dfrac L2=10$ cm; $T=\dfrac{\Delta t}{N}=\dfrac{30}{50}=0{,}6$ s; $\omega=\dfrac{2\pi}{T}=\dfrac{10\pi}{3}$ rad/s. Lúc $t=0$: $x=5=\dfrac A2$ và $v<0$ nên $M$ ở nửa trên đường tròn pha, $\cos\varphi=\dfrac12$, $\varphi=+\dfrac\pi3$.", ("eq", r"x=10\cos\left(\dfrac{10\pi}{3}t+\dfrac\pi3\right)\ \text{cm}")]),
  ("b", 0.5, [r"$v_0=-\omega A\sin\varphi=-\dfrac{10\pi}{3}\cdot10\cdot\dfrac{\sqrt3}{2}=-\dfrac{50\sqrt3\,\pi}{3}\approx-90{,}7$ cm/s (vật đi theo chiều âm).", r"$a_0=-\omega^2x_0=-\left(\dfrac{10\pi}{3}\right)^2\cdot5\approx-548$ cm/s² (hướng về VTCB)."]),
  ("c", 0.25, [r"$\cos\alpha=-\dfrac{\sqrt3}{2}$ nên $\alpha=\dfrac{5\pi}{6}$. Từ pha $\dfrac\pi3$ (đang tăng) đến $\dfrac{5\pi}{6}$ quét $\Delta\alpha=\dfrac\pi2$, nên $t=\dfrac{\Delta\alpha}{\omega}=\dfrac{\pi/2}{10\pi/3}=0{,}15$ s, đúng bằng $T/4$."]),
 ],
 common=[r"Quên đổi $L$ thành $A=L/2$; chọn $\varphi=-\dfrac\pi3$ do chỉ giải $\cos\varphi=\dfrac12$ mà bỏ qua dấu của $v_0$."],
),
dict(
 pts=1.25, level="DOK2", fig=("d1_c22.png", 6.3, "Hình 4"),
 stem=r"Con lắc lò xo nằm ngang gồm vật nhỏ khối lượng $m=250$ g gắn vào lò xo nhẹ, ma sát không đáng kể. Kéo vật lệch khỏi vị trí cân bằng rồi thả nhẹ. Hình 4 là đồ thị thế năng đàn hồi $W_t$ theo li độ $x$ (đường parabol); đường nét đứt nằm ngang ứng với cơ năng $W=180$ mJ; đồ thị đi qua điểm có $x=4$ cm, $W_t=80$ mJ.",
 parts=[
  (r"Chứng minh gia tốc của vật là $a=-\dfrac{k}{m}x$ và vật dao động điều hoà.", 0.25),
  (r"Xác định độ cứng $k$, biên độ $A$, tần số góc $\omega$ và chu kì $T$.", 0.5),
  (r"Tại vị trí động năng bằng hai lần thế năng, tính độ lớn li độ và tốc độ của vật. Tính khoảng thời gian ngắn nhất giữa hai lần liên tiếp động năng bằng thế năng.", 0.5),
 ],
 sol=[
  ("a", 0.25, [r"Lực đàn hồi $F=-kx$ (định luật Hooke) là hợp lực theo phương ngang. Định luật II Newton $ma=-kx$ nên $a=-\dfrac kmx=-\omega^2x$ với $\omega^2=\dfrac km>0$. Gia tốc tỉ lệ với li độ và luôn ngược dấu nên vật dao động điều hoà."]),
  ("b", 0.5, [r"Từ điểm $(4\text{ cm};80\text{ mJ})$: $W_t=\dfrac12kx^2\Rightarrow k=\dfrac{2\cdot0{,}08}{0{,}04^2}=100$ N/m.", r"Cơ năng $W=\dfrac12kA^2=0{,}18$ J nên $A=\sqrt{\dfrac{2\cdot0{,}18}{100}}=0{,}06$ m $=6$ cm.", r"$\omega=\sqrt{\dfrac km}=\sqrt{\dfrac{100}{0{,}25}}=20$ rad/s; $T=\dfrac{2\pi}{\omega}=\dfrac{\pi}{10}\approx0{,}314$ s."]),
  ("c", 0.5, [r"$W_đ=2W_t$ nên $W=3W_t$, $A^2=3x^2$, $|x|=\dfrac{A}{\sqrt3}=2\sqrt3\approx3{,}46$ cm. Tốc độ: $|v|=\omega\sqrt{A^2-x^2}=20\sqrt{36-12}=40\sqrt6\approx98$ cm/s.", r"$W_đ=W_t$ ứng với $x=\pm\dfrac{A}{\sqrt2}$, 4 vị trí trên đường tròn pha, cách nhau $\dfrac\pi2$. Khoảng thời gian ngắn nhất giữa hai lần liên tiếp: $\Delta t=\dfrac T4=\dfrac{\pi}{40}\approx0{,}0785$ s."]),
 ],
 common=[r"Dùng $x$ tính bằng cm trong $\frac12kx^2$ mà không đổi sang mét; viết $W_đ=\frac12m\omega^2(A-x)^2$ thay vì $(A^2-x^2)$."],
),
dict(
 pts=1.25, level="DOK2", fig=("d1_c23.png", 4.6, "Hình 5"),
 stem=r"Con lắc lò xo treo thẳng đứng gồm lò xo nhẹ có chiều dài tự nhiên $\ell_0=40$ cm và vật nhỏ khối lượng $m=200$ g. Ở vị trí cân bằng, lò xo dãn $2{,}5$ cm (Hình 5). Kéo vật xuống dưới vị trí cân bằng 5 cm rồi thả nhẹ. Lấy $g=10$ m/s². Chọn trục $Ox$ hướng xuống, gốc $O$ tại vị trí cân bằng.",
 parts=[
  (r"Tính độ cứng $k$, tần số góc, chu kì dao động; chiều dài lớn nhất và nhỏ nhất của lò xo.", 0.5),
  (r"Tính cơ năng và độ lớn lực đàn hồi lớn nhất, nhỏ nhất của lò xo.", 0.5),
  (r"Tính thời gian lò xo bị nén trong một chu kì.", 0.25),
 ],
 sol=[
  ("a", 0.5, [r"$k=\dfrac{mg}{\Delta\ell_0}=\dfrac{0{,}2\cdot10}{0{,}025}=80$ N/m; $\omega=\sqrt{\dfrac km}=\sqrt{\dfrac{g}{\Delta\ell_0}}=20$ rad/s; $T=\dfrac{2\pi}{\omega}=\dfrac\pi{10}\approx0{,}314$ s. Thả nhẹ nên $A=5$ cm.", r"$\ell_{CB}=\ell_0+\Delta\ell_0=42{,}5$ cm; $\ell_{max}=\ell_{CB}+A=47{,}5$ cm; $\ell_{min}=\ell_{CB}-A=37{,}5$ cm."]),
  ("b", 0.5, [r"$W=\dfrac12kA^2=\dfrac12\cdot80\cdot0{,}05^2=0{,}1$ J.", r"$F_{max}=k(\Delta\ell_0+A)=80\cdot0{,}075=6$ N (ở biên dưới).", r"Vì $A>\Delta\ell_0$ nên vật đi qua vị trí lò xo có chiều dài tự nhiên ($x=-\Delta\ell_0=-2{,}5$ cm) và $F_{min}=0$."]),
  ("c", 0.25, [r"Lò xo bị nén khi $x<-\Delta\ell_0=-\dfrac A2$, tức vật ở nửa trên so với vị trí lò xo không biến dạng. Trên đường tròn pha, cung ứng với $x<-\dfrac A2$ là $\dfrac{2\pi}{3}$ (từ $\dfrac{2\pi}{3}$ đến $\dfrac{4\pi}{3}$). Thời gian nén: $\Delta t=\dfrac{2\pi/3}{2\pi}T=\dfrac T3=\dfrac{\pi}{30}\approx0{,}105$ s."]),
 ],
 common=[r"Nhầm $\Delta\ell_0$ với $A$; cho $F_{min}=k(\Delta\ell_0-A)<0$ thay vì nhận ra lò xo chuyển sang trạng thái nén nên $F_{min}=0$."],
),
dict(
 pts=1.25, level="DOK2-3", fig=("d1_c24.png", 5.6, "Hình 6"),
 stem=r"Một con lắc đơn dao động tắt dần chậm trong không khí. Chu kì dao động là 2,0 s, cơ năng ban đầu là 50 mJ và biên độ giảm 2% sau mỗi chu kì.",
 parts=[
  (r"Trong chu kì đầu tiên, cơ năng giảm bao nhiêu phần trăm và bao nhiêu mJ?", 0.25),
  (r"Tính công suất trung bình cần cung cấp để duy trì biên độ ban đầu (xét theo chu kì đầu).", 0.25),
  (r"Sau tối thiểu bao nhiêu chu kì thì cơ năng giảm xuống còn không quá một nửa cơ năng ban đầu?", 0.5),
  (r"Con lắc được đẩy bằng một lực tuần hoàn có tần số $f$ thay đổi được. Hình 6 là đường biểu diễn biên độ theo $f$ khi lực cản nhỏ. Hãy vẽ phác trên cùng hình đường biểu diễn khi lực cản lớn hơn và nêu một ví dụ cộng hưởng có lợi.", 0.25),
 ],
 sol=[
  ("a", 0.25, [r"Cơ năng tỉ lệ $A^2$: $\dfrac{W_1}{W_0}=(0{,}98)^2=0{,}9604$, nên cơ năng giảm $3{,}96\%$, tức $50\cdot0{,}0396\approx1{,}98$ mJ."]),
  ("b", 0.25, [r"Để duy trì biên độ, mỗi chu kì phải bù đúng phần cơ năng mất: $P=\dfrac{\Delta W}{T}=\dfrac{1{,}98\text{ mJ}}{2{,}0\text{ s}}\approx0{,}99\text{ mW}\approx1\text{ mW}$."]),
  ("c", 0.5, [r"Sau $n$ chu kì: $W_n=W_0\,(0{,}98)^{2n}\le\dfrac{W_0}{2}$, suy ra $n\ge\dfrac{\ln0{,}5}{2\ln0{,}98}\approx17{,}2$. Kiểm tra: $0{,}98^{34}\approx0{,}503>0{,}5$ (chưa đủ) và $0{,}98^{36}\approx0{,}483<0{,}5$. Vậy cần tối thiểu **18 chu kì** (36 s)."]),
  ("d", 0.25, [r"Đường cộng hưởng khi lực cản lớn hơn: vẫn có cực đại gần $f_0$ nhưng đỉnh thấp hơn và tù hơn, nằm dưới đường cũ ở mọi tần số (xem hình trong file đáp án). Ví dụ có lợi: hộp đàn ghita, violon; lò vi sóng."]),
 ],
 common=[r"Cho rằng biên độ giảm 2% thì cơ năng cũng chỉ giảm 2%; tính $n$ theo $0{,}98^{n}$ thay vì $0{,}98^{2n}$."],
 ans_fig=("a_c24.png", 7.0, "Hình đáp án Câu 24: hai đường cộng hưởng"),
),
]
