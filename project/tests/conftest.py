# tests/conftest.py  ← THAY TOÀN BỘ FILE NÀY (ĐÃ FIX LỖI + CHỤP ẢNH 100%)
import pytest
from playwright.sync_api import sync_playwright
import json
import os
import datetime
from project.config import settings


# ================================
# Tìm root + tạo thư mục ảnh
# ================================
def find_project_root():
    current = os.path.abspath(os.getcwd())
    while True:
        if os.path.isfile(os.path.join(current, "pytest.ini")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            raise RuntimeError("Không tìm thấy pytest.ini")
        current = parent


PROJECT_ROOT = find_project_root()
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ================================
# Load users.json
# ================================
data_path = os.path.join(PROJECT_ROOT, "project", "data", "users.json")
with open(data_path, "r", encoding="utf-8") as f:
    testdata = json.load(f)


# ================================
# Browser fixture
# ================================
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=settings.HEADLESS,
            args=["--start-maximized"]
        )
        yield browser
        browser.close()


# ================================
# Page fixture + lưu context đúng cách
# ================================
@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context(viewport=None)
    page = context.new_page()

    # Cách đúng: lưu vào request để hook lấy được
    request.node._page = page          # Dùng thuộc tính private
    request.node._context = context    # Lưu context để đóng sau

    yield page

    # Đóng context sau test
    try:
        context.close()
    except:
        pass


# ================================
# Dữ liệu + Page Objects
# ================================
@pytest.fixture(scope="session")
def users():
    return testdata


@pytest.fixture(scope="function")
def login_page(page):
    from project.pages.login_page import LoginPage
    return LoginPage(page)


@pytest.fixture(scope="function")
def dashboard_page(page):
    from project.pages.dashboard_page import DashboardPage
    return DashboardPage(page)


@pytest.fixture(scope="function")
def logged_in_page(page, users, login_page):
    from project.pages.dashboard_page import DashboardPage
    login_page.goto("http://localhost/orangehrm-5.8/web/index.php/auth/login")
    admin = users["admin"]
    login_page.login(admin["username"], admin["password"])
    dashboard = DashboardPage(page)
    assert dashboard.is_dashboard_displayed(), "Đăng nhập thất bại!"
    return dashboard


# ================================
# HOOK CHỤP ẢNH – ĐÃ FIX 100% (chạy ngon lành)
# ================================
def _capture_screenshot(page, name, status):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
    safe_name = "".join(c if c.isalnum() else "_" for c in name)
    filename = f"{status}_{safe_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    try:
        page.wait_for_timeout(800)
        page.screenshot(path=filepath, full_page=True)
        print(f"Đã lưu ảnh: {filepath}")
    except Exception as e:
        print(f"Lỗi chụp ảnh: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Chỉ chụp khi phase "call" (test thực thi)
    if rep.when == "call":
        page = getattr(item, "_page", None)
        if page:
            status = "PASS" if rep.passed else "FAIL"
            _capture_screenshot(page, item.name, status)