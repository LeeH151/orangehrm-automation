# tests/ui/test_pim_crud.py
import pytest
import time
from project.pages.pim_page import PIMPage


# =====================================================================
# ===============         TC: ADD MULTIPLE EMPLOYEES      ==============
# =====================================================================
def test_add_multiple_employees(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    employees_list = employee_data.get("employees", [])

    for employee in employees_list:
        pim.go_to_pim()
        pim.add_employee_complete(employee)

        title, message = pim.get_toast_success_message()

        print("\n" + "═" * 90)
        print(
            f"        THÊM NHÂN VIÊN - {employee['firstName']} {employee.get('middleName', '')} {employee['lastName']}")
        print("═" * 90)
        print(f"{'Employee ID':<40} : {employee['employeeId']}")
        print(f"{'Kết quả thực tế':<40} : {title} - {message}")
        print("═" * 90)

        assert title == "Success"
        assert message == "Successfully Saved" or message == "Successfully Updated"


# =====================================================================
# ===============       TC_PIM_001 - ADD EMPLOYEE SUCCESS =============
# =====================================================================
@pytest.mark.pim
def test_add_employee_success(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    data = employee_data["valid_employee"]

    pim.go_to_pim()
    toast_add, toast_personal = pim.add_employee_complete(data)

    title_add, msg_add = toast_add
    title_per, msg_per = toast_personal

    expected_add = "Successfully Saved"
    expected_personal = "Successfully Updated"

    # ==== Xác định trạng thái ====
    status_add = "KẾT QUẢ KHỚP ✅" if msg_add == expected_add else "KẾT QUẢ KHÔNG KHỚP ❌"
    status_personal = "KẾT QUẢ KHỚP ✅" if msg_per == expected_personal else "KẾT QUẢ KHÔNG KHỚP ❌"

    # ==== Log đẹp ====
    print("\n" + "═" * 95)
    print("        TC_PIM_001 - THÊM NHÂN VIÊN THÀNH CÔNG")
    print("═" * 95)

    print(f"{'Họ và tên':<40} : {data['firstName']} {data.get('middleName', '')} {data['lastName']}")
    print(f"{'Employee ID':<40} : {data['employeeId']}")
    print("─" * 95)

    print(f"{'Kết quả mong đợi - Add Employee':<40} : {expected_add}")
    print(f"{'Kết quả thực tế - Add Employee':<40} : {msg_add}")
    print(f"{'Trạng thái kiểm tra - Add Employee':<40} : {status_add}")
    print("─" * 95)

    print(f"{'Kết quả mong đợi - Personal Details':<40} : {expected_personal}")
    print(f"{'Kết quả thực tế - Personal Details':<40} : {msg_per}")
    print(f"{'Trạng thái kiểm tra - Personal Details':<40} : {status_personal}")
    print("═" * 95)

    # ==== Assertions ====
    assert msg_add == expected_add
    assert msg_per == expected_personal

# =====================================================================
# ===============       TC_PIM_002 - FIRSTNAME EMPTY      =============
# =====================================================================
@pytest.mark.pim
def test_add_employee_firstname_empty(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    data = employee_data["valid_employee"].copy()
    data["firstName"] = ""   # Trống

    pim.go_to_pim()
    pim.click_add_employee()
    pim.fill_basic_info(data)
    pim.page.click(pim.BTN_SAVE_BASIC)

    pim.page.wait_for_selector(pim.ERROR_FIRSTNAME)
    actual_error = pim.page.text_content(pim.ERROR_FIRSTNAME).strip()
    expected_error = "Required"

    # ==== Họ tên hiển thị ====
    first_name_display = "-"   # vì firstname trống
    full_name = f"{first_name_display} {data.get('middleName','')} {data['lastName']}"

    # ==== Trạng thái ====
    status = "KẾT QUẢ KHỚP ✅" if actual_error == expected_error else "KẾT QUẢ KHÔNG KHỚP ❌"

    # ==== Log đẹp ====
    print("\n" + "═" * 95)
    print("        TC_PIM_002 - FIRSTNAME TRỐNG")
    print("═" * 95)
    print(f"{'Họ và tên':<40} : {full_name}")
    print(f"{'Kết quả mong đợi':<40} : {expected_error}")
    print(f"{'Kết quả thực tế':<40} : {actual_error}")
    print(f"{'Trạng thái kiểm tra':<40} : {status}")
    print("═" * 95)

    # ==== Assertion ====
    assert actual_error == expected_error

# =====================================================================
# ===============     TC_PIM_003 - LASTNAME TOO LONG      =============
# =====================================================================
@pytest.mark.pim
def test_add_employee_lastname_too_long(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    data = employee_data["valid_employee"].copy()

    # Generate Lastname quá 30 ký tự
    data["lastName"] = "A" * 31

    pim.go_to_pim()
    pim.click_add_employee()
    pim.fill_basic_info(data)
    pim.page.click(pim.BTN_SAVE_BASIC)

    pim.page.wait_for_selector(pim.ERROR_LASTNAME)
    actual_error = pim.page.text_content(pim.ERROR_LASTNAME).strip()
    expected_error = "Should not exceed 30 characters"

    # ==== Họ tên hiển thị ====
    full_name = f"{data['firstName']} {data.get('middleName','')} {data['lastName']}"

    # ==== Trạng thái ====
    status = "KẾT QUẢ KHỚP ✅" if actual_error == expected_error else "KẾT QUẢ KHÔNG KHỚP ❌"

    # ==== Log đẹp ====
    print("\n" + "═" * 95)
    print("        TC_PIM_003 - LASTNAME QUÁ DÀI")
    print("═" * 95)
    print(f"{'Họ và tên':<40} : {full_name}")
    print(f"{'Kết quả mong đợi':<40} : {expected_error}")
    print(f"{'Kết quả thực tế':<40} : {actual_error}")
    print(f"{'Trạng thái kiểm tra':<40} : {status}")
    print("═" * 95)

    # ==== Assertion ====
    assert actual_error == expected_error

# =====================================================================
# ================= TC_PIM_004 - EDIT EMPLOYEE ========================
# =====================================================================
@pytest.mark.pim
def test_edit_employee_success(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    emp_id = employee_data["valid_employee"]["employeeId"]
    new_data = employee_data["edit_employee"]

    # Step 1: Go to PIM
    pim.go_to_pim()

    # Step 2: Edit employee
    toast_title, toast_message = pim.edit_employee(
        emp_id=emp_id,
        new_first=new_data["firstName"],
        new_last=new_data["lastName"],
        new_middle=new_data.get("middleName", "")
    )

    # ==== Kết quả mong đợi ====
    expected_toast_title = "Success"
    expected_toast_message_contains = "Successfully Updated"
    expected_name = f"{new_data['firstName']} {new_data.get('middleName','')} {new_data['lastName']}".replace("  ", " ").strip()

    # ==== Trạng thái kiểm tra ====
    toast_status = "KẾT QUẢ KHỚP ✅" if toast_title.strip() == expected_toast_title and expected_toast_message_contains in toast_message else "KẾT QUẢ KHÔNG KHỚP ❌"

    # ==== Log đẹp ====
    print("\n" + "═" * 90)
    print("        TC_PIM_004 - CHỈNH SỬA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Employee ID':<30} : {emp_id}")
    print(f"{'Tên mới':<30} : {expected_name}")
    print(f"{'Toast thực tế':<30} : {toast_title} - {toast_message}")
    print(f"{'Trạng thái kiểm tra toast':<30} : {toast_status}")
    print("═" * 90)

# =====================================================================
# ================= TC_PIM_005 - DELETE EMPLOYEE ======================
# =====================================================================
@pytest.mark.pim
def test_delete_employee(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    # Fetch valid employee data
    delete_employee_id = employee_data["delete_employee"]["employeeId"]

    # Go to the PIM page and search for the employee by ID
    pim.go_to_pim()
    pim.search_by_id(delete_employee_id)

    # Hover over the delete button and click it to trigger the modal
    pim.page.hover(pim.TABLE_FIRST_ROW)
    pim.page.click(pim.BTN_DELETE)

    # Check the dialog content before confirming deletion
    dialog_title, dialog_message, expected_title, expected_message = pim.check_delete_dialog_content()

    # Bấm nút 'Yes, Delete' để xác nhận xóa
    pim.page.click("button:has-text('Yes, Delete')")

    # Nhận thông báo thành công sau khi xóa
    title, message = pim.get_toast_success_message()

    # Kết hợp title và message vào 1 chuỗi cho kết quả mong đợi
    expected = "Success - Successfully Deleted"

    # Kết hợp title và message vào 1 chuỗi cho kết quả thực tế
    actual = f"{title} - {message}"

    # ==== Log đẹp ====
    print("\n" + "═" * 95)
    print("        TC_PIM_005 - XÓA NHÂN VIÊN")
    print("═" * 95)
    print(f"{'Mã Nhân Viên':<40} : {delete_employee_id}")
    print("─" * 95)
    # In thông tin về hộp thoại (Dialog) - Tiếng Việt
    print(f"Tiêu đề Hộp thoại: '{dialog_title}'")
    print(f"Tiêu đề Mong đợi: '{expected_title}'")
    if dialog_title == expected_title:
        print("Kết quả: KHỚP ✅")
    else:
        print(f"Kết quả: KHÔNG KHỚP ❌ (Expected: '{expected_title}', Got: '{dialog_title}')")
    print(f"Nội dung Hộp thoại: '{dialog_message}'")
    print(f"Nội dung Mong đợi: '{expected_message}'")
    if dialog_message == expected_message:
        print("Kết quả: KHỚP ✅")
    else:
        print(f"Kết quả: KHÔNG KHỚP ❌ (Expected: '{expected_message}', Got: '{dialog_message}')")
    print("─" * 95)
    print(f"{'Kết quả mong đợi - Xóa Nhân Viên':<40} : {expected}")
    print(f"{'Kết quả thực tế - Xóa Nhân Viên':<40} : {actual}")

    # Kiểm tra kết quả thực tế và mong đợi
    if actual == expected:
        print("Kết quả: KHỚP ✅")
    else:
        print(f"Kết quả: KHÔNG KHỚP ❌ (Expected: '{expected}', Got: '{actual}')")
    print("═" * 95)

# =====================================================================
# ===============     TC_PIM_006 - SEARCH BY ID         ===============
# =====================================================================
@pytest.mark.pim
def test_search_by_valid_id(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    # Truy cập vào trang PIM và tìm kiếm nhân viên theo ID
    pim.go_to_pim()
    pim.search_by_id(employee_data["search_employee"]["employeeId"])

    # Lấy số lượng kết quả trả về
    result = pim.get_result_count()

    # In thông tin kết quả kiểm thử
    print("\n" + "═" * 90)
    print("        TC_PIM_006 - TÌM KIẾM THEO ID")
    print("═" * 90)

    print(f"{'Mã Nhân Viên':<40} : {employee_data['search_employee']['employeeId']}")
    print(f"{'Kết quả tìm kiếm':<40} : {result}")
    print("═" * 90)

    # Kiểm tra kết quả và in thông báo khớp hay không khớp
    if "Record Found" in result:
        print("Kết quả Tìm Kiếm THÀNH CÔNG ✅")
    else:
        print(f"Kết quả Tìm Kiếm KHÔNG THÀNH CÔNG ❌ (Expected: 'Record Found', Got: '{result}')")

    # Nếu tìm thấy bản ghi, thực hiện kiểm tra thành công
    if "Record Found" in result:
        # Bạn có thể thêm các bước kiểm tra chi tiết nếu cần
        pass

# =====================================================================
# ===============     TC_PIM_007 - FILTER SUBUNIT/INCLUDE =============
# =====================================================================
@pytest.mark.pim
def test_filter_by_status_and_subunit(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    pim.go_to_pim()

    # ===================== Lọc theo Sub Unit =====================
    # Click dropdown Sub Unit
    pim.page.click("//label[text()='Sub Unit']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")

    # Chọn giá trị trong dropdown Sub Unit
    pim.page.click("div.oxd-select-option >> text=LeeHyeon")

    # Click Search
    pim.page.click(pim.BTN_SEARCH)

    # Chờ một chút để cập nhật kết quả tìm kiếm
    pim.page.wait_for_timeout(1500)

    # Lấy giá trị đã chọn trong dropdown Sub Unit (sử dụng .nth(1) để chọn phần tử đúng)
    sub_unit_value = pim.page.locator("//label[text()='Sub Unit']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]").nth(1).text_content()

    # Kiểm tra số lượng kết quả
    actual_result = pim.get_result_count()

    # ===================== Lọc theo Include =====================
    pim.page.reload()  # Làm mới trang để tiếp tục kiểm tra với Include
    pim.go_to_pim()

    # Click dropdown Include
    pim.page.click("//label[text()='Include']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")

    # Chọn giá trị trong dropdown Include
    pim.page.click("div.oxd-select-option >> text=Current and Past Employees")

    # Click Search
    pim.page.click(pim.BTN_SEARCH)

    # Chờ một chút để cập nhật kết quả tìm kiếm
    pim.page.wait_for_timeout(1500)

    # Lấy giá trị đã chọn trong dropdown Include (sử dụng .nth(1) để chọn phần tử đúng)
    include_value = pim.page.locator("//label[text()='Include']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]").nth(1).text_content()

    # Kiểm tra số lượng kết quả
    actual_result_include = pim.get_result_count()

    # ===================== In kết quả kiểm thử =====================
    print("\n" + "═" * 90)
    print("        TC_PIM_007 - KẾT QUẢ LỌC NHÂN VIÊN")
    print("═" * 90)

    # In kết quả cho Sub Unit
    print(f"\n{'Sub Unit lọc':<45} : {sub_unit_value.strip()}")  # Lấy giá trị thực tế từ dropdown
    print(f"{'Kết quả thực tế Sub Unit (Actual)':<45} : {actual_result}")
    if actual_result == "No Records Found":
        print(f"{'Kết quả mong đợi Sub Unit (Expected)':<45} : No Records Found")
    else:
        print(f"{'Kết quả mong đợi Sub Unit (Expected)':<45} : Có kết quả")

    # Thêm dòng phân cách
    print("\n" + "─" * 90)

    # In kết quả cho Include
    print(f"{'Include lọc':<45} : {include_value.strip()}")  # Lấy giá trị thực tế từ dropdown
    print(f"{'Kết quả thực tế Include (Actual)':<45} : {actual_result_include}")
    if actual_result_include == "No Records Found":
        print(f"{'Kết quả mong đợi Include (Expected)':<45} : No Records Found")
    else:
        print(f"{'Kết quả mong đợi Include (Expected)':<45} : Có kết quả")

    # Dòng phân cách cuối cùng
    print("═" * 90)


# =====================================================================
# ===============     TC_PIM_008 - PAGINATION            ===============
# =====================================================================
@pytest.mark.pim
def test_pagination_observe(logged_in_page):
    pim = PIMPage(logged_in_page.page)
    pim.go_to_pim()

    # ===== Danh sách các trang =====
    pages = pim.page.query_selector_all("ul.oxd-pagination__ul li button.oxd-pagination-page-item--page")
    num_pages = len(pages)

    # ===== Nút Next =====
    next_button = pim.page.query_selector("button.oxd-pagination-page-item--previous-next")
    disabled = next_button.get_attribute("disabled") if next_button else None

    # ===== Liệt kê nhân viên trang hiện tại =====
    rows = pim.page.query_selector_all("div.oxd-table-card")
    employees_on_page = [row.text_content().strip() for row in rows]

    # ===== In kết quả ra màn hình =====
    print("\n" + "═" * 90)
    print("        TC_PIM_008 - PHÂN TRANG")
    print("═" * 90)

    if num_pages <= 1:
        print("KẾT QUẢ: KHÔNG CÓ PHÂN TRANG")
        print(f"Số lượng nhân viên trang hiện tại: {len(employees_on_page)}")
        for i, name in enumerate(employees_on_page, start=1):
            print(f"  {i:>2}. {name}")
    else:
        print("KẾT QUẢ: CÓ PHÂN TRANG")
        print(f"{'Số trang tìm thấy':<40} : {num_pages}")
        print(f"{'Nút Next tồn tại':<40} : {'Có' if next_button else 'Không'}")
        print(f"{'Nút Next disabled':<40} : {disabled}")
        print(f"{'Nhân viên trang hiện tại':<40} :")
        for i, name in enumerate(employees_on_page, start=1):
            print(f"  {i:>2}. {name}")

    print("═" * 90)

    # ===== Assertion =====
    assert len(rows) >= 1, "Trang hiện tại phải có ít nhất 1 nhân viên"



########################################################
@pytest.mark.pim
def test_edit_employee_success(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    emp_id = employee_data["valid_employee"]["employeeId"]
    new_data = employee_data["edit_employee"]

    # Step 1: Go to PIM
    pim.go_to_pim()

    # Step 2: Edit employee
    toast_title, toast_message = pim.edit_employee(
        emp_id=emp_id,
        new_first=new_data["firstName"],
        new_last=new_data["lastName"],
        new_middle=new_data.get("middleName", "")
    )

    # ==== Kết quả mong đợi ====
    expected_toast_title = "Success"
    expected_toast_message_contains = "Successfully Updated"
    expected_name = f"{new_data['firstName']} {new_data.get('middleName','')} {new_data['lastName']}".replace("  ", " ").strip()

    # ==== Trạng thái kiểm tra ====
    toast_status = "KẾT QUẢ KHỚP ✅" if toast_title.strip() == expected_toast_title and expected_toast_message_contains in toast_message else "KẾT QUẢ KHÔNG KHỚP ❌"

    # ==== Log đẹp ====
    print("\n" + "═" * 90)
    print("        TC_PIM_004 - CHỈNH SỬA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Employee ID':<30} : {emp_id}")
    print(f"{'Tên mới':<30} : {expected_name}")
    print(f"{'Toast thực tế':<30} : {toast_title} - {toast_message}")
    print(f"{'Trạng thái kiểm tra toast':<30} : {toast_status}")
    print("═" * 90)



@pytest.mark.pim
def test_delete_employee_check(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    pim.go_to_pim()
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    pim.delete_first_employee()

    # Kiểm tra kết quả tìm kiếm sau khi xóa
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    result_count = pim.get_result_count()
    assert "Record Found" not in result_count

    print("\n" + "═" * 90)
    print("        TC_PIM_005 - XÓA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Employee ID đã xóa':<40} : {employee_data['valid_employee']['employeeId']}")
    print(f"{'Kết quả thực tế':<40} : THÀNH CÔNG")
    print("═" * 90)
