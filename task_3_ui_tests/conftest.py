import pytest
import pytest_html
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(screenshot_path))
            report.extra = extra

@pytest.fixture
def driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

def pytest_generate_tests(metafunc):
    browsers = metafunc.config.getoption("browser").split(",")
    if "browser" in metafunc.fixturenames:
        metafunc.parametrize("browser", browsers, scope="function")

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )