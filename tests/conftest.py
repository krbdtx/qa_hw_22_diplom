import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sofrino_auto_test.utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "122.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='122.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.config.base_url = 'https://sofrino.ru'
    browser.config.window_width = 1200
    browser.config.window_height = 1400
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


def pytest_configure(config):
    config.addinivalue_line("markers", "web")

@pytest.fixture(autouse=True)
def auto_use_fixture(request):
    if request.node.get_closest_marker("web"):
        request.getfixturevalue("setup_browser")

@pytest.fixture()
def base_api_url():
    base_url = 'https://sofrino.ru'
    return base_url
