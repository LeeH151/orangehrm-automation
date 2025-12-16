import pytest

# =======================
# Login thành công
# =======================
@pytest.mark.smoke
def test_login_success(login_page, users):
    admin = users["admin"]

    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(admin["username"], admin["password"])

    actual_url = login_page.page.url
    dashboard_title = login_page.page.text_content("h6.oxd-text--h6").strip()

    print("\n" + "═" * 90)
    print("         TC001 - ĐĂNG NHẬP THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Tài khoản':<20} : {admin['username']}")
    print(f"{'Mật khẩu':<20} : {'*' * len(admin['password'])}")
    print(f"{'URL kỳ vọng':<20} : chứa 'dashboard'")
    print(f"{'URL thực tế':<20} : {actual_url}")
    print(f"{'Tiêu đề trang':<20} : {dashboard_title}")
    print(f"{'Kết quả':<20} : {'THÀNH CÔNG' if 'Dashboard' in dashboard_title else 'THẤT BẠI'}")
    print("═" * 90)

    assert "dashboard" in actual_url, f"Expected 'dashboard' in URL, but got {actual_url}"
    assert "Dashboard" in dashboard_title, f"Expected 'Dashboard' in page title, but got {dashboard_title}"

# =======================
# Login thất bại - Sai mật khẩu
# =======================
@pytest.mark.negative
def test_login_invalid_password(login_page, users):
    user = users["invalid_password"]

    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(user["username"], user["password"])

    error = login_page.get_error_message().strip()
    expected_error = "Invalid credentials"

    print("\n" + "═" * 90)
    print("         TC002 - ĐĂNG NHẬP THẤT BẠI (Sai mật khẩu)")
    print("═" * 90)
    print(f"{'Tài khoản thử':<23} : {user['username']}")
    print(f"{'Mật khẩu thử':<23} : {user['password']}")
    print(f"{'Thông báo mong đợi':<23} : {expected_error}")
    print(f"{'Thông báo thực tế':<23} : {error}")
    print(f"{'Kết quả kiểm tra':<23} : {'KHỚP' if expected_error in error else 'KHÔNG KHỚP'}")
    print("═" * 90)

    assert "Invalid credentials" in error, f"Expected 'Invalid credentials' error, but got {error}"

# =======================
# Login thất bại - Username trống
# =======================
@pytest.mark.negative
def test_login_empty_username(login_page, users):
    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(users["empty_username"]["username"], users["empty_username"]["password"])

    # Lấy thông báo dưới input username
    actual_error = login_page.page.locator(".oxd-input-group__message").first.text_content().strip()
    expected_error = "Required"

    print("\n" + "═" * 90)
    print("         TC003 - ĐĂNG NHẬP THẤT BẠI (Username trống)")
    print("═" * 90)
    print(f"{'Tài khoản thử':<23} : (trống)")
    print(f"{'Mật khẩu thử':<23} : {users['empty_username']['password']}")
    print(f"{'Thông báo mong đợi':<23} : {expected_error}")
    print(f"{'Thông báo thực tế':<23} : {actual_error}")
    print(f"{'Kết quả kiểm tra':<23} : {'KHỚP' if expected_error == actual_error else 'KHÔNG KHỚP'}")
    print("═" * 90)

    assert expected_error == actual_error, f"Expected '{expected_error}', but got '{actual_error}'"

# =======================
# Login thất bại - Password trống
# =======================
@pytest.mark.negative
def test_login_empty_password(login_page, users):
    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(users["empty_password"]["username"], users["empty_password"]["password"])

    # Lấy thông báo dưới input password
    actual_error = login_page.page.locator(".oxd-input-field-error-message").text_content().strip()
    expected_error = "Required"

    print("\n" + "═" * 90)
    print("         TC004 - ĐĂNG NHẬP THẤT BẠI (Password trống)")
    print("═" * 90)
    print(f"{'Tài khoản thử':<23} : {users['empty_password']['username']}")
    print(f"{'Mật khẩu thử':<23} : (trống)")
    print(f"{'Thông báo mong đợi':<23} : {expected_error}")
    print(f"{'Thông báo thực tế':<23} : {actual_error}")
    print(f"{'Kết quả kiểm tra':<23} : {'KHỚP' if expected_error == actual_error else 'KHÔNG KHỚP'}")
    print("═" * 90)

    # Kiểm tra thông báo lỗi "Required"
    assert expected_error == actual_error, f"Expected '{expected_error}', but got '{actual_error}'"

@pytest.mark.smoke
def test_login_case_sensitive_success(login_page, users):
    # Thực hiện đăng nhập
    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(users["uppercase_username"]["username"], users["uppercase_username"]["password"])

    # Kiểm tra URL sau khi đăng nhập
    actual_url = login_page.page.url
    dashboard_title = login_page.page.text_content("h6.oxd-text--h6").strip()

    # In ra kết quả kiểm thử
    print("\n" + "═" * 90)
    print("         TC005 - ĐĂNG NHẬP THÀNH CÔNG (Không phân biệt chữ hoa/thường)")
    print("═" * 90)
    print(f"{'Tài khoản thử':<23} : {users['uppercase_username']['username']}")
    print(f"{'Mật khẩu thử':<23} : {'*' * len(users['uppercase_username']['password'])}")
    print(f"{'URL kỳ vọng':<23} : chứa 'dashboard'")
    print(f"{'URL thực tế':<23} : {actual_url}")
    print(f"{'Tiêu đề trang':<23} : {dashboard_title}")
    print(f"{'Kết quả kiểm tra':<23} : {'THÀNH CÔNG' if 'Dashboard' in dashboard_title else 'THẤT BẠI'}")
    print("═" * 90)

    # Kiểm tra URL có chứa 'dashboard' và tiêu đề có 'Dashboard'
    assert "dashboard" in actual_url, f"Expected URL to contain 'dashboard', but got '{actual_url}'"
    assert "Dashboard" in dashboard_title, f"Expected page title to contain 'Dashboard', but got '{dashboard_title}'"

# =======================
# Login thành công - Kiểm tra logout
# =======================
@pytest.mark.smoke
def test_logout_success(login_page, users):
    # Đăng nhập trước khi logout
    admin = users["admin"]
    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(admin["username"], admin["password"])

    # Tiến hành logout
    login_page.logout()

    # Kiểm tra sau khi logout, người dùng có được chuyển hướng về trang đăng nhập hay không
    login_page_url = login_page.page.url
    expected_url = "http://localhost/orangehrm-5.8/web/index.php/auth/login"

    print("\n" + "═" * 90)
    print("         TC006 - ĐĂNG XUẤT THÀNH CÔNG")
    print("═" * 90)
    print(f"{'URL kỳ vọng':<23} : {expected_url}")
    print(f"{'URL thực tế':<23} : {login_page_url}")
    print(f"{'Kết quả kiểm tra':<23} : {'KHỚP' if expected_url in login_page_url else 'KHÔNG KHỚP'}")
    print("═" * 90)

    assert expected_url in login_page_url, f"Expected '{expected_url}', but got '{login_page_url}'"
