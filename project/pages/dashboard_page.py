# project/pages/dashboard_page.py
from project.pages.base_page import BasePage


class DashboardPage(BasePage):
    URL = "http://localhost/orangehrm-5.8/web/index.php/dashboard/index"

    HEADER_DASHBOARD = "h6.oxd-text--h6"
    MENU_PIM = "text=PIM"
    MENU_ADMIN = "text=Admin"

    def is_dashboard_displayed(self) -> bool:
        """Kiểm tra đã vào Dashboard thành công"""
        return "Dashboard" in self.page.text_content(self.HEADER_DASHBOARD)

    def go_to_pim(self):
        self.page.get_by_text(self.MENU_PIM).click()
        self.page.wait_for_load_state("networkidle")