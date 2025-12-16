from project.pages.base_page import BasePage
from project.utils.helpers import fill_with_delay, click_with_delay
from project.config import settings


class LoginPage(BasePage):
    # ================= SELECTORS =================
    username_input = 'input[name="username"]'
    password_input = 'input[name="password"]'
    login_button = 'button[type="submit"]'
    error_msg = '.oxd-alert-content-text'

    # User menu / logout
    user_dropdown = "li.oxd-userdropdown"
    logout_link = "a:has-text('Logout')"

    # ================= LOGIN =================
    def login(self, username, password):
        """Login vào hệ thống với username/password"""
        # Điền username với delay
        fill_with_delay(self.page, self.username_input, username, delay_ms=settings.DELAY_MS)

        # Điền password với delay
        fill_with_delay(self.page, self.password_input, password, delay_ms=settings.DELAY_MS)

        # Chờ và click nút đăng nhập
        self.page.wait_for_selector(self.login_button, timeout=5000)  # Chờ nút đăng nhập xuất hiện
        click_with_delay(self.page, self.login_button, delay_ms=settings.DELAY_MS)

    def get_error_message(self):
        """Lấy thông báo lỗi sau khi login thất bại"""
        # Chờ để đảm bảo thông báo lỗi đã xuất hiện
        self.page.wait_for_selector(self.error_msg, timeout=5000)
        return self.page.text_content(self.error_msg)

    # ================= LOGOUT =================
    def logout(self):
        """Đăng xuất khỏi hệ thống"""
        # Chờ menu user xuất hiện và click để mở
        self.page.wait_for_selector(self.user_dropdown, timeout=5000)
        self.page.click(self.user_dropdown)

        # Chờ và click logout link
        self.page.wait_for_selector(self.logout_link, timeout=5000)
        self.page.click(self.logout_link)

        # Chờ trang login xuất hiện để đảm bảo logout thành công
        self.page.wait_for_url("http://localhost/orangehrm-5.8/web/index.php/auth/login", timeout=5000)

        # Optional: Kiểm tra URL sau khi logout
        current_url = self.page.url
        if current_url != "http://localhost/orangehrm-5.8/web/index.php/auth/login":
            raise Exception(f"Đăng xuất thất bại, vẫn ở trang: {current_url}")
