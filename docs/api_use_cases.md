## API-UC01 – Cấp Token (Login API)
1. Mục tiêu
Lấy access_token hợp lệ để sử dụng cho tất cả các API yêu cầu xác thực.
2. Phương thức (Method)
POST
3. Endpoint
/oauth/issueToken
4. Header yêu cầu
Key	Value
Content-Type	application/json
5. Request Body
{
  "client_id": "admin",
  "client_secret": "admin123",
  "grant_type": "password"
}
6. Luồng chính (Main Flow)
Client gửi request với client_id và client_secret hợp lệ.
Server xác thực thông tin.
Server trả về access_token.
Client lưu token để sử dụng trong header Authorization cho các API khác.
7. Luồng phụ (Alternative / Error Flow)
Sai client_id → trả 401 Unauthorized.
Sai mật khẩu → trả 400 Bad Request.
Sai format body → 400.
Lỗi hệ thống → 500 Internal Server Error.
8. Response mong đợi
200 OK
{
  "access_token": "xxxxxx",
  "token_type": "Bearer",
  "expires_in": 3600
}
9. Điều kiện sau (Post-condition)
Access token hợp lệ được tạo và có thể được dùng cho các API yêu cầu quyền truy cập.
## API-UC02 – Lấy danh sách Employee
1. Mục tiêu
Lấy danh sách nhân viên hiện có trong hệ thống PIM.
2. Method
GET
3. Endpoint
/api/v2/pim/employees
4. Header yêu cầu
Key	Value
Authorization	Bearer <token>
Content-Type	application/json
5. Luồng chính
Client gửi request GET kèm token hợp lệ.
Server xác thực token.
Server truy vấn dữ liệu Employee.
Trả về danh sách employees.
6. Luồng phụ
Token hết hạn → 401 Unauthorized.
Token không hợp lệ → 403 Forbidden.
Không có dữ liệu → trả danh sách rỗng.
Lỗi truy vấn DB → 500 Internal Server Error.
7. Response mong đợi
200 OK
{
  "data": [
    {
      "employeeId": "001",
      "firstName": "John",
      "lastName": "Doe"
    }
  ]
}
8. Điều kiện sau
Danh sách Employee hiển thị đúng, đầy đủ và đúng định dạng.
## API-UC03 – Tạo Employee
1. Mục tiêu
Thêm mới một Employee vào hệ thống.
2. Method
POST
3. Endpoint
/api/v2/pim/employees
4. Header yêu cầu
Authorization: Bearer <token>
Content-Type: application/json
5. Request Body
{
  "firstName": "John",
  "lastName": "Doe"
}
6. Luồng chính
Client gửi POST với dữ liệu hợp lệ.
Server kiểm tra tính hợp lệ (firstname, lastname…).
Server ghi dữ liệu vào DB.
Server trả về thông tin Employee mới tạo.
7. Luồng phụ
Thiếu firstname → 400 Bad Request.
Token sai → 401 Unauthorized.
Trùng mã nhân viên (nếu có) → 409 Conflict.
8. Response mong đợi
201 Created
{
  "employeeId": "1234",
  "message": "Employee created successfully."
}
9. Điều kiện sau
Employee mới được thêm và hiển thị trong danh sách.
## API-UC04 – Cập nhật Employee
1. Mục tiêu
Cập nhật thông tin nhân viên theo ID.
2. Method
PUT
3. Endpoint
/api/v2/pim/employees/{id}
4. Header yêu cầu
Authorization: Bearer <token>
5. Request Body
{
  "firstName": "Michael",
  "lastName": "Smith"
}
6. Luồng chính
Client gửi PUT lên ID hợp lệ.
Server kiểm tra ID có tồn tại.
Server cập nhật thông tin.
Trả về kết quả thành công.
7. Luồng phụ
ID không tồn tại → 404 Not Found.
Token không hợp lệ → 401 Unauthorized.
Body sai format → 400 Bad Request.
8. Response mong đợi
200 OK
{
  "message": "Employee updated successfully."
}
9. Post-condition
Thông tin employee được cập nhật đúng trong hệ thống.
## API-UC05 – Xóa Employee
1. Mục tiêu
Xóa nhân viên bằng ID.
2. Method
DELETE
3. Endpoint
/api/v2/pim/employees/{id}
4. Header yêu cầu
Authorization: Bearer <token>
5. Luồng chính
Client gửi DELETE với ID hợp lệ.
Server xác thực quyền + token.
Server kiểm tra employeeId.
Nếu tồn tại → tiến hành xóa.
Trả về kết quả thành công.
6. Luồng phụ
ID không tồn tại → 404 Not Found.
Token sai/thiếu → 401 Unauthorized.
Không có quyền xóa → 403 Forbidden.
7. Response mong đợi
200 OK
{
  "message": "Employee deleted successfully."
}
8. Điều kiện sau
Employee bị xóa khỏi danh sách và không còn xuất hiện trong hệ thống.