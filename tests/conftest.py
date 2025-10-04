from playwright.sync_api import sync_playwright
from pytest import fixture

@fixture(scope="session")
def my_page():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    yield page
    page.context.close()
    page.browser.close()
    sync_playwright().stop()                                                                                        

    