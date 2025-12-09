from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url, timeout=60000)

    def screenshot(self, path: str):
        self.page.screenshot(path=path)
