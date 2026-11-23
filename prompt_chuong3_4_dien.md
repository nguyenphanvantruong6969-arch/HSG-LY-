# Prompt: Chương 3 (Điện trường) và Chương 4 (Dòng điện, mạch điện) (`tai_lieu_pdf/chuong3_4.pdf`, 18 trang)

Khuyến nghị: tách thành HAI file HTML (Chương 3 gồm trang 1–12, Chương 4 gồm trang 13–18) để mỗi file nhẹ, dễ duyệt. Chạy lần lượt hai prompt dưới đây trong hai phiên riêng.

## Prompt A – Chương 3: Điện trường (trang 1–12)

```text
Vai trò: giáo viên Vật lí HSG + kỹ sư tài liệu. Biến Chương 3 (trang 1–12) của `tai_lieu_pdf/chuong3_4.pdf` thành MỘT file HTML tự chứa `chuong3_dien_truong.html` ở thư mục gốc repo, cùng cấu trúc, CSS, KaTeX và class với `chuong1_dao_dong_dieu_hoa.html` trên main (copy <head>/CSS/script từ file đó, không viết lại thư viện; chỉ viết <body> mới).

BƯỚC 0 – Đọc mẫu trên main, nắm các class: box quick/formula/tip/warn, proof (proof-head, pgoal, psteps, why, pcheck, pwrong), ex/hint/sol, details "Tự kiểm tra", TOC, "Tất cả chứng minh", "Bảng công thức", "Bài tập ôn luyện".

BƯỚC 1 – Đọc PDF trang 1–12 (có hình thì nhìn hình), gửi tôi bảng trích xuất rồi DỪNG chờ tôi xác nhận. Lưu ý đã biết:
- Cấu trúc: Bài 16 Lực tương tác giữa hai điện tích (kiến thức nền về nguyên tử, định luật Coulomb F = k|Q1Q2|/(εr²), k = 1/4πε0 ≈ 9·10^9, nguyên lí chồng chất lực) → Bài 17 Khái niệm điện trường (E = F/q, E = |Q|/(4πε0r²), đường sức, điện phổ) → Bài 18 Điện trường đều (E = U/d, chuyển động của điện tích bay vào vuông góc với đường sức → quỹ đạo parabol) → Bài 19–20 Thế năng điện, điện thế (A = qEd_MN, W_M = qEd, V_M = A/q, U_MN = V_M − V_N = A_MN/q = E·d_MN) → Bài 21 Tụ điện (C = Q/U, ghép song song/nối tiếp, W = ½QU = ½CU² = Q²/2C).
- Trang 6–7 là ảnh sách Giancoli bằng tiếng Anh (Example 17–2 electron trong ống TV: tăng tốc qua 5000 V, v ≈ 4,2·10^7 m/s; Conceptual Example 17–1 điện tích âm). Hãy dịch và trình bày lại thành ví dụ tiếng Việt, ghi nguồn "Giancoli".
- Các mục "Bài tập minh hoạ" chỉ trỏ tới ví dụ trong sách Giancoli (Example 16.3–16.5, 16.6–16.10, 17.1–17.2, 17.8) mà PDF không chứa nội dung: bỏ qua phần trỏ, thay bằng bài tự sinh.
- Lỗi/chỗ gồ ghề trong PDF cần xử lí: trang 8 viết "d_MN = QN × cos cos α" (lặp cos, là lỗi gõ: d_MN = NQ·cos α theo hình, α là góc giữa MN và phương đường sức... hãy tự đọc hình và nêu rõ góc nào); trang 4–5 hình đường sức chỉ có chữ trong bảng; vài ô "Nội dung chính" bị cắt chữ. Ghi chú những chỗ này trong báo cáo, không đoán.
- PDF không có bài tập. Toàn bộ bài tập là bài sinh mới.

BƯỚC 2 – Viết HTML từng phần lớn (Bài 16 → 17 → 18 → 19–20 → 21). Mỗi mục lý thuyết: Hiểu nhanh 1 câu → giải thích bằng hình ảnh đời thường → công thức trong khung formula kèm đơn vị → CHỨNG MINH/DẪN GIẢI ĐẦY ĐỦ → ví dụ mini có số → "Dễ sai" + "Mẹo nhớ" → "Tự kiểm tra". Khối chứng minh: Cần chứng minh → Ý tưởng → các bước nhỏ, mỗi bước một phép biến đổi và có "vì sao" → kết luận \boxed{} → kiểm tra nhanh (đơn vị, trường hợp biên) → lập luận sai thường gặp → nguồn "PDF tr.X". Cấm "dễ thấy", "suy ra" khi chưa nêu phép biến đổi.
Phân biệt rõ ba loại mệnh đề:
 (i) ĐỊNH LUẬT THỰC NGHIỆM (Coulomb, nguyên lí chồng chất): không chứng minh được; thay vào đó nêu thí nghiệm gốc, kiểm tra thứ nguyên, giải thích dạng 1/r² bằng hình học (mặt cầu 4πr²), và nói rõ đây là định luật;
 (ii) ĐỊNH NGHĨA (E = F/q, V = A/q, C = Q/U): giải thích vì sao định nghĩa như vậy và vì sao đại lượng đó không phụ thuộc điện tích thử;
 (iii) HỆ QUẢ: phải chứng minh đầy đủ.

Danh sách chứng minh/dẫn giải BẮT BUỘC (đánh số liên tục):
1. Hệ số k = 1/4πε0 ≈ 9·10^9 từ ε0 = 8,85·10^−12; lực trong môi trường: F = F_chân không/ε.
2. Lực Coulomb tuân định luật III Newton; hướng lực theo dấu điện tích (nêu quy tắc cùng dấu đẩy, trái dấu hút).
3. Chồng chất lực: tổng vectơ, cách tính bằng hình chiếu/định lí cosin cho 2 và 3 điện tích (ví dụ điện tích đặt tại đỉnh tam giác đều, hình vuông).
4. E của điện tích điểm: E = F/q = |Q|/(4πε0r²) suy ra từ Coulomb; hướng ra xa Q>0, vào gần Q<0; E không phụ thuộc q thử.
5. Chồng chất điện trường E = ΣE_i; E tại điểm giữa/trung trực của hai điện tích (có tính cụ thể).
6. Đường sức không cắt nhau, không khép kín (giải thích định tính vì sao: tại mỗi điểm E chỉ có một hướng; "không khép kín" ghi là kết quả đúng cho điện trường tĩnh, chứng minh chặt cần công bảo toàn, nên nói sau mục công).
7. Điện trường đều và E = U/d: từ A = qEd = qU, suy ra U = Ed.
8. Chuyển động của hạt khối lượng m, điện tích q bay vào điện trường đều với v0 ⟂ E: a = qE/m, x = v0t, y = ½at², suy ra quỹ đạo y = qE x²/(2mv0²) (parabol); góc lệch, thời gian bay, độ lệch khi ra khỏi bản dài ℓ.
9. Tăng tốc qua hiệu điện thế: ½mv² = |q|U, v = √(2|q|U/m); kiểm tra lại ví dụ electron 5000 V → 4,2·10^7 m/s và proton 5000 V (Exercise A).
10. Công lực điện trong điện trường đều A = qEd_MN: tính công trên đoạn thẳng MN bất kì bằng A = F·MN·cosα = qE·(MN cosα) với d_MN = hình chiếu MN lên phương đường sức; dấu của A theo α < 90°, = 90°, > 90°.
11. Công không phụ thuộc đường đi: chia đường cong thành các đoạn nhỏ, tổng hình chiếu lên phương E luôn bằng d_MN; hệ quả: công theo đường kín bằng 0 (điện trường là trường thế).
12. Thế năng W_M = qEd (chọn gốc thế năng tại bản âm) và W_M = A_M∞ (chọn gốc ở vô cực), A_MN = W_M − W_N.
13. Điện thế V_M = A/q, U_MN = V_M − V_N = A_MN/q = E·d_MN; phân biệt điện thế (độc lập q) và thế năng (phụ thuộc q) bằng ví dụ 10 J/2 C và 100 J/20 C; dấu của ΔPE = qV_ba cho điện tích âm/dương.
14. Điện dung C = Q/U là hằng số của tụ (không đổi theo Q, U); tụ phẳng C = ε0εS/d (Bổ sung, chứng minh từ E = σ/ε0ε hoặc U = Ed; nếu dùng định lí Gauss thì ghi rõ Bổ sung).
15. Ghép tụ song song: U chung, Q = ΣQ_i, suy ra C = ΣC_i; ghép nối tiếp: Q chung, U = ΣU_i, suy ra 1/C = Σ1/C_i. Mỗi cái chứng minh từng bước.
16. Năng lượng tụ W = ½QU = ½CU² = Q²/2C: chứng minh bằng công đưa từng phần điện tích dq (U' = q/C, W = ∫0^Q q/C dq = Q²/2C) và giải thích bằng diện tích tam giác trên đồ thị U–q; hai cách biểu diễn khác nhau khi tụ nối nguồn (U không đổi) và khi ngắt nguồn (Q không đổi).

BƯỚC 3 – Bài tập mới theo DẠNG. Mỗi dạng: nhận dạng, phương pháp 3–4 bước, 1 ví dụ mẫu giải đủ, rồi 6 bài tăng dần (2 cơ bản, 2 vận dụng, 1 DOK3, 1 Olympic), mỗi bài có Gợi ý 1 → Gợi ý 2 → Lời giải trong <details>, ghi mức độ và link ngược tới chứng minh.
D1. Lực Coulomb giữa hai điện tích; thay đổi khoảng cách/môi trường; cân bằng của hai quả cầu treo (góc lệch α, tan α = F/P).
D2. Chồng chất lực lên một điện tích (tam giác, hình vuông, ba điện tích thẳng hàng); điều kiện cân bằng của điện tích thứ ba.
D3. Cường độ điện trường của điện tích điểm; điểm có E = 0 trên đường nối hai điện tích; E tổng hợp của hệ điện tích tại đỉnh hình.
D4. Điện trường đều: E = U/d, cân bằng của hạt bụi/giọt dầu giữa hai bản, quả cầu tích điện treo trong điện trường đều.
D5. Chuyển động trong điện trường đều: tăng tốc dọc đường sức; bay vào vuông góc (độ lệch, góc ló, có bắn trúng màn không); electron trong ống tia âm cực.
D6. Công lực điện, thế năng, điện thế, hiệu điện thế: A = qEd, định lí động năng, bảo toàn năng lượng cho điện tích chuyển động, mặt đẳng thế.
D7. Tụ điện: C = Q/U, ghép tụ (song song, nối tiếp, hỗn hợp), nối tụ đã tích điện với nhau (bảo toàn điện tích, mất mát năng lượng), năng lượng tụ khi nối nguồn / ngắt nguồn / đưa tấm điện môi vào (Bổ sung).

QUY TẮC CHẤT LƯỢNG
- KaTeX ($...$, $$...$$), dấu thập phân kiểu Việt 0{,}5; mọi đại lượng có đơn vị, đổi đơn vị µC, nC, pF cẩn thận.
- Mọi đáp số tự kiểm bằng Python/sympy trước khi ghi; bài vectơ/quỹ đạo kiểm bằng numpy.
- Hình vẽ SVG hoặc matplotlib nhúng inline, có chú thích: đường sức (điện tích điểm, hai điện tích cùng dấu/trái dấu), hai bản phẳng, quỹ đạo parabol, đồ thị U–q của tụ.
- Phần ngoài PDF ghi rõ "Bổ sung"; không bịa rồi gán cho PDF.
- Chạy thử bằng Playwright: không lỗi KaTeX/console, TOC và link chứng minh hoạt động, xem được ở khổ điện thoại; chụp 3 ảnh cho tôi duyệt.
- Báo cáo cuối: số chứng minh, số bài sinh thêm, chỗ không chắc, các lỗi PDF đã phát hiện.

Commit lên nhánh hiện tại, chưa mở PR.
```

