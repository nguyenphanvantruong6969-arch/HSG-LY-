---
description: Chuyển Chương 4 (Dòng điện, mạch điện) từ PDF sang HTML học tập có chứng minh và bài luyện
---
Làm theo `huong_dan/quy_trinh_pdf_to_html.md`. Nguồn: `tai_lieu_pdf/chuong3_4.pdf`, CHỈ trang 13–18. Đầu ra: `chuong4_dong_dien.html`. Nếu `chuong3_dien_truong.html` đã có, liên kết chéo tới điện thế và công lực điện.

Lưu ý PDF: trang 13 là truyện tranh (3 bóng đèn song song vào ắc quy 12 V: sáng như nhau, dòng nguồn gấp 3, điện trở tương đương còn 1/3): diễn giải thành ví dụ có số. "Bài tập minh hoạ" chỉ trỏ sách Giancoli, bỏ qua; trang 16 trỏ nhầm Example 17.8 cho mục Ôm, ghi chú. Khung "Nội dung chính" bị cắt chữ: không đoán. PDF không có ghép điện trở, ε = I(R+r), định luật Joule, bài tập: phần này là "Bổ sung" cần chứng minh đủ.

Cấu trúc: B22 cường độ dòng điện (I = Δq/Δt, I = Snve) → B23 điện trở, định luật Ôm (R = ρℓ/S) → B24 nguồn điện (ε = A/q, r) → B25 năng lượng và công suất (W = UIt, P = UI, H = U/ε).

Chứng minh bắt buộc (Ôm là định luật thực nghiệm: nêu điều kiện, giải thích vi mô):
1. I = Snve từ hình trụ h = vΔt; v = I/(Sne); tốc độ trôi dây đồng cỡ 10^−4 m/s, vì sao đèn sáng ngay.
2. Dòng trong dung dịch/khí: I = (|q+|n+v+ + |q−|n−v−)S (Bổ sung).
3. 1 A = 1 C/s ≈ 6,25·10^18 e/s.
4. R = ρℓ/S từ hai nhận xét ghép dây giống nhau (nối tiếp, song song).
5. R theo nhiệt độ: dây tóc tăng, thermistor giảm (Bổ sung, giải thích vi mô).
6. I = U/R: đồ thị I–U thẳng qua gốc; vì sao đèn dây tóc cong.
7. Ghép điện trở nối tiếp, song song (Bổ sung); kiểm lại truyện tranh.
8. ε = A/q: nguồn là "máy bơm điện tích".
9. U = ε − Ir; hở mạch, đoản mạch I = ε/r; I = ε/(R+r) từ bảo toàn năng lượng (Bổ sung).
10. W = qU = UIt; P = UI = I²R = U²/R; Q = I²Rt (Bổ sung); 1 kWh = 3,6·10^6 J.
11. A_ng = εIt, P_ng = εI; H = U/ε = R/(R+r).
12. P_max = ε²/4r khi R = r, H = 50% (Cô-si, Bổ sung).

Dạng bài (sinh mới): D1 I = Δq/Δt; D2 tốc độ trôi; D3 R = ρℓ/S, kéo dãn dây (R tăng k²); D4 Ôm, đồ thị I–U, bóng đèn, thermistor; D5 ghép điện trở, mạch hỗn hợp (Bổ sung); D6 nguồn ε, r, đồ thị U–I; D7 năng lượng, công suất, tiền điện, đun nước; D8 hiệu suất, công suất cực đại (R1R2 = r²); D9 tổng hợp: tụ nạp qua điện trở (nửa năng lượng nguồn thành nhiệt).
Hình cần vẽ: dây dẫn có hạt tải, sơ đồ mạch, đồ thị I–U, U–I của nguồn, P theo R.
