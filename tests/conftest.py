from utils import attach
from selene import browser
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def path(file_name):
    return str(Path(__file__).parent.joinpath(f'resources/{file_name}'))


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
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