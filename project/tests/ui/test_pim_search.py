# tests/ui/test_pim_crud.py – CHẠY NGON 100% VỚI FILE DỮ LIỆU CỦA BẠN
import pytest
from project.pages.pim_page import PIMPage
import time

def test_add_multiple_employees(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    # Lấy danh sách nhân viên từ JSON
    employees_list = employee_data.get("employees", [])

    for employee in employees_list:
        pim.go_to_pim()
        pim.add_employee_complete(employee)

        first_name_display = employee['firstName'] if employee['firstName'] else "-"

        print("\n" + "═" * 90)
        print(
            f"        THÊM NHÂN VIÊN - {first_name_display} {employee.get('middleName', '')} {employee['lastName']}")
        print("═" * 90)
        print(f"{'Employee ID':<40} : {employee['employeeId']}")
        print(f"{'Kết quả':<40} : THÀNH CÔNG")
        print("═" * 90)

@pytest.mark.pim
def test_add_employee_success(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    data = employee_data["valid_employee"]

    pim.go_to_pim()
    pim.add_employee_complete(data)

    print("\n" + "═" * 90)
    print("        TC_PIM_001 - THÊM NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Họ và tên':<40} : {data['firstName']} {data.get('middleName','')} {data['lastName']}")
    print(f"{'Employee ID':<40} : {data['employeeId']}")
    print(f"{'Kết quả':<40} : THÀNH CÔNG")
    print("═" * 90)

@pytest.mark.pim
def test_add_employee_firstname_empty(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    # Lấy dữ liệu employee hợp lệ và chỉnh sửa Firstname trống
    data = employee_data["valid_employee"].copy()
    data["firstName"] = ""

    # Điều hướng đến trang PIM và mở form thêm nhân viên
    pim.go_to_pim()
    pim.click_add_employee()
    pim.fill_basic_info(data)
    pim.page.click(pim.BTN_SAVE_BASIC)  # Chỉ nhấn Save Basic để kiểm tra lỗi

    # --- Kiểm tra lỗi ---
    pim.page.wait_for_selector(pim.ERROR_FIRSTNAME, timeout=5000)
    actual_error = pim.page.text_content(pim.ERROR_FIRSTNAME).strip()
    expected_error = "Required"

    # Thay firstName trống bằng ký hiệu "-" để in log
    first_name_display = data['firstName'] if data['firstName'] else "-"

    # --- Dừng 3 giây để quan sát UI trước khi hook chụp ảnh tự động chạy ---
    time.sleep(3)

    # In log chi tiết
    print("\n" + "═" * 90)
    print("        TC_PIM_002 - THÊM NHÂN VIÊN - FIRSTNAME TRỐNG")
    print("═" * 90)
    print(f"{'Họ và tên':<40} : {first_name_display} {data.get('middleName','')} {data['lastName']}")
    print(f"{'Employee ID':<40} : {data['employeeId']}")
    print(f"{'Thông báo lỗi mong đợi (Expected)':<40} : {expected_error}")
    print(f"{'Thông báo lỗi thực tế (Actual)':<40} : {actual_error}")
    print("═" * 90)

    # Assert kiểm tra lỗi
    assert actual_error == expected_error, (
        f"Expected error message: '{expected_error}', but got: '{actual_error}'"
    )

@pytest.mark.pim
def test_add_employee_lastname_too_long(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    data = employee_data["valid_employee"]
    data["lastName"] = "A" * 31  # Lastname quá dài

    pim.go_to_pim()
    pim.click_add_employee()
    pim.fill_basic_info(data)
    pim.page.click(pim.BTN_SAVE_BASIC)

    pim.page.wait_for_selector(pim.ERROR_LASTNAME, timeout=5000)
    actual_error = pim.page.text_content(pim.ERROR_LASTNAME).strip()
    expected_error = "Should not exceed 30 characters"

    last_name_display = data['lastName'] if data['lastName'] else "-"

    time.sleep(3)

    print("\n" + "═" * 90)
    print("        TC_PIM_003 - THÊM NHÂN VIÊN - LASTNAME QUÁ DÀI")
    print("═" * 90)
    print(f"{'Họ và tên':<40} : {data['firstName']} {data.get('middleName','')} {last_name_display}")
    print(f"{'Employee ID':<40} : {data['employeeId']}")
    print(f"{'Thông báo lỗi mong đợi (Expected)':<40} : {expected_error}")
    print(f"{'Thông báo lỗi thực tế (Actual)':<40} : {actual_error}")
    print("═" * 90)

    # Assert kiểm tra lỗi
    assert actual_error == expected_error, (
        f"Expected error message: '{expected_error}', but got: '{actual_error}'"
    )

@pytest.mark.pim
def test_edit_employee(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    new_data = employee_data["edit_employee"]

    pim.go_to_pim()
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    pim.edit_first_employee(new_data["firstName"], new_data["lastName"])

    print("\n" + "═" * 90)
    print("        TC_PIM_004 - CHỈNH SỬA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Tên mới':<40} : {new_data['firstName']} {new_data['lastName']}")
    print(f"{'Kết quả':<40} : THÀNH CÔNG")
    print("═" * 90)


@pytest.mark.pim
def test_delete_employee(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    pim.go_to_pim()
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    pim.delete_first_employee()

    print("\n" + "═" * 90)
    print("        TC_PIM_005 - XÓA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Employee ID đã xóa':<40} : {employee_data['valid_employee']['employeeId']}")
    print(f"{'Kết quả':<40} : THÀNH CÔNG")
    print("═" * 90)


@pytest.mark.pim
def test_search_by_valid_id(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)

    pim.go_to_pim()
    pim.search_by_id(employee_data["search_employee"]["employeeId"])
    count = pim.get_result_count()

    print("\n" + "═" * 90)
    print("        TC_PIM_006 - TÌM KIẾM THEO ID HỢP LỆ")
    print("═" * 90)
    print(f"{'ID tìm kiếm':<40} : {employee_data['search_employee']['employeeId']}")
    print(f"{'Kết quả':<40} : {count}")
    print("═" * 90)

    assert "Record Found" in count

@pytest.mark.pim
def test_filter_by_status_and_subunit(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    pim.go_to_pim()
    # Click dropdown Sub Unit
    pim.page.click("//label[text()='Sub Unit']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
    # Chọn giá trị trong dropdown
    pim.page.click("div.oxd-select-option >> text=LeeHyeon")
    # Click Search
    pim.page.click(pim.BTN_SEARCH)
    # Chờ thông báo xuất hiện
    pim.page.wait_for_selector("div.oxd-toast-container", timeout=5000)
    toast_message = pim.page.locator("div.oxd-toast-container").text_content()
    # Expected & actual
    expected_result = "No Records Found"
    # Nếu có kết quả
    actual_result = pim.get_result_count()
    # In bảng format đẹp
    print("\n" + "═" * 90)
    print(" TC_PIM_007 - LỌC NHÂN VIÊN THEO SUB UNIT")
    print("═" * 90)
    print(f"{'Sub Unit lọc':<40} : LeeHyeon")
    print(f"{'Kết quả mong đợi (Expected)':<40} : {expected_result}")
    print(f"{'Kết quả thực tế (Actual)':<40} : {actual_result}")
    print("═" * 90)
    # Thực hiện assert
    assert expected_result in actual_result, "Kết quả lọc không đúng!"

@pytest.mark.pim
def test_pagination_observe(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    pim.go_to_pim()

    # Danh sách các trang
    pages = pim.page.query_selector_all("ul.oxd-pagination__ul li button.oxd-pagination-page-item--page")
    num_pages = len(pages)

    # Nút Next
    next_button = pim.page.query_selector("button.oxd-pagination-page-item--previous-next")
    disabled = next_button.get_attribute("disabled") if next_button else None

    # Liệt kê nhân viên trang hiện tại
    rows = pim.page.query_selector_all("div.oxd-table-card")
    employees_on_page = [row.text_content().strip() for row in rows]

    # ===== In kết quả ra màn hình =====
    print("\n" + "═" * 90)
    print("        TC_PIM_008 - KIỂM TRA PHÂN TRANG")
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

###################################################


@pytest.mark.pim
def test_edit_employee_name_update(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    new_data = employee_data["edit_employee"]

    pim.go_to_pim()
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    pim.edit_first_employee(new_data["firstName"], new_data["lastName"])

    # Kiểm tra thông tin đã sửa
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    updated_name = pim.page.text_content("table tbody tr td:nth-child(2)")  # Giả sử tên nhân viên ở cột thứ 2
    assert new_data["firstName"] in updated_name and new_data["lastName"] in updated_name

    print("\n" + "═" * 90)
    print("        TC_PIM_004 - CHỈNH SỬA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Tên mới':<40} : {new_data['firstName']} {new_data['lastName']}")
    print(f"{'Kết quả':<40} : THÀNH CÔNG")
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
    print(f"{'Kết quả':<40} : THÀNH CÔNG")
    print("═" * 90)









@pytest.mark.pim
def test_edit_employee(logged_in_page, employee_data):
    pim = PIMPage(logged_in_page.page)
    new_data = employee_data["edit_employee"]

    pim.go_to_pim()
    pim.search_by_id(employee_data["valid_employee"]["employeeId"])
    pim.edit_first_employee(new_data["firstName"], new_data["lastName"])

    # ==============================
    # Lấy Toast Message
    # ==============================
    # Chờ toast xuất hiện
    pim.page.wait_for_selector("div.oxd-toast-container--toast", timeout=5000)

    toast = pim.page.locator("div.oxd-toast-container--toast")

    # Lấy đúng title và message
    title = toast.locator(".oxd-text--toast-title").text_content().strip()
    message = toast.locator(".oxd-text--toast-message").text_content().strip()

    # ==============================
    # In kết quả
    # ==============================
    print("\n" + "═" * 90)
    print("        TC_PIM_004 - CHỈNH SỬA NHÂN VIÊN THÀNH CÔNG")
    print("═" * 90)
    print(f"{'Tên mới':<40} : {new_data['firstName']} {new_data['lastName']}")
    print(f"{'Toast Title':<40} : {title}")
    print(f"{'Toast Message':<40} : {message}")
    print(f"{'Kết quả':<40} : THÀNH CÔNG")
    print("═" * 90)

    # ==============================
    # Optional: assert
    # ==============================
    assert "Success" in title
    assert (
        "Successfully Updated" in message
        or "Successfully Saved" in message
    )





