import time
import allure
import pytest
from allure_commons.types import AttachmentType

from utilities import driver_factory
from selenium.webdriver.remote import webdriver
from typing import Dict, Tuple

_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}


def pytest_addoption(parser):
    parser.addoption(
        "--platform", default="pc_web", action="store", help="pc/android/ios/android_chrome/ios_safari"
    )

@pytest.fixture(scope="session")
def print_for_testcase(request) -> str:
    platform = request.config.getoption('platform').upper()

    print("this is fixture method for session-----")

    return platform

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


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        # incremental marker is used
        if call.excinfo is not None:
            # the test has failed
            # retrieve the class name of the test
            cls_name = str(item.cls)
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # retrieve the name of the test function
            test_name = item.originalname or item.name
            # store in _test_failed_incremental the original name of the failed test
            _test_failed_incremental.setdefault(cls_name, {}).setdefault(
                parametrize_index, test_name
            )
            allure.attach(
                item.cls.driver.get_screenshot_as_png(),
                "Screenshot",
                attachment_type=AttachmentType.PNG
            )


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        # retrieve the class name of the test
        cls_name = str(item.cls)
        # check if a previous test has failed for this class
        if cls_name in _test_failed_incremental:
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # retrieve the name of the first test function to fail for this class name and index
            test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
            # if name found, test has failed for the combination of class name & test name
            if test_name is not None:
                pytest.xfail(f"previous test failed ({test_name})")
