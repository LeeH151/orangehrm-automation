'''from .base_page import BasePage


class PIMPage(BasePage):
    URL = "http://localhost/orangehrm-5.8/web/index.php/pim/viewEmployeeList"

    # === TRANG DANH SÁCH ===
    BTN_ADD = "text=Add"
    SEARCH_EMPLOYEE_ID = "div.oxd-input-group:has-text('Employee Id') input.oxd-input"
    BTN_SEARCH = "button:has-text('Search')"

    # === FORM ADD / EDIT EMPLOYEE ===
    INPUT_FIRSTNAME = "input[name='firstName']"
    INPUT_MIDDLENAME = "input[name='middleName']"
    INPUT_LASTNAME = "input[name='lastName']"
    INPUT_EMPLOYEE_ID = "input >> nth=5"
    BTN_SAVE_BASIC = "button:has-text('Save') >> nth=0"

    # === PERSONAL DETAILS ===
    DROPDOWN_NATIONALITY = "div.oxd-select-text >> nth=0"
    DROPDOWN_MARITAL = "div.oxd-select-text >> nth=1"
    INPUT_DOB = "input[placeholder='yyyy-mm-dd']"
    RADIO_MALE = "label:has-text('Male')"
    BTN_SAVE_PERSONAL = "button.oxd-button--secondary:has-text('Save')"

    # === TABLE ===
    TABLE_FIRST_ROW = "div.oxd-table-card:first-child"
    TABLE_ROWS = "div.oxd-table-card"
    BTN_EDIT = f"{TABLE_FIRST_ROW} i.bi-pencil-fill"
    BTN_DELETE = f"{TABLE_FIRST_ROW} i.bi-trash"
    BTN_CONFIRM_DELETE = "button:has-text('Yes, Delete')"

    # === SEARCH RESULT ===
    RESULT_COUNT = "span:has-text('Record')"

    # === ERROR MESSAGES ===
    ERROR_FIRSTNAME = "div.oxd-input-group:has(input[name='firstName']) span.oxd-input-field-error-message"
    ERROR_LASTNAME = "div.oxd-input-group:has(input[name='lastName']) span.oxd-input-field-error-message"

    # ================= TOAST =================
    TOAST_CONTAINER = "div.oxd-toast-container--toast"
    TOAST_TITLE = ".oxd-text--toast-title"
    TOAST_MESSAGE = ".oxd-text--toast-message"

    # ================= NAVIGATE =================
    def go_to_pim(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.TABLE_FIRST_ROW).wait_for(state="attached", timeout=10000)

    # ================= ADD EMPLOYEE =================
    def click_add_employee(self):
        self.page.click(self.BTN_ADD)
        self.page.wait_for_selector(self.INPUT_FIRSTNAME, timeout=20000)

    def fill_basic_info(self, data):
        self.page.fill(self.INPUT_FIRSTNAME, data["firstName"])
        self.page.fill(self.INPUT_MIDDLENAME, data.get("middleName", ""))
        self.page.fill(self.INPUT_LASTNAME, data["lastName"])
        self.page.fill(self.INPUT_EMPLOYEE_ID, data["employeeId"])

    def save_basic_and_go_to_personal(self):
        self.page.click(self.BTN_SAVE_BASIC)
        return self.get_toast_success_message(timeout=10000)

    def fill_personal_details(self):
        self.page.click(self.DROPDOWN_NATIONALITY)
        self.page.click("div.oxd-select-option span:has-text('Vietnamese')")

        self.page.click(self.DROPDOWN_MARITAL)
        self.page.click("div.oxd-select-option span:has-text('Single')")

        self.page.fill(self.INPUT_DOB, "1990-01-01")
        self.page.click(self.RADIO_MALE)

        self.page.click(self.BTN_SAVE_PERSONAL)
        return self.get_toast_success_message(timeout=10000)

    def add_employee_complete(self, data):
        self.click_add_employee()
        self.fill_basic_info(data)
        toast_add = self.save_basic_and_go_to_personal()
        toast_personal = self.fill_personal_details()
        return toast_add, toast_personal

    # ================= SEARCH =================
    def search_by_id(self, emp_id):
        self.page.fill(self.SEARCH_EMPLOYEE_ID, emp_id)
        self.page.click(self.BTN_SEARCH)
        self.page.locator(self.TABLE_FIRST_ROW).wait_for(state="visible", timeout=10000)

    # ================= HELPER =================
    def clear_and_fill(self, selector, value):
        """
        Click vào input, xóa hết nội dung và fill giá trị mới
        """
        el = self.page.locator(selector)
        el.click()
        el.press("Control+A")
        el.press("Backspace")
        el.fill(value)

    # ================= EDIT EMPLOYEE =================
    def edit_employee(self, emp_id: str, new_first: str, new_last: str, new_middle: str = ""):
        """
        Chỉnh sửa thông tin nhân viên:
        1. Search theo employee id
        2. Click edit
        3. Clear & fill tên mới
        4. Save
        5. Capture toast
        """
        # Step 1: Search
        self.search_by_id(emp_id)

        # Step 2: Click Edit
        first_row = self.page.locator(self.TABLE_ROWS).first
        first_row.hover()
        first_row.locator("i.bi-pencil-fill").click()

        # Step 3: Clear & Update info
        self.page.wait_for_selector(self.INPUT_FIRSTNAME, timeout=30000)
        self.clear_and_fill(self.INPUT_FIRSTNAME, new_first)
        self.clear_and_fill(self.INPUT_MIDDLENAME, new_middle)
        self.clear_and_fill(self.INPUT_LASTNAME, new_last)

        # Step 4: Save
        self.page.click(self.BTN_SAVE_BASIC)

        # Step 5: Capture toast
        self.page.wait_for_selector(self.TOAST_CONTAINER, timeout=10000)
        toast = self.page.locator(self.TOAST_CONTAINER)
        toast_title = toast.locator(self.TOAST_TITLE).inner_text().strip()
        toast_message = toast.locator(self.TOAST_MESSAGE).inner_text().strip()

        # Step 6: Wait toast disappears
        self.page.locator(self.TOAST_CONTAINER).wait_for(state="detached", timeout=5000)

        return toast_title, toast_message

    # ================= DELETE =================
    def delete_first_employee(self):
        self.page.hover(self.TABLE_FIRST_ROW)
        self.page.click(self.BTN_DELETE)
        self.page.click(self.BTN_CONFIRM_DELETE)
        return self.get_toast_success_message(timeout=8000)

    # ================= RESULTS =================
    def get_result_count(self):
        return self.page.text_content(self.RESULT_COUNT)

    # ================= TOAST MESSAGES =================
    def get_toast(self, timeout=5000):
        try:
            self.page.wait_for_selector("div.oxd-toast-container--toast", timeout=timeout)
            toast = self.page.locator("div.oxd-toast-container--toast")
            title = toast.locator(".oxd-text--toast-title").text_content().strip()
            message = toast.locator(".oxd-text--toast-message").text_content().strip()
            return title, message
        except Exception:
            return "", ""

    def get_toast_success_message(self, timeout=5000):
        return self.get_toast(timeout)

    def get_toast_error_message(self, timeout=5000):
        return self.get_toast(timeout)

    # ================= CHECK DIALOG =================
    def check_delete_dialog_content(self):
        # Wait for the modal (dialog) to be visible
        dialog = self.page.locator(".oxd-dialog-sheet")
        dialog.wait_for(state="visible", timeout=5000)

        # Check title and message in the dialog
        dialog_title = dialog.locator(".oxd-text--card-title").text_content().strip()
        dialog_message = dialog.locator(".oxd-text--card-body").text_content().strip()

        # Expected content
        expected_title = "Are you Sure?"
        expected_message = "The selected record will be permanently deleted. Are you sure you want to continue?"

        # Return both actual content
        return dialog_title, dialog_message, expected_title, expected_message

    # ================= TOAST =================
    def get_toast_success_message(self, timeout=5000):
        self.page.wait_for_selector(self.TOAST_CONTAINER, timeout=timeout)
        toast = self.page.locator(self.TOAST_CONTAINER)
        title = toast.locator(self.TOAST_TITLE).text_content().strip()
        message = toast.locator(self.TOAST_MESSAGE).text_content().strip()
        return title, message'''
