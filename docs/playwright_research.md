# Nghiên cứu về Playwright và pytest

## Playwright
Locator Strategy (role, get_by, nth…)
- Locator được dùng để xác định và tương tác với phần tử trên trang.
- Có thể tìm phần tử dựa trên role (button, textbox…), dựa vào text, thuộc tính, hoặc chọn phần tử theo vị trí (nth).
- Giúp code ổn định hơn so với dùng XPath/CSS thuần.
Page Object Model (POM)
- Là mô hình tổ chức mã giúp phân tách logic trang web khỏi mã test.
- Mỗi trang được đại diện bởi một class chứa các locator và hành động tương ứng.
- Giúp test dễ đọc, tái sử dụng, và bảo trì lâu dài.
Fixture structure (conftest.py)
- conftest.py chứa các fixture dùng chung trong dự án pytest.
- Fixture trong Playwright có thể dùng để khởi tạo trình duyệt, mở trang, hoặc chuẩn bị dữ liệu.
- Giảm trùng lặp mã, chuẩn hóa setup cho tất cả test.
Auto-waiting, retry và timeout
- Playwright tự động chờ phần tử sẵn sàng trước khi click, fill, hay đọc text → tránh lỗi timing.
- Cơ chế retry tự động trong nhiều hành động quan trọng.
- Cho phép đặt thời gian chờ (timeout) khi tương tác, điều hướng, hoặc chờ sự kiện.
Screenshot, Video recording
- Screenshot dùng để ghi nhận trạng thái giao diện khi test chạy hoặc khi test lỗi.
- Video recording ghi lại toàn bộ phiên chạy test, hỗ trợ phân tích lỗi và báo cáo.
Tracing & Debug mode
- Tracing lưu lại log, screenshot, timeline thao tác… để dễ dàng xem lại và tìm nguyên nhân lỗi.
- Debug mode cho phép dừng test, mở giao diện Inspector và xem từng bước thực thi.
Data-driven test với pytest
- Kiểm thử cùng một chức năng với nhiều bộ dữ liệu khác nhau.
- Giúp bao phủ nhiều trường hợp hơn với ít mã hơn.
- Thường kết hợp với parametrize để truyền dữ liệu vào hàm test.
## pytest
Fixtures
- Dùng để chuẩn bị môi trường hoặc dữ liệu cho test.
- Có thể tạo theo phạm vi test: function, class, module, session.
- Tự động chạy trước và sau mỗi test (setup/teardown).
Parametrize
- Cho phép chạy cùng một test nhiều lần với các bộ dữ liệu khác nhau.
- Giảm số lượng hàm test và tăng phạm vi kiểm thử.
Markers (smoke, regression…)
- Marker dùng để phân loại test như: smoke, regression, critical…
- Dễ dàng chạy nhóm test theo nhu cầu.
- Được khai báo trong pytest.ini để tránh cảnh báo.
Hooks (setup/teardown global)
- Là các hàm đặc biệt chạy tự động trước hoặc sau khi pytest thực thi toàn bộ test.
- Có thể dùng để khởi tạo tài nguyên chung (database, báo cáo…) hoặc dọn dẹp sau khi chạy.
Cấu hình pytest.ini
- Là file cấu hình chính của pytest.
- Dùng để khai báo markers, cấu hình plugin, quy định cách tìm test, và thiết lập tham số mặc định.
- Giúp đồng bộ cấu hình cho toàn dự án mà không cần viết lại trong từng file.

