def test_playwright_opens_page(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
