import pytest
from playwright.sync_api import sync_playwright
import json
import os
import datetime
from pathlib import Path
from project.config import settings

# =====================================================
# TÌM PROJECT ROOT (dựa vào pytest.ini)
# =====================================================
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

# =====================================================
# THƯ MỤC LƯU ARTIFACT
# =====================================================
SCREENSHOT_DIR = Path(PROJECT_ROOT) / "screenshots"
VIDEO_DIR = Path(PROJECT_ROOT) / "videos"
TRACE_DIR = Path(PROJECT_ROOT) / "trace"

SCREENSHOT_DIR.mkdir(exist_ok=True)
VIDEO_DIR.mkdir(exist_ok=True)
TRACE_DIR.mkdir(exist_ok=True)

# =====================================================
# LOAD TEST DATA USERS (DDT)
# =====================================================
data_path = Path(PROJECT_ROOT) / "project" / "data" / "users.json"
with open(data_path, "r", encoding="utf-8") as f:
    testdata = json.load(f)

# =====================================================
# BROWSER FIXTURE
# =====================================================
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=settings.HEADLESS
        )
        yield browser
        browser.close()

# =====================================================
# PAGE FIXTURE (SCREENSHOT + VIDEO + TRACE)
# =====================================================
@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context(
        viewport={"width": 1366, "height": 768},  # FULL HD
        device_scale_factor=1.25,  # 🔥 RÕ NÉT
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 1366, "height": 768}
    )
    page = context.new_page()

    # Lưu để hook dùng
    request.node._page = page
    request.node._context = context

    # 🧭 Trace
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield page

    # 🧭 Stop trace
    trace_path = TRACE_DIR / f"{request.node.name}.zip"
    try:
        context.tracing.stop(path=str(trace_path))
    except Exception as e:
        print("Trace stop error:", e)

    # Đóng context (video tự lưu)
    try:
        context.close()
    except:
        pass

# =====================================================
# DATA FIXTURES
# =====================================================
@pytest.fixture(scope="session")
def users():
    return testdata

@pytest.fixture(scope="session")
def employee_data():
    """Đọc dữ liệu nhân viên cho PIM (DDT)"""
    data_path = Path(PROJECT_ROOT) / "project" / "data" / "employee_data.json"
    if not data_path.exists():
        pytest.fail(f"Không tìm thấy file dữ liệu: {data_path}")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

# =====================================================
# PAGE OBJECT FIXTURES
# =====================================================
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

# =====================================================
# SCREENSHOT FUNCTION
# =====================================================
def _capture_screenshot(page, name, status):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
    safe_name = "".join(c if c.isalnum() else "_" for c in name)
    filename = f"{status}_{safe_name}_{timestamp}.png"
    filepath = SCREENSHOT_DIR / filename
    try:
        page.wait_for_timeout(500)
        page.screenshot(path=str(filepath), full_page=True)
        print(f"[SCREENSHOT] Saved: {filepath}")
    except Exception as e:
        print(f"[SCREENSHOT ERROR]: {e}")

# =====================================================
# PYTEST HOOK – CHỤP SCREENSHOT PASS / FAIL
# =====================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        page = getattr(item, "_page", None)
        if page:
            status = "PASS" if rep.passed else "FAIL"
            _capture_screenshot(page, item.name, status)
