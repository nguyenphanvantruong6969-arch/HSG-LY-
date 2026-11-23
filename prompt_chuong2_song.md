# Prompt: Chương 2 – Sóng (`tai_lieu_pdf/chuong2_song.pdf`, 11 trang)

```text
Vai trò: giáo viên Vật lí HSG + kỹ sư tài liệu. Biến `tai_lieu_pdf/chuong2_song.pdf` (Vật lí 11, Chương 2: Sóng, 11 trang) thành MỘT file HTML tự chứa `chuong2_song.html` ở thư mục gốc repo, cùng cấu trúc, CSS, KaTeX và class với `chuong1_dao_dong_dieu_hoa.html` trên main (copy <head>/CSS/script từ file đó, KHÔNG viết lại thư viện; chỉ viết <body> mới).

BƯỚC 0 – Đọc mẫu trên main, nắm các class: box quick/formula/tip/warn, proof (proof-head, pgoal, psteps, why, pcheck, pwrong), ex/hint/sol, details "Tự kiểm tra", TOC, "Tất cả chứng minh", "Bảng công thức", "Bài tập ôn luyện".

BƯỚC 1 – Đọc PDF theo từng trang (có hình thì nhìn hình), gửi tôi bảng trích xuất rồi DỪNG chờ tôi xác nhận. Lưu ý đã biết về PDF này:
- Đánh số bài nhảy cách: Bài 1, 2, 3, rồi Bài 5, 6 (không có Bài 4). Giữ nguyên số bài của PDF, ghi chú "PDF không có Bài 4".
- Cấu trúc: Bài 1 Mô tả sóng (sóng cơ, biên độ, chu kì, tần số, tốc độ, bước sóng, năng lượng; λ = vT = v/f) → Bài 2 Sóng ngang/sóng dọc, truyền năng lượng, tính chất âm thanh, PHƯƠNG TRÌNH TRUYỀN SÓNG (Δφ = ωd/v = 2πd/λ; u_M = A cos(ωt − 2πd/λ)) → Bài 3 Sóng điện từ (v = c/n, λ = c/f, thang sóng: hồng ngoại, tử ngoại, tia X, gamma, vô tuyến) → Bài 5 Giao thoa (A. sóng nước: tổng hợp u_M = 2A cos(π(d1−d2)/λ) cos(ωt − π(d1+d2)/λ), cực đại d1−d2 = kλ, cực tiểu d1−d2 = (k+1/2)λ; B. Young: d2−d1 = ax/D, x = kλD/a, i = λD/a) → Bài 6 Sóng dừng (nút, bụng, khoảng cách nút–nút = λ/2, nút–bụng = (2k+1)λ/4; hai đầu cố định ℓ = kλ/2, một đầu cố định ℓ = (2k+1)λ/4; số bụng, số nút; nhạc cụ f = k·v/2ℓ và f = (2k+1)·v/4ℓ; Δt giữa hai lần sợi dây duỗi thẳng = T/2).
- PDF CHỈ nêu kết quả, không chứng minh. PDF không có bài tập: toàn bộ bài tập là bài tôi yêu cầu sinh thêm.
- Các QR/video trong PDF (trang 6) không xem được: ghi "xem video trong PDF" và thay bằng mô tả bằng chữ.

BƯỚC 2 – Viết HTML từng phần lớn (Bài 1–2 → Bài 3 → Bài 5A → Bài 5B → Bài 6), mỗi mục lý thuyết gồm: Hiểu nhanh 1 câu → giải thích bằng hình ảnh đời thường → công thức trong khung formula kèm đơn vị → CHỨNG MINH ĐẦY ĐỦ → ví dụ mini có số → "Dễ sai" + "Mẹo nhớ" → "Tự kiểm tra" (details có đáp án). Khối chứng minh: Cần chứng minh → Ý tưởng → các bước nhỏ, mỗi bước một phép biến đổi và có "vì sao" → kết luận \boxed{} → kiểm tra nhanh (đơn vị, trường hợp biên) → lập luận sai thường gặp → nguồn "PDF tr.X". Cấm "dễ thấy", "suy ra" khi chưa nêu phép biến đổi.

Danh sách chứng minh BẮT BUỘC (đánh số liên tục, tối thiểu):
1. λ = vT = v/f (quãng đường sóng đi được trong một chu kì).
2. Phương trình truyền sóng u_M = A cos(ωt − 2πd/λ): sóng tới M trễ thời gian d/v, suy ra pha trễ ω·d/v = 2πd/λ; từ đó Δφ = ωd/v = 2πd/λ.
3. Điểm cùng pha / ngược pha / vuông pha: d = kλ, (k+1/2)λ, (k+1/4)λ... từ Δφ.
4. Sóng ngang/sóng dọc truyền được trong môi trường nào (giải thích bằng lực liên kết/lực cắt, không chứng minh định lượng; ghi rõ là giải thích định tính).
5. v = c/n và λ = c/f cho sóng điện từ; λ' = λ/n khi vào môi trường (f không đổi).
6. Tổng hợp hai sóng kết hợp tại M: dùng cos a + cos b = 2cos((a+b)/2)cos((a−b)/2), rút ra biên độ A_M = 2A|cos(π(d1−d2)/λ)| và pha φ_M.
7. Điều kiện cực đại d1−d2 = kλ và cực tiểu d1−d2 = (k+1/2)λ.
8. Số cực đại/cực tiểu trên đoạn S1S2 (chặn k bằng |d1−d2| ≤ S1S2): lập công thức đếm, nêu rõ trường hợp hai nguồn cùng pha và ngược pha (ngược pha là Bổ sung).
9. Hệ vân Young: d2² − d1² = 2ax, suy ra d2 − d1 = 2ax/(d1+d2) ≈ ax/D khi a, x << D (nêu rõ phép xấp xỉ và sai số); x_k = kλD/a, x_t = (k+1/2)λD/a, i = λD/a, λ = ia/D.
10. Khoảng cách n vân liên tiếp = (n−1)i; khi cả hệ đặt trong môi trường chiết suất n thì i' = i/n (Bổ sung).
11. Sóng dừng: cộng sóng tới u1 = A cos(ωt − 2πx/λ) và sóng phản xạ (tại đầu cố định đổi pha π, tại đầu tự do không đổi pha) → u = 2A sin(2πx/λ) sin(ωt) kiểu "biên độ chỉ phụ thuộc x, pha không truyền đi"; từ đó vị trí nút x = kλ/2, bụng x = (2k+1)λ/4, khoảng cách nút–nút = λ/2, nút–bụng = λ/4.
12. Điều kiện sóng dừng: hai đầu cố định ℓ = kλ/2 (số bụng = k, số nút = k+1); một đầu cố định một đầu tự do ℓ = (2k+1)λ/4 (số bụng = số nút = k+1).
13. Tần số nhạc cụ: dây đàn f = k·v/2ℓ (f0 = v/2ℓ), ống sáo f = (2k+1)·v/4ℓ (f0 = v/4ℓ).
14. Khoảng thời gian giữa hai lần sợi dây duỗi thẳng liên tiếp = T/2.
Với mỗi công thức PDF nêu không kèm chứng minh, vẫn phải chứng minh. Chỗ nào PDF không đủ cơ sở (ví dụ dấu của pha phản xạ) ghi rõ "Bổ sung".

BƯỚC 3 – Bài tập (PDF không có bài, nên sinh mới). Mỗi DẠNG gồm: nhận dạng, phương pháp 3–4 bước, 1 ví dụ mẫu giải đủ, rồi 6 bài tăng dần (2 cơ bản, 2 vận dụng, 1 DOK3, 1 Olympic), mỗi bài có Gợi ý 1 → Gợi ý 2 → Lời giải trong <details>, ghi mức độ và link ngược tới chứng minh. Các dạng:
D1. Đại lượng đặc trưng của sóng (λ, v, f, T, đếm đỉnh sóng, phao nhấp nhô).
D2. Viết phương trình sóng và tính li độ/vận tốc dao động của điểm cách nguồn d.
D3. Độ lệch pha, điểm cùng pha/ngược pha/vuông pha; số điểm cùng pha trên đoạn thẳng.
D4. Đồ thị sóng u–x và u–t; đọc A, λ, T, chiều truyền sóng; đồ thị hai thời điểm.
D5. Sóng điện từ: λ, f, v trong môi trường; thang sóng; bài về radar/siêu âm (tính khoảng cách từ thời gian phản hồi).
D6. Giao thoa sóng nước: biên độ tại một điểm, vị trí cực đại/cực tiểu, ĐẾM cực đại/cực tiểu trên S1S2, trên đường tròn/đường elip, điểm cực đại gần nguồn nhất, đường trung trực.
D7. Giao thoa Young: x, i, đếm vân sáng/tối trong trường giao thoa, vị trí trùng, đổi a/D/λ, thay môi trường, dùng đèn trắng (bài khó).
D8. Sóng dừng: sợi dây hai đầu cố định / một đầu tự do, đếm nút bụng, biên độ tại điểm cách nút x (A_M = A_bụng·|sin(2πx/λ)|), tốc độ truyền, f khi thay đổi lực căng.
D9. Nhạc cụ: dây đàn, ống sáo, họa âm bậc k, ống cộng hưởng (tìm v từ hai vị trí cộng hưởng liên tiếp).

QUY TẮC CHẤT LƯỢNG
- KaTeX ($...$, $$...$$), dấu thập phân kiểu Việt 0{,}5. Mọi đại lượng có đơn vị.
- Mọi đáp số tự kiểm bằng Python/sympy trước khi ghi; mô phỏng giao thoa/sóng dừng bằng numpy để kiểm các bài đếm cực trị.
- Hình vẽ bằng SVG hoặc matplotlib nhúng inline, có chú thích trục: đồ thị sóng, hệ vân hyperbol S1S2, sơ đồ Young, sóng dừng 2 loại đầu.
- Phần ngoài PDF ghi rõ "Bổ sung"; không bịa rồi gán cho PDF.
- Chạy thử bằng Playwright: không lỗi KaTeX/console, TOC và link chứng minh hoạt động, xem được ở khổ điện thoại; chụp 3 ảnh cho tôi duyệt.
- Báo cáo cuối: số chứng minh, số bài sinh thêm, chỗ không chắc.

Commit lên nhánh hiện tại, chưa mở PR.
```
