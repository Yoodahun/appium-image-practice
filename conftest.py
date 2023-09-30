import pytest
from selenium.webdriver.remote import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--platform", default="pc", action="store", help="pc/android/ios/android_chrome/ios_safari"
    )

@pytest.fixture(scope="class", autouse=True)
def setup_and_teardown(request) -> webdriver:

    platform = request.config.getoption('platform').upper()

    driver = driver_factory(platform)


