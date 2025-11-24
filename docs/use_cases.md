Use Case UC01 – Login
- Tên Use Case: Login
- Mục tiêu: Cho phép người dùng truy cập vào Dashboard khi nhập đúng thông tin xác thực.
- Tác nhân: Admin/ Employee
- Điều kiện trước: 
  * Người dùng có tài khoản hợp lệ.
  * Truy cập được trang Login.
  * Hệ thống hoạt động bình thường.
- Luồng chính (Happy Flow):
  1. User mở trang Login
  2. Nhập username/password hợp lệ
  3. Nhấn Login
  4. Hệ thống điều hướng đến Dashboard
- Luồng phụ (Alternative Flow): 
  * Username hoặc password sai → hiển thị “Invalid credentials”.
  * Username/password bỏ trống → hiển thị “Required”.
  * Tài khoản bị khóa/disabled → hiển thị “Account disabled”.
  * Session timeout → yêu cầu login lại.
- Điều kiện sau: 
  * Dashboard hiển thị theo đúng quyền của user.
  * Phiên đăng nhập được tạo thành công.
-----------------------
Use Case UC02 - Logout
- Tên Use Case: Logout
- Mục tiêu: Cho phép người dùng thoát khỏi hệ thống an toàn.
- Tác nhân: Admin/ Employee
- Điều kiện trước: 
  * User đã đăng nhập thành công.
  * Icon avatar hiển thị đầy đủ.
- Luồng chính:
  1. User click vào icon avatar.
  2. Chọn Logout.
  3. Hệ thống xóa session.
  4. Chuyển về trang Login.
- Luồng phụ: 
  * Mất kết nối mạng → không logout được → hiển thị thông báo lỗi.
  * Server error → logout thất bại → yêu cầu thử lại.
- Điều kiện sau: 
  * Phiên đăng nhập bị hủy.
  * Hệ thống trở về màn hình Login.
-----------------------
Use Case UC03 - CRUD User Management
- Tên Use Case: CRUD User (Admin)
- Mục tiêu: Quản lý tài khoản người dùng (tạo, sửa, xóa) trong hệ thống.
- Tác nhân: Admin
- Điều kiện trước: 
  * Admin đã đăng nhập thành công.
  * Có quyền truy cập menu Admin → User Management.
  * Dữ liệu Roles và Employees load thành công.
- Luồng chính:
* Create User – Luồng chính
  1. Admin mở Admin → User Management.
  2. Nhấn Add.
  3. Nhập Role, Employee Name, Username, Status, Password.
  4. Nhấn Save.
  5. User mới xuất hiện trong danh sách.
* Update User – Luồng chính
  1. Admin user cần sửa.
  2. Nhấn Edit.
  3. Sửa thông tin theo yêu cầu.
  4. Nhấn Save.
  5. Dữ liệu được cập nhật.
* Delete User – Luồng chính
  1. Tick chọn user.
  2. Nhấn Delete.
  3. Xác nhân Yes.
  4. User bị xóa khỏi hệ thống.
- Luồng phụ: 
  * Username bị trùng → báo lỗi “Already exists”.
  * Password không hợp lệ → báo lỗi (min length, ký tự đặc biệt…).
  * Không tick user → không thể Delete.
  * Employee name không chính xác → không thể tạo user.
  * Không có quyền → hiển thị “Access Denied”.
- Điều kiện sau: 
  * Dữ liệu user được cập nhật chính xác và hiển thị đúng trong danh sách.
  * Hành động (create/update/delete) được lưu trong hệ thống.
-----------------------
Use Case 04 - CRUD Employee
- Tên Use Case: CRUD Employee
- Mục tiêu: Quản lý thông tin nhân viên trong hệ thống.
- Tác nhân: Admin
- Điều kiện trước: 
  * Admin đã đăng nhập vào hệ thống.
  * Admin có quyền truy cập module PIM (Employee Management).
  * Dữ liệu Employee tồn tại (đối với Update/Delete).
  * Kết nối mạng ổn định.
- Luồng chính:
* Create Employee – Luồng chính
  1. Admin vào PIM → Add Employee.
  2. Nhập Firstname, Lastname.
  3. Nhấn Save.
  4. Hệ thống tạo employee mới.
  5. Employee mới xuất hiện trong danh sách.
* Update Employee – Luồng chính
  1. Admin chọn Employee.
  2. Nhấn Edit.
  3. Sửa mục Personal Details.
  4. Nhấn Save.
  5. Hệ thống cập nhật thành công.
* Delete Employee – Luồng chính
  1. Admin tick chọn Employee.
  2. Nhấn Delete.
  3. Nhấn Comfirm.
  4. Employee bị xóa khỏi hệ thống.
- Luồng phụ: 
  * Firstname trống → báo lỗi “Required”.
  * Nhập ký tự số hoặc ký tự đặc biệt vào tên → báo lỗi validation.
  * Employee không tồn tại → không hiển thị trong list.
  * Không tick Employee → không thể Delete.
- Điều kiện sau: 
  * Employee được tạo/sửa/xóa đúng theo yêu cầu.
  * Danh sách Employee cập nhật theo dữ liệu mới nhất.
-----------------------
Use Case 05 - Search & Filter
- Tên Use Case: Search and Filter
- Mục tiêu: Cho phép Admin tìm kiếm hoặc lọc User/Employee theo nhiều điều kiện.
- Tác nhân: Admin 
- Điều kiện trước:
  * Admin đã login.
  * Module Admin hoặc PIM load thành công.
  * Form Search hiển thị đầy đủ
- Luồng chính: 
  1. Admin mở User List hoặc Employee List.
  2. Nhập điều kiện (Username, Role, Status, Name, ID,...)
  3. Nhấn Search.
  4. Hệ thống hiển thị danh sách khớp với filter.
- Luồng phụ:
  * Không có kết quả → hiển thị “No Records Found”.
  * Nhập ký tự không hợp lệ → validation message.
  * Để trống tất cả → nhận kết quả toàn bộ list.
- Điều kiện sau:
  * Danh sách hiển thị theo đúng tiêu chí tìm kiếm.
  * Bộ lọc được giữ nguyên sau khi load kết quả.
-----------------------
Use Case 06 - Pagination
- Tên Use Case: Pagination
- Mục tiêu: Kiểm tra khả năng phân trang trong danh sách User/Employee.
- Tác nhân: Admin
- Điều kiện trước:
  * Admin đã login.
  * Danh sách có >10 bản ghi.
  * Các nút Next, Prev, Page numbers hiển thị đầy đủ.
- Luồng chính:
  1. Admin mở danh sách User hoặc Employee.
  2. Nhấn Next hoặc Previous, hoặc chọn số trang.
  3. Hệ thống hiển thị trang tương ứng với dữ liệu đúng.
- Luồng phụ:
  * Ở trang 1 → nút Prev disabled.
  * Ở trang cuối → nút Next disabled.
  * Load dữ liệu chậm → hiển thị loading spinner.
  * Lỗi server → không đổi trang.
- Điều kiện sau:
  * Danh sách hiển thị đúng dữ liệu theo từng trang.
  * Không lặp dữ liệu giữa các trang.
  * Trạng thái pagination ổn định sau mỗi lần chuyển trang.