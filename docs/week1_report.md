git add .
git commit -m "Week 1 completed - Initial setup"
git push origin main

# Báo cáo tuần 1 - Xây dựng Hệ thống Automation Testing

## Mục tiêu tuần 1
- Phân tích phạm vi test (Web UI + API)
- Cài đặt môi trường và công cụ cần thiết.
- Xây dựng cấu trúc dự án Playwright cho Web UI và API.

## Công việc đã thực hiện
- **Phân tích phạm vi test**: Đã xác định các module cần test cho ứng dụng OrangeHRM bao gồm Login, Dashboard, Admin, PIM, và API (Login API, Employee API).
- **Nghiên cứu Playwright và pytest**: Đã nghiên cứu các kiến thức cơ bản về Playwright (Locator, POM, Fixtures, Screenshot) và pytest (Fixtures, Parametrize, Hooks).
- **Cài đặt công cụ**: Đã cài đặt Python, Playwright, pytest, Git và PyCharm trên hệ thống Windows.
- **Cấu trúc dự án**: Đã tạo cấu trúc thư mục dự án Playwright bao gồm các thư mục `tests`, `pages`, `api`, `utils`, `data`, `config`, và các file cấu hình như `.env`, `pytest.ini`.
- **Tạo file test đầu tiên**: Đã viết và chạy thử nghiệm đơn giản `test_smoke.py` để kiểm tra việc cấu hình môi trường.
- **Kết nối GitHub**: Đã tạo repository trên GitHub và kết nối với project local để quản lý phiên bản.

## Kế hoạch tuần 2
- Bắt đầu viết các test cases cho các module Web UI (Login, Admin, PIM) và API.
- Tiến hành tích hợp các test cho UI và API.
- Bắt đầu áp dụng các kỹ thuật kiểm thử nâng cao với Playwright như Data-driven testing và Parallel execution.

