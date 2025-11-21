def test_open_homepage(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    assert "OrangeHRM" in page.title()
