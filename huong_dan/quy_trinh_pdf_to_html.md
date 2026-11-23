# Quy trình chung: PDF → HTML học tập

Mẫu: `chuong1_dao_dong_dieu_hoa.html` (trên main). Mọi chương mới phải cùng cấu trúc, CSS, KaTeX và class với mẫu.

## Bước 0 – Đọc mẫu
Copy <head>/CSS/script của mẫu, không viết lại thư viện; chỉ viết <body> mới. Nắm các class: box quick/formula/tip/warn, proof (proof-head, pgoal, psteps, why, pcheck, pwrong), ex/hint/sol, details "Tự kiểm tra", TOC, "Tất cả chứng minh", "Bảng công thức", "Bài tập ôn luyện".

## Bước 1 – Trích xuất PDF (DỪNG chờ xác nhận)
Đọc từng trang (có hình thì nhìn hình). Gửi bảng ngắn: mục → công thức → định nghĩa → ví dụ → bài tập → hình, kèm số trang; liệt kê và đánh số mọi công thức. Chỗ đọc không chắc thì hỏi, không đoán. Chờ Truong xác nhận rồi mới viết HTML.

## Bước 2 – Viết HTML (mỗi lần một phần lớn)
Mỗi mục lý thuyết theo thứ tự: Hiểu nhanh 1 câu → giải thích bằng ví dụ đời thường → công thức trong khung formula kèm đơn vị → CHỨNG MINH ĐẦY ĐỦ → ví dụ mini có số → "Dễ sai" + "Mẹo nhớ" → "Tự kiểm tra" (details có đáp án).
Khối chứng minh: Cần chứng minh → Ý tưởng → các bước nhỏ (mỗi bước một phép biến đổi, có "vì sao") → kết luận \boxed{} → kiểm tra nhanh (đơn vị, trường hợp biên) → lập luận sai thường gặp → nguồn "PDF tr.X". Cấm "dễ thấy", "suy ra" khi chưa nêu phép biến đổi.
Phân biệt: định nghĩa / định luật thực nghiệm (không chứng minh được: nêu thí nghiệm gốc, thứ nguyên, điều kiện áp dụng) / hệ quả (chứng minh đầy đủ).
Cuối trang: "Tất cả chứng minh" (link), "Bảng công thức tổng hợp" (công thức + điều kiện + link chứng minh).

## Bước 3 – Bài tập theo dạng
Mỗi dạng: nhận dạng, phương pháp 3–4 bước, 1 ví dụ mẫu giải đủ, rồi 6 bài tăng dần (2 cơ bản, 2 vận dụng, 1 DOK3, 1 Olympic). Mỗi bài có Gợi ý 1 → Gợi ý 2 → Lời giải trong <details>, ghi mức độ và link ngược tới chứng minh. Bài trong PDF (nếu có) chuyển nguyên số liệu thành khối `ex`.

## Quy tắc chất lượng
- KaTeX, dấu thập phân kiểu Việt 0{,}5, mọi đại lượng có đơn vị.
- Mọi đáp số tự kiểm bằng Python/sympy/numpy trước khi ghi.
- Hình vẽ SVG hoặc matplotlib nhúng inline, có chú thích trục và đơn vị.
- Nội dung ngoài PDF ghi rõ "Bổ sung"; không gán cho PDF điều PDF không viết.
- Chạy thử bằng Playwright: không lỗi KaTeX/console, TOC và link hoạt động, đúng ở khổ điện thoại; chụp 3 ảnh để duyệt.
- Báo cáo cuối: số chứng minh, số bài sinh thêm, chỗ không chắc, lỗi PDF phát hiện.
- Commit lên nhánh hiện tại, chưa mở PR.
