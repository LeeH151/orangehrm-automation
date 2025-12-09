from project.tests.base_test import BaseTest
from project.utils.config import ADMIN_USER, ADMIN_PASS
from project.pages.admin_user_page import AdminUserPage

class TestAdminUser(BaseTest):

    def test_admin_search_user(self, page):
        dashboard = self.login_as_admin(page, ADMIN_USER, ADMIN_PASS)
        dashboard.goto_admin()

        admin_page = AdminUserPage(page)
        admin_page.search_user("Admin")

        table = admin_page.table_text()

        assert "Admin" in table