## Prompt B – Chương 4: Dòng điện, mạch điện (trang 13–18)

```text
Vai trò: giáo viên Vật lí HSG + kỹ sư tài liệu. Biến Chương 4 (trang 13–18) của `tai_lieu_pdf/chuong3_4.pdf` thành MỘT file HTML tự chứa `chuong4_dong_dien.html` ở thư mục gốc repo, cùng cấu trúc, CSS, KaTeX và class với `chuong1_dao_dong_dieu_hoa.html` trên main (copy <head>/CSS/script từ file đó, không viết lại thư viện; chỉ viết <body> mới). Nếu `chuong3_dien_truong.html` đã có, dùng nó làm mẫu thứ hai về cách đánh số chứng minh và liên kết chéo tới chương 3 (điện thế, hiệu điện thế, công lực điện).

BƯỚC 0 – Đọc mẫu trên main, nắm các class: box quick/formula/tip/warn, proof (proof-head, pgoal, psteps, why, pcheck, pwrong), ex/hint/sol, details "Tự kiểm tra", TOC, "Tất cả chứng minh", "Bảng công thức", "Bài tập ôn luyện".

BƯỚC 1 – Đọc PDF trang 13–18 (có hình thì nhìn hình), gửi tôi bảng trích xuất rồi DỪNG chờ tôi xác nhận. Lưu ý đã biết:
- Cấu trúc: trang 13 là truyện tranh mạch song song (ba bóng đèn nối song song vào ắc quy 12 V: độ sáng không đổi, dòng từ nguồn tăng gấp 3, điện trở tương đương giảm còn 1/3, ắc quy hết nhanh gấp 3) → hãy diễn giải thành một ví dụ có số, không chép hình → Bài 22 Cường độ dòng điện (I = Δq/Δt, I = Snve, v = I/(Sne)) → Bài 23 Điện trở, định luật Ôm (R = ρℓ/S, I = U/R, ảnh hưởng nhiệt độ) → Bài 24 Nguồn điện (lực lạ, ε = A/q, điện trở trong r) → Bài 25 Năng lượng điện và công suất (W = qU = UIt, P = UI, A_ng = qε = εIt, P_ng = εI, hiệu suất H = U/ε).
- PDF có trích "Bài tập minh hoạ" chỉ trỏ tới sách Giancoli (Example 18.5, 18.7, 17.8): không chứa nội dung, bỏ qua và thay bằng bài tự sinh. Lưu ý trang 16 trỏ nhầm "Example 17.8 / trang 484" cho mục Ohm (thuộc phần tụ điện), hãy ghi chú đây là chỗ PDF trỏ nhầm.
- Một số khung "Nội dung chính" bị cắt chữ ở cuối. Ghi chú, không đoán nội dung bị mất.
- PDF không có phần ghép điện trở, định luật Ôm cho toàn mạch ε = I(R + r), công thức ε = U + Ir, định luật Joule: đây là Bổ sung cần thiết cho bài tập; nếu thêm, đặt trong mục có nhãn "Bổ sung" và chứng minh đầy đủ. PDF không có bài tập.

BƯỚC 2 – Viết HTML từng phần lớn (truyện tranh/mạch song song → Bài 22 → 23 → 24 → 25 → Bổ sung ghép điện trở và toàn mạch). Mỗi mục lý thuyết: Hiểu nhanh 1 câu → giải thích bằng hình ảnh đời thường (ống nước, máy bơm) → công thức trong khung formula kèm đơn vị → CHỨNG MINH ĐẦY ĐỦ → ví dụ mini có số → "Dễ sai" + "Mẹo nhớ" → "Tự kiểm tra". Khối chứng minh: Cần chứng minh → Ý tưởng → các bước nhỏ, mỗi bước một phép biến đổi và có "vì sao" → kết luận \boxed{} → kiểm tra nhanh (đơn vị, trường hợp biên) → lập luận sai thường gặp → nguồn "PDF tr.X". Cấm "dễ thấy", "suy ra" khi chưa nêu phép biến đổi.
Phân biệt rõ: ĐỊNH NGHĨA (I = Δq/Δt, R, ε) / ĐỊNH LUẬT THỰC NGHIỆM (Ôm chỉ đúng cho vật dẫn kim loại ở nhiệt độ không đổi, không chứng minh được, chỉ giải thích vi mô và nêu điều kiện) / HỆ QUẢ (phải chứng minh).

Danh sách chứng minh BẮT BUỘC (đánh số liên tục):
1. I = Snve: xét hình trụ đáy S, cao h = vΔt chứa nS·vΔt hạt, Δq = nS·vΔt·e, chia cho Δt; hệ quả v = I/(Sne); tính tốc độ trôi của electron trong dây đồng (ví dụ số cụ thể, chỉ cỡ 10^−4 m/s) và giải thích vì sao đèn sáng ngay khi bật công tắc.
2. Chiều dòng điện quy ước và dòng điện trong dung dịch/khí có cả hạt dương và âm: I = (|q+|n+ v+ + |q−|n− v−)S (Bổ sung).
3. Đơn vị ampe từ Δq/Δt; 1 A = 1 C/s; quan hệ với số electron mỗi giây (1 A ≈ 6,25·10^18 e/s).
4. R = ρℓ/S: chứng minh bằng hai nhận xét ghép điện trở (hai dây giống nhau nối tiếp thì R tăng gấp đôi → R ∝ ℓ; hai dây giống nhau song song thì R giảm một nửa → R ∝ 1/S), rồi kết hợp; ghi rõ đây là chứng minh logic dựa trên quy tắc ghép điện trở (chứng minh ghép R ở mục Bổ sung).
5. Điện trở phụ thuộc nhiệt độ: R = R0[1 + α(t − t0)] (Bổ sung, giải thích vi mô: ion dao động mạnh hơn, va chạm nhiều hơn); phân biệt dây tóc bóng đèn (R tăng theo T) và nhiệt điện trở thermistor (R giảm theo T).
6. Định luật Ôm I = U/R: đồ thị I–U của vật dẫn kim loại là đường thẳng đi qua gốc, R = U/I = hệ số góc nghịch đảo; giải thích vì sao đồ thị bóng đèn dây tóc cong.
7. Ghép điện trở (Bổ sung): nối tiếp R = ΣR_i, song song 1/R = Σ1/R_i, từ I và U; kiểm tra lại truyện tranh: 3 nhánh song song, điện trở tương đương còn 1/3, dòng tổng gấp 3 ở cùng 12 V.
8. ε = A/q của nguồn: công lực lạ khi chuyển điện tích dương q từ cực âm sang cực dương; nguồn như "máy bơm điện tích", không tạo ra điện tích.
9. Điện trở trong: U = ε − Ir khi có dòng I; U = ε khi hở mạch; U = 0 khi đoản mạch, dòng đoản mạch I = ε/r (chứng minh từ bảo toàn năng lượng: ε I = U I + I²r); suy ra I = ε/(R + r) (Bổ sung).
10. W = A = qU = UIt (từ q = It); P = A/t = UI; với đoạn mạch chỉ có điện trở R: P = I²R = U²/R (dùng định luật Ôm); nhiệt lượng Q = I²Rt (Joule, Bổ sung); đổi kWh sang J (1 kWh = 3,6·10^6 J).
11. Công và công suất của nguồn A_ng = qε = εIt, P_ng = εI; hiệu suất H = P/P_ng = UIt/(εIt) = U/ε = R/(R + r).
12. Công suất cực đại mà nguồn cấp cho mạch ngoài khi R = r: chứng minh bằng bất đẳng thức Cô-si hoặc đạo hàm, P_max = ε²/4r, H = 50% (Bổ sung, bài nâng cao).

BƯỚC 3 – Bài tập mới theo DẠNG. Mỗi dạng: nhận dạng, phương pháp 3–4 bước, 1 ví dụ mẫu giải đủ, rồi 6 bài tăng dần (2 cơ bản, 2 vận dụng, 1 DOK3, 1 Olympic), mỗi bài có Gợi ý 1 → Gợi ý 2 → Lời giải trong <details>, ghi mức độ và link ngược tới chứng minh.
D1. Cường độ dòng điện: I = Δq/Δt, số electron qua tiết diện trong 1 s, đồ thị q–t.
D2. Tốc độ trôi: I = Snve, thay đổi đường kính dây, so sánh tốc độ trôi với tốc độ lan truyền tín hiệu.
D3. Điện trở dây dẫn: R = ρℓ/S, kéo dãn dây (thể tích không đổi, ℓ tăng k lần thì R tăng k² lần), cắt dây rồi ghép lại, ảnh hưởng nhiệt độ.
D4. Định luật Ôm và đường đặc trưng I–U: đọc đồ thị, bóng đèn dây tóc và thermistor, xác định R từ số liệu U–I (hồi quy bình phương tối thiểu đơn giản).
D5. Ghép điện trở và mạch hỗn hợp (Bổ sung): điện trở tương đương, phân bố dòng, phân áp, cầu cân bằng.
D6. Nguồn điện: ε, r, U = ε − Ir, đồ thị U–I của nguồn (cắt trục tung tại ε, hệ số góc −r), ghép nguồn nối tiếp/song song (Bổ sung).
D7. Năng lượng và công suất: W = UIt, P = UI, tiền điện (kWh), bóng đèn định mức, mắc đèn vào hiệu điện thế khác định mức, nhiệt lượng đun nước (có hiệu suất).
D8. Hiệu suất nguồn và công suất cực đại: H = U/ε, tìm R để P mạch ngoài cực đại, so sánh hai giá trị R cho cùng công suất (R1R2 = r²).
D9. Bài tổng hợp Chương 3 + 4: tụ nối nguồn qua điện trở (năng lượng tụ so với nhiệt tỏa ra trên điện trở, vì sao đúng một nửa năng lượng nguồn bị tiêu hao); electron trong dây vừa chịu E = U/ℓ.

QUY TẮC CHẤT LƯỢNG
- KaTeX ($...$, $$...$$), dấu thập phân kiểu Việt 0{,}5; mọi đại lượng có đơn vị.
- Mọi đáp số tự kiểm bằng Python/sympy trước khi ghi; bài cực trị kiểm bằng numpy.
- Hình vẽ SVG hoặc matplotlib nhúng inline, có chú thích: dây dẫn có hạt tải, sơ đồ mạch, đồ thị I–U (kim loại, bóng đèn, thermistor), đồ thị U–I của nguồn, đồ thị P theo R.
- Phần ngoài PDF ghi rõ "Bổ sung"; không bịa rồi gán cho PDF.
- Chạy thử bằng Playwright: không lỗi KaTeX/console, TOC và link chứng minh hoạt động, xem được ở khổ điện thoại; chụp 3 ảnh cho tôi duyệt.
- Báo cáo cuối: số chứng minh, số bài sinh thêm, chỗ không chắc, các lỗi PDF đã phát hiện.

Commit lên nhánh hiện tại, chưa mở PR.
```
