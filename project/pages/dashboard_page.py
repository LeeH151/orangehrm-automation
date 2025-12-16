# project/pages/dashboard_page.py
from project.pages.base_page import BasePage


class DashboardPage(BasePage):
    URL = "http://localhost/orangehrm-5.8/web/index.php/dashboard/index"

    HEADER_DASHBOARD = "h6.oxd-text--h6"
    MENU_PIM = "text=PIM"
    MENU_ADMIN = "text=Admin"

    def is_dashboard_displayed(self) -> bool:
        self.page.wait_for_selector(self.HEADER_DASHBOARD)
        return "Dashboard" in self.page.text_content(self.HEADER_DASHBOARD)

    def go_to_pim(self):
        self.page.click(self.MENU_PIM)
        self.page.wait_for_load_state("networkidle")

    def go_to_admin(self):
        self.page.click(self.MENU_ADMIN)
        self.page.wait_for_load_state("networkidle")

'''from playwright.sync_api import Page, Locator
from base_page import BasePage
from data.test_data import TEST_DATA


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, TEST_DATA["urlPaths"]["dashboard"])

        self.search_box: Locator = page.get_by_placeholder("Search")
        self.user_dropdown: Locator = page.locator(".oxd-userdropdown")
        self.logout_button: Locator = page.get_by_text("Logout")
        self.sidebar_menu: Locator = page.locator(".oxd-sidepanel-body")
        self.menu_items: Locator = page.locator(".oxd-main-menu-item")

    def search_menu(self, search_term: str) -> None:
        self.fill(self.search_box, search_term)

    def get_visible_menu_items(self) -> list[str]:
        items = self.menu_items.all_text_contents()
        return [item for item in items if item.strip() != ""]

    def click_menu_item(self, menu_name: str) -> None:
        self.page.get_by_text(menu_name).click()

    def logout(self) -> None:
        self.click(self.user_dropdown)
        self.click(self.logout_button)

    def clear_search(self) -> None:
        self.search_box.clear()

    def is_menu_item_visible(self, menu_name: str) -> bool:
        return self.page.get_by_text(menu_name).is_visible()

    def verify_all_visible_items_contain(self, search_term: str) -> bool:
        items = self.get_visible_menu_items()
        return all(
            search_term.lower() in item.lower()
            for item in items
        )
'''