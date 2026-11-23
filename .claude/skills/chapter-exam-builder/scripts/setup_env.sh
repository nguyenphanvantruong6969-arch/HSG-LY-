#!/usr/bin/env bash
# Cai cong cu can thiet. An toan khi chay lai. Can quyen root cho apt-get.
set -e
python3 -m pip install -q python-docx lxml matplotlib numpy sympy pillow 2>&1 | tail -1 || true
command -v pandoc >/dev/null || apt-get install -y pandoc
command -v soffice >/dev/null || apt-get install -y libreoffice-writer
command -v pdftoppm >/dev/null || apt-get install -y poppler-utils
# libreoffice-math: bat buoc de XEM TRUOC cong thuc (khong co thi cong thuc bi trong khi chuyen sang PDF)
if ! dpkg -l 2>/dev/null | grep -q '^ii  libreoffice-math'; then
  apt-get update -qq && apt-get install -y libreoffice-math
fi
echo "OK: pandoc=$(pandoc --version | head -1) soffice=$(command -v soffice)"
