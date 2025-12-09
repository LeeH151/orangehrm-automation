## Tuần 1 (17/11 – 23/11)
* Công việc:
- Phân tích phạm vi, chọn ứng dụng mục tiêu (Web/API).
- Nghiên cứu Playwright cho Python.
- Thiết lập môi trường Python, Git/GitHub, Playwright và pytest.
- Thiết lập cấu hình môi trường (.env).
* Kết quả: 
- Tài liệu đề xuất phạm vi và ứng dụng.
- Cấu trúc dự án Playwright/Python khởi tạo.
- Thiết lập cấu hình API/Base URL và .env.
-----------------------------------------------
1. Chọn ứng dụng mục tiêu & viết tài liệu đề xuất phạm vi
1.1 Tiêu chí chọn ứng dụng mục tiêu
Chọn ứng dụng đáp ứng ít nhất các yêu cầu sau:
• Có giao diện Web (UI) có tính năng Login + CRUD (create/read/update/delete) hoặc danh sách + tìm kiếm/lọc.
• Có API (REST) công khai hoặc công ty cung cấp (cần endpoint cơ bản như /login, /users, /items).
• Có environmant test / sandbox hoặc bạn được phép sử dụng (quan trọng: không test mạnh trên hệ thống production).
• Có tài liệu API (Swagger/OpenAPI) càng tốt.
• Phù hợp phạm vi đồ án: không quá lớn, không quá nhỏ (vài module chính đủ để viết 25 – 40 testcases).
1.2 Ứng dụng mục tiêu
• Tên ứng dụng mục tiêu: OrangeHRM Demo (Hệ thống Quản lý Nhân sự)
• URL base (UI): https://opensource-demo.orangehrmlive.com/
• API base URL: Không áp dụng API nội bộ. (Sẽ sử dụng https://reqres.in/ để mô phỏng và kiểm thử API độc lập, sau đó 
dùng API Helper để hỗ trợ chuẩn bị dữ liệu test).
• Chức năng sẽ tự động hóa: 
   1. Đăng nhập/Đăng ký: Login và Logout (sử dụng tài khoản Admin mặc định). 
   2. CRUD đối tượng: Quản lý Nhân viên (Module PIM: Thêm/Sửa/Xóa Nhân viên). 
   3. Nghiệp vụ: Search, Filter, Pagination trên bảng danh sách nhân viên/người dùng.
• Lý do chọn:
   1. Mô hình Doanh nghiệp: Mô phỏng một ứng dụng quản trị (Admin Dashboard) phức tạp, lý tưởng để áp dụng Page Object 
Model (POM) chuyên nghiệp. 
   2. Đa dạng phần tử: Chứa đầy đủ các phần tử phức tạp như Dynamic Tables, Dropdowns, Date Pickers, File Upload (khi 
thêm ảnh nhân viên), phù hợp để luyện tập Playwright. 
   3. Ổn định: Trang demo công khai và ổn định, ít thay đổi.
• Rủi ro & phương án giảm thiểu: 
      - Rủi ro 1 (Thiếu API nội bộ): Ứng dụng này không cung cấp API công khai cho mục đích CRUD. Phương án: Sử dụng Reqres.in
      để triển khai các test case API độc lập (Tuần 6) và áp dụng kỹ thuật Hybrid E2E để chứng minh sự kết hợp của API Helper 
      trong việc chuẩn bị dữ liệu (Tuần 7). 
      - Rủi ro 2 (Dữ liệu chung): Dữ liệu có thể bị thay đổi bởi người dùng khác. 
      - Phương án: Thiết lập các test case để tạo dữ liệu mới hoàn toàn (ví dụ: Tên nhân viên ngẫu nhiên) và xóa dữ liệu đó 
      trong bước Teardown.
---------------------------------------------------
## Tuần 2 (24/11 – 30/11)
* 