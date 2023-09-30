import time

import pytest
from utilities import driver_factory
from selenium.webdriver.remote import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--platform", default="pc_web", action="store", help="pc/android/ios/android_chrome/ios_safari"
    )

@pytest.fixture(scope="class", autouse=True)
def setup_and_teardown(request) -> webdriver:

    platform = request.config.getoption('platform').lower()

    driver = driver_factory(platform)

    if platform in ("pc_web", "android_chrome", "ios_safari"):
        driver.get("https://www.naver.com")

    request.cls.driver = driver

    yield

    driver.quit()
    driver = None
    time.sleep(1)


