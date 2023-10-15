import time
import allure
import pytest
from allure_commons.types import AttachmentType

from utilities import driver_factory
from selenium.webdriver.remote import webdriver
from typing import Dict, Tuple

_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}


def pytest_addoption(parser):
    """
    pytest 실행 시에 commandLine option을 설정합니다.
    :param parser:
    :return:
    """
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
    """
    driver 객체를 생성하고, 삭제합니다.
    class 단위로 실행되며, request 객체에 드라이버를 저장하여, 필요 시 request 객체에서 꺼내사용할 수 있습니다.
    :param request:
    :return:
    """

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
    """
    하나의 클래스 내에 실행해야할 메소드가 여러개일 경우 혹은 의존관계에 있는 선제 테스트가 실패할 경우,\n
    다음 테스트가 실행되지 않도록 하는 설정입니다.
    또한 해당 테스트가 실패했을 시에 리포트에 캡쳐를 첨부하도록 합니다.
    :param item:
    :param call:
    :return:
    """
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
    """
    의존관계의 테스트 A와 B에서, B의 선행 테스트 A가 실패하는 경우 B의 테스트는 무조건 강제적으로 실행실패시키도록하는 메소드입니다.

    :param item:
    :return:
    """
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
