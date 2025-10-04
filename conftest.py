from playwright.sync_api import sync_playwright
from pytest import fixture

@fixture(scope="session")
def my_page():
    context = sync_playwright().start().chromium.launch(headless=False).new_context()
    page = context.new_page()

    yield page

    context.close()
    page.browser.close()
    sync_playwright().stop()
    
