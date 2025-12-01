from project.utils.config import BASE_URL

def test_open_homepage(page):
    page.goto(BASE_URL)
    assert "OrangeHRM" in page.title()
    page.wait_for_timeout(5000)  # 5000ms = 5s
