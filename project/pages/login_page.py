from project.pages.base_page import BasePage
from project.utils.helpers import fill_with_delay, click_with_delay
from project.config import settings

class LoginPage(BasePage):
    username_input = 'input[name="username"]'
    password_input = 'input[name="password"]'
    login_button = 'button[type="submit"]'
    error_msg = '.oxd-alert-content-text'

    def login(self, username, password):
        fill_with_delay(self.page, self.username_input, username, delay_ms=settings.DELAY_MS)
        fill_with_delay(self.page, self.password_input, password, delay_ms=settings.DELAY_MS)
        click_with_delay(self.page, self.login_button, delay_ms=settings.DELAY_MS)

    def get_error_message(self):
        return self.page.text_content(self.error_msg)
