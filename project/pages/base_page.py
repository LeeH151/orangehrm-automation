# project/pages/base_page.py
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url, timeout=60000)
        self.page.wait_for_load_state("networkidle")

    def wait_until_loaded(self):
        self.page.wait_for_load_state("networkidle")

    def take_screenshot(self, path: str):
        self.page.screenshot(path=path, full_page=True)

'''from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page, url: str = ""):
        self.page = page
        self.url = url

    def navigate(self) -> None:
        if self.url:
            self.page.goto(self.url)

    def wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def get_text(self, locator: Locator) -> str:
        return locator.text_content() or ""

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        locator.fill(text)

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def wait_for_element(self, locator: Locator) -> None:
        locator.wait_for(state="visible")

    def take_screenshot(self, name: str) -> None:
        self.page.screenshot(path=f"screenshots/{name}.png")
'''
