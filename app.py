"""
Vibe Hosting — Landing Page
----------------------------
Một website landing page giới thiệu giải pháp "Vibe Hosting",
xây dựng bằng Flask (Python).

Chạy thử:
    pip install -r requirements.txt
    python app.py

Sau đó mở trình duyệt tại: http://127.0.0.1:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Nội dung trang (tách riêng để dễ chỉnh sửa mà không đụng vào logic Flask)
# ---------------------------------------------------------------------------

STATS = [
    {"value": "99.99%", "label": "Uptime trung bình"},
    {"value": "<30s", "label": "Thời gian deploy"},
    {"value": "42+", "label": "Điểm edge toàn cầu"},
    {"value": "12,000+", "label": "Dự án đang chạy"},
]

FEATURES = [
    {
        "icon": "bolt",
        "title": "Deploy tức thì",
        "desc": "Chỉ cần \"git push\", Vibe Hosting build và lên sóng "
                "cho bạn trong chưa đầy 30 giây — không cấu hình rườm rà.",
    },
    {
        "icon": "globe",
        "title": "Edge network toàn cầu",
        "desc": "42+ điểm hiện diện trên khắp thế giới, nội dung luôn "
                "được phục vụ từ nơi gần người dùng của bạn nhất.",
    },
    {
        "icon": "lock",
        "title": "SSL & bảo mật tự động",
        "desc": "Chứng chỉ SSL, tường lửa và giám sát bất thường được "
                "bật mặc định trên mọi dự án, không phụ phí.",
    },
    {
        "icon": "scale",
        "title": "Auto-scaling theo thời gian thực",
        "desc": "Traffic tăng đột biến? Hạ tầng tự giãn nở theo, rồi "
                "tự thu lại khi hạ nhiệt. Bạn chỉ trả tiền cho phần dùng.",
    },
    {
        "icon": "terminal",
        "title": "Log & giám sát trực quan",
        "desc": "Theo dõi request, lỗi và hiệu năng theo thời gian thực "
                "ngay trong dashboard, không cần rời khỏi \"vibe\".",
    },
    {
        "icon": "rewind",
        "title": "Rollback tức thời",
        "desc": "Lỡ deploy hỏng? Quay lại phiên bản trước chỉ với một cú "
                "click, zero downtime, không ai kịp nhận ra.",
    },
]

DEPLOY_LOG = [
    {"t": "00:00", "line": "$ git push vibe main"},
    {"t": "00:02", "line": "▲ Đang build dự án..."},
    {"t": "00:11", "line": "✓ Build thành công (9.4s)"},
    {"t": "00:14", "line": "▲ Đang phân phối tới 42 edge nodes..."},
    {"t": "00:24", "line": "✓ Đã lên sóng toàn cầu"},
    {"t": "00:24", "line": "♪ vibe check: passed — 99.99% uptime"},
]

PRICING = [
    {
        "name": "Chill",
        "price": "0đ",
        "period": "/ tháng",
        "tagline": "Cho dự án cá nhân & thử nghiệm ý tưởng.",
        "features": [
            "1 dự án đang hoạt động",
            "Băng thông 50GB / tháng",
            "SSL tự động",
            "Cộng đồng hỗ trợ",
        ],
        "cta": "Bắt đầu miễn phí",
        "highlight": False,
    },
    {
        "name": "Flow",
        "price": "199.000đ",
        "period": "/ tháng",
        "tagline": "Cho sản phẩm đang tăng trưởng, cần độ ổn định cao.",
        "features": [
            "10 dự án đang hoạt động",
            "Băng thông 1TB / tháng",
            "Auto-scaling toàn phần",
            "Hỗ trợ ưu tiên trong 1 giờ",
            "Rollback không giới hạn",
        ],
        "cta": "Chọn gói Flow",
        "highlight": True,
    },
    {
        "name": "Studio",
        "price": "Liên hệ",
        "period": "",
        "tagline": "Cho đội nhóm & doanh nghiệp cần SLA riêng.",
        "features": [
            "Dự án không giới hạn",
            "Băng thông tuỳ chỉnh",
            "SLA & on-call riêng",
            "SSO & phân quyền theo team",
            "Quản lý tài khoản riêng",
        ],
        "cta": "Liên hệ đội ngũ",
        "highlight": False,
    },
]

TESTIMONIALS = [
    {
        "quote": "Chuyển qua Vibe Hosting xong thì team mình bớt hẳn "
                  "mấy buổi họp \"tại sao server sập\" lúc nửa đêm.",
        "name": "Minh Anh",
        "role": "Founder, phòng lab sản phẩm độc lập",
    },
    {
        "quote": "Cái dashboard log nhìn dễ chịu tới mức mình mở lên "
                  "kiểm tra còn nhiều hơn cả mạng xã hội.",
        "name": "Gia Bảo",
        "role": "Kỹ sư backend, ứng dụng đặt lịch",
    },
    {
        "quote": "Deploy 30 giây không phải marketing suông — mình bấm "
                  "giờ thật rồi, đúng là dưới nửa phút.",
        "name": "Thuỳ Trang",
        "role": "Freelance full-stack developer",
    },
]

FOOTER_LINKS = {
    "Sản phẩm": ["Tính năng", "Bảng giá", "Trạng thái hệ thống", "Đổi mới"],
    "Tài nguyên": ["Tài liệu", "Hướng dẫn deploy", "Blog kỹ thuật", "Cộng đồng"],
    "Công ty": ["Về chúng tôi", "Tuyển dụng", "Liên hệ", "Điều khoản"],
}


ICON_SVGS = {
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8"><path d="M12 2 4 14h6l-1 8 9-13h-6l1-7z" '
            'stroke-linejoin="round" stroke-linecap="round"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="1.8"><circle cx="12" cy="12" r="9"/>'
             '<path d="M3 12h18M12 3c2.8 2.6 4.2 5.7 4.2 9s-1.4 6.4-4.2 9'
             'c-2.8-2.6-4.2-5.7-4.2-9S9.2 5.6 12 3z"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8"><rect x="5" y="11" width="14" height="9" '
            'rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3" stroke-linecap="round"/>'
            '</svg>',
    "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
             '<path d="M12 3v18M7 7l-4 8a4 4 0 0 0 8 0l-4-8zM17 7l-4 8a4 4 0 0 0 8 0l-4-8z"/>'
             '<path d="M5 21h14M8 3h8"/></svg>',
    "terminal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
                '<rect x="3" y="4" width="18" height="16" rx="2"/>'
                '<path d="M7 9l3 3-3 3M13 15h4"/></svg>',
    "rewind": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
              '<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>',
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        stats=STATS,
        features=FEATURES,
        deploy_log=DEPLOY_LOG,
        pricing=PRICING,
        testimonials=TESTIMONIALS,
        footer_links=FOOTER_LINKS,
        icon_svgs=ICON_SVGS,
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
