# tests/ui/test_login.py
import pytest


@pytest.mark.smoke
def test_01_dang_nhap_thanh_cong(login_page, users):
    """TC001 - Đăng nhập thành công"""
    admin = users["admin"]

    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(admin["username"], admin["password"])

    actual_url = login_page.page.url
    dashboard_title = login_page.page.text_content("h6.oxd-text--h6").strip()

    print("\n" + "═" * 70)
    print("                TC001 - ĐĂNG NHẬP THÀNH CÔNG")
    print("═" * 70)
    print(f"{'Tài khoản':<20} : {admin['username']}")
    print(f"{'Mật khẩu':<20} : {'*' * len(admin['password'])}")
    print(f"{'URL kỳ vọng':<20} : chứa 'dashboard'")
    print(f"{'URL thực tế':<20} : {actual_url}")
    print(f"{'Tiêu đề trang':<20} : {dashboard_title}")
    print(f"{'Kết quả':<20} : {'THÀNH CÔNG' if 'Dashboard' in dashboard_title else 'THẤT BẠI'}")
    print("═" * 70)

    assert "dashboard" in actual_url
    assert "Dashboard" in dashboard_title


@pytest.mark.negative
def test_02_dang_nhap_sai_mat_khau(login_page, users):
    """TC002 - Đăng nhập thất bại - Sai mật khẩu"""
    user = users["invalid_user"]

    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(user["username"], user["password"])
    error = login_page.get_error_message().strip()
    expected_error = "Invalid credentials"

    print("\n" + "═" * 70)
    print("             TC002 - ĐĂNG NHẬP THẤT BẠI (Sai thông tin)")
    print("═" * 70)
    print(f"{'Tài khoản thử':<23} : {user['username']}")
    print(f"{'Mật khẩu thử':<23} : {user['password']}")
    print(f"{'Thông báo mong đợi':<23} : {expected_error}")
    print(f"{'Thông báo thực tế':<23} : {error}")
    print(f"{'Kết quả kiểm tra':<23} : {'KHỚP' if expected_error in error else 'KHÔNG KHỚP'}")
    print("═" * 70)

    assert "Invalid credentials" in error


@pytest.mark.negative
def test_03_de_trong_tai_khoan_va_mat_khau(login_page):
    """TC003 - Đăng nhập thất bại - Để trống tài khoản/mật khẩu"""
    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    login_page.login(username="", password="")
    error = login_page.page.locator(".oxd-input-group__message").first.text_content().strip()
    expected_error = "Required"

    # In báo cáo ĐÚNG FORMAT NHƯ TC002
    print("\n" + "═" * 70)
    print("             TC003 - ĐĂNG NHẬP THẤT BẠI (Để trống)")
    print("═" * 70)
    print(f"{'Tài khoản thử':<23} : (trống)")
    print(f"{'Mật khẩu thử':<23} : (trống)")
    print(f"{'Thông báo mong đợi':<23} : {expected_error}")
    print(f"{'Thông báo thực tế':<23} : {error}")
    print(f"{'Kết quả kiểm tra':<23} : {'KHỚP' if expected_error == error else 'KHÔNG KHỚP'}")
    print("═" * 70)

    assert "Required" in error