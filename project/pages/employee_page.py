from project.pages.base_page import BasePage

class EmployeePage(BasePage):

    PIM_MENU = "a[href='/web/index.php/pim/viewPimModule']"

    def goto_pim(self):
        self.click(self.PIM_MENU)