from .base_page import BasePage


class PIMPage(BasePage):
    URL = "http://localhost/orangehrm-5.8/web/index.php/pim/viewEmployeeList"

    # ================= TRANG DANH SÁCH =================
    BTN_ADD = "text=Add"
    SEARCH_EMPLOYEE_ID = "div.oxd-input-group:has-text('Employee Id') input.oxd-input"
    BTN_SEARCH = "button:has-text('Search')"

    TABLE_FIRST_ROW = "div.oxd-table-card:first-child"
    TABLE_ROWS = "div.oxd-table-card"
    BTN_EDIT = f"{TABLE_FIRST_ROW} i.bi-pencil-fill"
    BTN_DELETE = f"{TABLE_FIRST_ROW} i.bi-trash"
    BTN_CONFIRM_DELETE = "button:has-text('Yes, Delete')"
    RESULT_COUNT = "span:has-text('Record')"

    # ================= FORM ADD / EDIT =================
    INPUT_FIRSTNAME = "input[name='firstName']"
    INPUT_MIDDLENAME = "input[name='middleName']"
    INPUT_LASTNAME = "input[name='lastName']"
    INPUT_EMPLOYEE_ID = "input >> nth=5"
    BTN_SAVE_BASIC = "button:has-text('Save') >> nth=0"

    # ================= PERSONAL DETAILS =================
    DROPDOWN_NATIONALITY = "div.oxd-select-text >> nth=0"
    DROPDOWN_MARITAL = "div.oxd-select-text >> nth=1"
    INPUT_DOB = "input[placeholder='yyyy-mm-dd']"
    RADIO_MALE = "label:has-text('Male')"
    BTN_SAVE_PERSONAL = "button.oxd-button--secondary:has-text('Save')"

    # ================= ERROR MESSAGES =================
    ERROR_FIRSTNAME = "div.oxd-input-group:has(input[name='firstName']) span.oxd-input-field-error-message"
    ERROR_LASTNAME = "div.oxd-input-group:has(input[name='lastName']) span.oxd-input-field-error-message"

    # ================= TOAST =================
    TOAST_CONTAINER = "div.oxd-toast-container--toast"
    TOAST_TITLE = ".oxd-text--toast-title"
    TOAST_MESSAGE = ".oxd-text--toast-message"

    # ================= NAVIGATION =================
    def go_to_pim(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.TABLE_FIRST_ROW).wait_for(state="attached", timeout=10000)

    # ================= ADD EMPLOYEE =================
    def click_add_employee(self):
        self.page.click(self.BTN_ADD)
        self.page.wait_for_selector(self.INPUT_FIRSTNAME, timeout=20000)

    def fill_basic_info(self, data):
        self.page.fill(self.INPUT_FIRSTNAME, data["firstName"])
        self.page.fill(self.INPUT_MIDDLENAME, data.get("middleName", ""))
        self.page.fill(self.INPUT_LASTNAME, data["lastName"])
        self.page.fill(self.INPUT_EMPLOYEE_ID, data["employeeId"])

    def save_basic_and_go_to_personal(self):
        self.page.click(self.BTN_SAVE_BASIC)
        return self.get_toast_success_message(timeout=10000)

    def fill_personal_details(self):
        self.page.click(self.DROPDOWN_NATIONALITY)
        self.page.click("div.oxd-select-option span:has-text('Vietnamese')")

        self.page.click(self.DROPDOWN_MARITAL)
        self.page.click("div.oxd-select-option span:has-text('Single')")

        self.page.fill(self.INPUT_DOB, "1990-01-01")
        self.page.click(self.RADIO_MALE)
        self.page.click(self.BTN_SAVE_PERSONAL)
        return self.get_toast_success_message(timeout=10000)

    def add_employee_complete(self, data):
        self.click_add_employee()
        self.fill_basic_info(data)
        toast_basic = self.save_basic_and_go_to_personal()
        toast_personal = self.fill_personal_details()
        return toast_basic, toast_personal

    # ================= SEARCH =================
    def search_by_id(self, emp_id):
        self.page.fill(self.SEARCH_EMPLOYEE_ID, emp_id)
        self.page.click(self.BTN_SEARCH)
        self.page.locator(self.TABLE_FIRST_ROW).wait_for(state="visible", timeout=10000)

    # ================= HELPER =================
    def clear_and_fill(self, selector, value):
        """
        Xóa nội dung input và điền giá trị mới
        """
        el = self.page.locator(selector)
        el.click()
        el.press("Control+A")
        el.press("Backspace")
        el.fill(value)

    # ================= EDIT EMPLOYEE =================
    def edit_employee(self, emp_id, new_first, new_last, new_middle=""):
        """
        Chỉnh sửa thông tin nhân viên
        """
        self.search_by_id(emp_id)
        first_row = self.page.locator(self.TABLE_ROWS).first
        first_row.hover()
        first_row.locator("i.bi-pencil-fill").click()

        self.page.wait_for_selector(self.INPUT_FIRSTNAME, timeout=30000)
        self.clear_and_fill(self.INPUT_FIRSTNAME, new_first)
        self.clear_and_fill(self.INPUT_MIDDLENAME, new_middle)
        self.clear_and_fill(self.INPUT_LASTNAME, new_last)

        self.page.click(self.BTN_SAVE_BASIC)

        # Capture toast
        self.page.wait_for_selector(self.TOAST_CONTAINER, timeout=10000)
        toast = self.page.locator(self.TOAST_CONTAINER)
        toast_title = toast.locator(self.TOAST_TITLE).inner_text().strip()
        toast_message = toast.locator(self.TOAST_MESSAGE).inner_text().strip()
        self.page.locator(self.TOAST_CONTAINER).wait_for(state="detached", timeout=5000)

        return toast_title, toast_message

    # ================= DELETE =================
    def delete_first_employee(self):
        self.page.hover(self.TABLE_FIRST_ROW)
        self.page.click(self.BTN_DELETE)
        self.page.click(self.BTN_CONFIRM_DELETE)
        return self.get_toast_success_message(timeout=8000)

    # ================= RESULTS =================
    def get_result_count(self):
        return self.page.text_content(self.RESULT_COUNT)

    # ================= TOAST =================
    def get_toast(self, timeout=5000):
        try:
            self.page.wait_for_selector(self.TOAST_CONTAINER, timeout=timeout)
            toast = self.page.locator(self.TOAST_CONTAINER)
            title = toast.locator(self.TOAST_TITLE).text_content().strip()
            message = toast.locator(self.TOAST_MESSAGE).text_content().strip()
            return title, message
        except Exception:
            return "", ""

    def get_toast_success_message(self, timeout=5000):
        return self.get_toast(timeout)

    def get_toast_error_message(self, timeout=5000):
        return self.get_toast(timeout)

    # ================= CHECK DELETE DIALOG =================
    def check_delete_dialog_content(self):
        dialog = self.page.locator(".oxd-dialog-sheet")
        dialog.wait_for(state="visible", timeout=5000)

        dialog_title = dialog.locator(".oxd-text--card-title").text_content().strip()
        dialog_message = dialog.locator(".oxd-text--card-body").text_content().strip()

        expected_title = "Are you Sure?"
        expected_message = "The selected record will be permanently deleted. Are you sure you want to continue?"

        return dialog_title, dialog_message, expected_title, expected_message
