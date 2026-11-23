---
description: Chuyển Chương 2 (Sóng) từ PDF sang HTML học tập có chứng minh và bài luyện
---
Mẫu giao diện: `chuong1_dao_dong_dieu_hoa.html` (có sẵn trên main). Mọi thông tin cần thiết nằm trong file này. Nguồn: `tai_lieu_pdf/chuong2_song.pdf` (11 trang). Đầu ra: `chuong2_song.html`.

Lưu ý PDF: đánh số Bài 1, 2, 3, 5, 6 (không có Bài 4, giữ nguyên số). Chỉ nêu kết quả, không chứng minh, không có bài tập. QR/video trang 6 không xem được, thay bằng mô tả chữ.

Cấu trúc: B1 mô tả sóng (λ = vT = v/f) → B2 sóng ngang/dọc, âm, phương trình sóng (Δφ = 2πd/λ; u = A cos(ωt − 2πd/λ)) → B3 sóng điện từ (v = c/n, λ = c/f, thang sóng) → B5 giao thoa (A. sóng nước; B. Young) → B6 sóng dừng, nhạc cụ.

Chứng minh bắt buộc:
1. λ = vT = v/f.
2. u_M = A cos(ωt − 2πd/λ) và Δφ = ωd/v = 2πd/λ (sóng tới M trễ d/v).
3. Điểm cùng pha, ngược pha, vuông pha từ Δφ.
4. Sóng ngang/dọc truyền trong môi trường nào (giải thích định tính, ghi rõ).
5. v = c/n; λ' = λ/n (f không đổi).
6. Tổng hợp hai sóng kết hợp bằng cos a + cos b: A_M = 2A|cos(π(d1−d2)/λ)|.
7. Cực đại d1−d2 = kλ; cực tiểu d1−d2 = (k+½)λ.
8. Đếm cực đại/cực tiểu trên S1S2 (hai nguồn cùng pha; ngược pha là Bổ sung).
9. Young: d2²−d1² = 2ax ⇒ d2−d1 ≈ ax/D (nêu xấp xỉ), x_k = kλD/a, i = λD/a.
10. n vân liên tiếp cách (n−1)i; i' = i/n trong môi trường (Bổ sung).
11. Sóng dừng: cộng sóng tới và sóng phản xạ (đầu cố định đổi pha π, đầu tự do không đổi) ⇒ nút, bụng, khoảng cách λ/2 và λ/4.
12. Điều kiện sóng dừng: ℓ = kλ/2 (bụng k, nút k+1); ℓ = (2k+1)λ/4 (bụng = nút = k+1).
13. Nhạc cụ: f = kv/2ℓ; f = (2k+1)v/4ℓ.
14. Hai lần dây duỗi thẳng liên tiếp cách T/2.

Dạng bài (PDF không có bài, toàn bộ sinh mới):
D1 đại lượng đặc trưng; D2 viết phương trình sóng; D3 độ lệch pha, cùng/ngược pha; D4 đồ thị u–x, u–t; D5 sóng điện từ, radar/siêu âm; D6 giao thoa sóng nước (đếm cực trị trên S1S2, đường tròn, elip); D7 giao thoa Young (đếm vân, vân trùng, đổi môi trường, ánh sáng trắng); D8 sóng dừng (hai đầu cố định, một đầu tự do, biên độ tại điểm); D9 nhạc cụ, ống cộng hưởng.
Hình cần vẽ: đồ thị sóng, hệ vân hyperbol, sơ đồ Young, sóng dừng hai loại đầu. Mô phỏng numpy để kiểm các bài đếm cực trị.


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
