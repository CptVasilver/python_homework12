from utils import attach
from selene import browser
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

DEFAULT_BROWSER_VERSION = "122.0"


def path(file_name):
    return str(Path(__file__).parent.joinpath(f'resources/{file_name}'))


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='122.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()



@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "browser_version",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_video(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    browser.quit()
