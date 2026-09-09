# Vibe Hosting — Landing Page

Landing page giới thiệu giải pháp hosting **Vibe Hosting**, xây dựng bằng
**Python (Flask)**.

## Cấu trúc thư mục

```
vibe-hosting/
├── app.py                  # Flask app + toàn bộ nội dung trang
├── requirements.txt
├── templates/
│   └── index.html          # Template chính (Jinja2)
└── static/
    ├── css/style.css       # Toàn bộ style, không phụ thuộc framework CSS
    └── js/main.js          # Dựng equalizer "vibe meter" trong hero
```

## Cách chạy

1. (Khuyến nghị) tạo virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Cài thư viện:
   ```bash
   pip install -r requirements.txt
   ```

3. Chạy server:
   ```bash
   python app.py
   ```

4. Mở trình duyệt tại: **http://127.0.0.1:5000**

## Tuỳ chỉnh nội dung

Toàn bộ nội dung (số liệu, tính năng, bảng giá, đánh giá, footer...) nằm
trong các danh sách/dict ở đầu file `app.py` (`STATS`, `FEATURES`,
`DEPLOY_LOG`, `PRICING`, `TESTIMONIALS`, `FOOTER_LINKS`) — chỉnh trực tiếp
ở đó mà không cần đụng vào `index.html`.

Màu sắc & font chữ được khai báo dưới dạng CSS variables ở đầu file
`static/css/style.css` (mục `:root`), dễ đổi theo bộ nhận diện thương hiệu
nếu cần.

## Deploy lên production

Đây là bản demo dùng Flask dev server. Khi deploy thật, nên chạy qua
WSGI server như `gunicorn`:

```bash
pip install gunicorn
gunicorn app:app
```
