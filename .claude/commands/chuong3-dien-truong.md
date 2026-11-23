---
description: Chuyển Chương 3 (Điện trường) từ PDF sang HTML học tập có chứng minh và bài luyện
---
Mẫu giao diện: `chuong1_dao_dong_dieu_hoa.html` (có sẵn trên main). Mọi thông tin cần thiết nằm trong file này. Nguồn: `tai_lieu_pdf/chuong3_4.pdf`, CHỈ trang 1–12. Đầu ra: `chuong3_dien_truong.html`.

Lưu ý PDF: trang 6–7 là ảnh sách Giancoli tiếng Anh (electron trong ống TV tăng tốc 5000 V, v ≈ 4,2·10^7 m/s; điện tích âm): dịch lại, ghi nguồn. Các mục "Bài tập minh hoạ" chỉ trỏ sang sách, bỏ qua. Trang 8 có lỗi gõ "cos cos α": tự đọc hình, nêu rõ góc nào. Một số khung "Nội dung chính" bị cắt chữ: ghi chú, không đoán. PDF không có bài tập.

Cấu trúc: B16 Coulomb, chồng chất lực → B17 điện trường (E = F/q), đường sức → B18 điện trường đều (E = U/d), chuyển động parabol → B19–20 công, thế năng, điện thế (A = qEd, V = A/q, U = Ed) → B21 tụ điện (C = Q/U, ghép, W = ½CU²).

Chứng minh/dẫn giải bắt buộc (Coulomb và chồng chất là định luật thực nghiệm: nêu thí nghiệm, thứ nguyên, 1/r² từ mặt cầu 4πr²):
1. k = 1/4πε0 ≈ 9·10^9; F = F_chân không/ε.
2. Lực Coulomb tuân định luật III; quy tắc dấu.
3. Chồng chất lực bằng hình chiếu/định lí cosin (tam giác đều, hình vuông).
4. E điện tích điểm từ Coulomb; E không phụ thuộc q thử.
5. Chồng chất E; E tại trung điểm, trung trực hai điện tích.
6. Đường sức không cắt nhau; không khép kín (chặt chẽ sau mục công).
7. U = Ed từ A = qEd = qU.
8. Quỹ đạo y = qEx²/(2mv0²) khi v0 ⟂ E; góc lệch, độ lệch ra khỏi bản.
9. Tăng tốc: v = √(2|q|U/m); kiểm ví dụ electron và proton 5000 V.
10. Công A = qEd_MN trên đoạn thẳng bất kì; dấu theo α.
11. Công không phụ thuộc đường đi; công theo đường kín bằng 0.
12. Thế năng W = qEd, W_M = A_M∞, A_MN = W_M − W_N.
13. V = A/q, U_MN = Ed_MN; điện thế khác thế năng (10 J/2 C và 100 J/20 C).
14. C = Q/U là hằng số của tụ; C = ε0εS/d (Bổ sung).
15. Ghép tụ song song C = ΣC_i; nối tiếp 1/C = Σ1/C_i.
16. W = ½CU² bằng ∫q/C dq và diện tích tam giác U–q; nối nguồn khác ngắt nguồn.

Dạng bài (sinh mới): D1 lực Coulomb, hai quả cầu treo; D2 chồng chất lực, cân bằng điện tích thứ ba; D3 E điện tích điểm, điểm E = 0; D4 điện trường đều, hạt bụi cân bằng; D5 chuyển động trong điện trường đều (tăng tốc, bay vuông góc); D6 công, thế năng, điện thế, bảo toàn năng lượng; D7 tụ điện (ghép, nối tụ đã tích điện, nối/ngắt nguồn, điện môi).
Hình cần vẽ: đường sức, hai bản phẳng, quỹ đạo parabol, đồ thị U–q.


## Quy trình (bắt buộc)

### Bước 0 – Đọc mẫu
Copy <head>/CSS/script của mẫu, không viết lại thư viện; chỉ viết <body> mới. Nắm các class: box quick/formula/tip/warn, proof (proof-head, pgoal, psteps, why, pcheck, pwrong), ex/hint/sol, details "Tự kiểm tra", TOC, "Tất cả chứng minh", "Bảng công thức", "Bài tập ôn luyện".

### Bước 1 – Trích xuất PDF (DỪNG chờ xác nhận)
Đọc từng trang (có hình thì nhìn hình). Gửi bảng ngắn: mục → công thức → định nghĩa → ví dụ → bài tập → hình, kèm số trang; liệt kê và đánh số mọi công thức. Chỗ đọc không chắc thì hỏi, không đoán. Chờ người dùng xác nhận rồi mới viết HTML.

### Bước 2 – Viết HTML (mỗi lần một phần lớn)
Mỗi mục lý thuyết theo thứ tự: Hiểu nhanh 1 câu → giải thích bằng ví dụ đời thường → công thức trong khung formula kèm đơn vị → CHỨNG MINH ĐẦY ĐỦ → ví dụ mini có số → "Dễ sai" + "Mẹo nhớ" → "Tự kiểm tra" (details có đáp án).
Khối chứng minh: Cần chứng minh → Ý tưởng → các bước nhỏ (mỗi bước một phép biến đổi, có "vì sao") → kết luận \boxed{} → kiểm tra nhanh (đơn vị, trường hợp biên) → lập luận sai thường gặp → nguồn "PDF tr.X". Cấm "dễ thấy", "suy ra" khi chưa nêu phép biến đổi.
Phân biệt: định nghĩa / định luật thực nghiệm (không chứng minh được: nêu thí nghiệm gốc, thứ nguyên, điều kiện áp dụng) / hệ quả (chứng minh đầy đủ).
Cuối trang: "Tất cả chứng minh" (link), "Bảng công thức tổng hợp" (công thức + điều kiện + link chứng minh).

### Bước 3 – Bài tập theo dạng
Mỗi dạng: nhận dạng, phương pháp 3–4 bước, 1 ví dụ mẫu giải đủ, rồi 6 bài tăng dần (2 cơ bản, 2 vận dụng, 1 DOK3, 1 Olympic). Mỗi bài có Gợi ý 1 → Gợi ý 2 → Lời giải trong <details>, ghi mức độ và link ngược tới chứng minh. Bài trong PDF (nếu có) chuyển nguyên số liệu thành khối `ex`.

### Quy tắc chất lượng
- KaTeX, dấu thập phân kiểu Việt 0{,}5, mọi đại lượng có đơn vị.
- Mọi đáp số tự kiểm bằng Python/sympy/numpy trước khi ghi.
- Hình vẽ SVG hoặc matplotlib nhúng inline, có chú thích trục và đơn vị.
- Nội dung ngoài PDF ghi rõ "Bổ sung"; không gán cho PDF điều PDF không viết.
- Chạy thử bằng Playwright: không lỗi KaTeX/console, TOC và link hoạt động, đúng ở khổ điện thoại; chụp 3 ảnh để duyệt.
- Báo cáo cuối: số chứng minh, số bài sinh thêm, chỗ không chắc, lỗi PDF phát hiện.
- Commit lên nhánh hiện tại, chưa mở PR.
