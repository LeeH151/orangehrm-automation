def fill_with_delay(page, selector, value, delay_ms=1000):
    page.fill(selector, value)
    page.wait_for_timeout(delay_ms)

def click_with_delay(page, selector, delay_ms=1000):
    page.click(selector)
    page.wait_for_timeout(delay_ms)
