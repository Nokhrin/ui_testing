import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('--window-size=1920,1080')
    firefox_options.add_argument('--start-maximized')
    # firefox_options.add_argument('--headless')
    return firefox_options


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.maximize_window()

    yield browser
