from project.pages.base_page import BasePage

class AdminUserPage(BasePage):

    SEARCH_INPUT = "input[placeholder='Type for hints...']"
    SEARCH_BTN = "button[type='submit']"
    ADD_BTN = "button.oxd-button--secondary"
    TABLE = "div.oxd-table-body"

    def search_user(self, username):
        self.fill(self.SEARCH_INPUT, username)
        self.click(self.SEARCH_BTN)

    def click_add(self):
        self.click(self.ADD_BTN)

    def table_text(self):
        return self.get_text(self.TABLE)
