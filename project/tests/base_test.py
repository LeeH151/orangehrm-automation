from project.utils.config import BASE_URL
from project.pages.login_page import LoginPage
from project.pages.dashboard_page import DashboardPage

class BaseTest:

    def login_as_admin(self, page, username, password):
        login_page = LoginPage(page)
        page.goto(BASE_URL)
        login_page.login(username, password)
        return DashboardPage(page)
