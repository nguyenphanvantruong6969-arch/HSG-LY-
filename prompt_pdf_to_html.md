# Prompt: PDF → trang HTML học tập (chứng minh đầy đủ + bài luyện tập)

> Cách dùng: mở phiên Claude Code trong repo này, đính kèm (hoặc đặt vào thư mục repo) file PDF, rồi dán toàn bộ khối prompt bên dưới. Thay các chỗ trong `[...]`.

```text
Vai trò: bạn là giáo viên Vật lí HSG + kỹ sư tài liệu. Hãy biến tài liệu PDF [TÊN_FILE.pdf] (chương: [TÊN CHƯƠNG]) thành MỘT file HTML tự chứa để học, giống hệt cấu trúc và phong cách của file `chuong1_dao_dong_dieu_hoa.html` trên nhánh main.

BƯỚC 0 – Đọc mẫu (bắt buộc, làm trước khi viết)
- Đọc file mẫu trên main. KHÔNG sao chép nội dung vật lí; chỉ tái dùng: <head> (KaTeX + font nhúng sẵn), CSS, các class (box quick/formula/tip/warn, proof/proof-head/pgoal/psteps/why/pcheck/pwrong, ex/hint/sol, details "Tự kiểm tra"), cấu trúc TOC, mục "Tất cả chứng minh", "Bảng công thức", "Bài tập ôn luyện".
- Tạo file mới bằng cách copy phần <head>/CSS/script của mẫu, sau đó viết phần <body> mới. Không viết lại thư viện.

BƯỚC 1 – Trích xuất PDF (làm riêng, báo cáo trước khi viết HTML)
- Đọc từng trang PDF (có hình thì nhìn hình). Lập bảng: mục lớn → công thức → định nghĩa → ví dụ → bài tập → hình/đồ thị, kèm số trang.
- Liệt kê TẤT CẢ công thức/định luật xuất hiện, đánh số. Công thức nào PDF không chứng minh vẫn phải có chứng minh.
- Dừng lại, gửi cho tôi bảng này (ngắn gọn) và chờ tôi xác nhận rồi mới sang bước 2. Nếu có chỗ đọc không chắc (chữ mờ, hình khó), hỏi tôi, không đoán.

BƯỚC 2 – Viết HTML theo từng phần (mỗi lần 1 phần lớn, không viết cả file một lượt)
Mỗi mục lý thuyết gồm, theo thứ tự:
1. "Hiểu nhanh trong 1 câu".
2. Giải thích bằng hình ảnh/ví dụ đời thường, ngôn ngữ đơn giản, không nhảy bước.
3. Công thức trong khung `formula`, kèm ý nghĩa từng đại lượng và ĐƠN VỊ.
4. CHỨNG MINH ĐẦY ĐỦ cho từng công thức, dùng khối `proof` đánh số liên tục:
   - "Cần chứng minh" (viết công thức đích) → "Ý tưởng" (1–2 câu) → các bước nhỏ, mỗi bước một phép biến đổi, mỗi bước có "vì sao" → kết luận có \boxed{}.
   - Không được viết "dễ thấy", "suy ra" khi chưa nêu phép biến đổi. Nêu rõ định lí/đồng nhất thức đã dùng.
   - Kiểm tra nhanh (đơn vị, trường hợp biên, giới hạn) và "Lập luận sai thường gặp".
   - Ghi nguồn: "PDF tr.X".
5. Ví dụ mini có số liệu và tính ra kết quả.
6. Hộp "Dễ sai" (lỗi học sinh hay mắc) và "Mẹo nhớ".
7. Câu "Tự kiểm tra" dạng <details> có đáp án.
Cuối trang: mục "Tất cả chứng minh" (danh sách link tới từng proof), "Bảng công thức tổng hợp" (công thức + điều kiện dùng + link tới chứng minh).

BƯỚC 3 – Bài tập
A. Chuyển TOÀN BỘ bài tập trong PDF thành khối `ex`: đề (giữ nguyên số liệu), Gợi ý 1 → Gợi ý 2 → Lời giải (các cấp gợi ý tăng dần, lời giải chi tiết từng bước, có đơn vị và đáp số).
B. SINH BÀI MỚI theo DẠNG. Với mỗi dạng bài chính của chương:
   - Nêu "Dạng X: tên dạng", nhận dạng (dấu hiệu đề bài), phương pháp giải 3–4 bước, 1 ví dụ mẫu giải đầy đủ.
   - Sau đó 6 bài luyện tăng dần: 2 cơ bản → 2 vận dụng → 1 nâng cao (DOK3) → 1 kiểu Olympic. Mỗi bài có 2 gợi ý + lời giải. Số liệu khác bài trong PDF.
   - Đáp án/lời giải để trong <details>, không lộ sẵn.
   - Mỗi bài ghi mức độ và công thức/chứng minh liên quan (link ngược).

QUY TẮC CHẤT LƯỢNG
- Mọi công thức dùng KaTeX ($...$, $$...$$). Dấu thập phân kiểu Việt: 0{,}5.
- Mỗi bài giải phải được tự kiểm tra: tính lại bằng Python (hoặc sympy) và đối chiếu đáp số trước khi ghi vào file. Bài nào không khớp thì sửa.
- Đồ thị/hình: vẽ bằng SVG hoặc matplotlib nhúng inline, có chú thích trục và đơn vị.
- Không bịa nội dung không có trong PDF khi nói "PDF viết rằng"; phần bổ sung của bạn ghi rõ là "Bổ sung".
- Chạy thử trong trình duyệt (Playwright có sẵn): không lỗi KaTeX, không lỗi console, TOC và link proof hoạt động, mở được ở khổ điện thoại. Chụp ảnh 2–3 chỗ để tôi duyệt.
- Cuối cùng báo cáo: số chứng minh, số bài PDF, số bài sinh thêm, danh sách chỗ bạn không chắc.

Đầu ra: file `[ten_chuong].html` ở thư mục gốc repo, commit lên nhánh hiện tại. Chưa mở PR cho đến khi tôi yêu cầu.
```

## Ghi chú cho Truong
- File mẫu nặng khoảng 850 KB vì nhúng sẵn KaTeX và font; prompt yêu cầu tái dùng phần đó nên file mới sẽ không tốn công và đồng bộ giao diện.
- Có thể dùng thêm skill `chapter-exam-builder` (đã có trong PR #4) để sinh đề thi `.docx` từ chính nội dung này sau khi HTML xong.
