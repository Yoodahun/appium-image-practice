import configparser
import logging

from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from selenium.webdriver.chrome.options import Options as WebChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_driver
from webdriver_manager.chrome import ChromeDriverManager


def config_factory(file_name: str) -> configparser.ConfigParser:
    """
    config ini파일을 읽어서 해당 값을 리턴하는 메소드입니다.
    .ini 파일들을 대부분 ./resources/ 하위에 위치해야합니다. 만약 해당위치보다 더 하위로 내려가는 경우
    파라미터 file_name에 파일의 경로까지 함께 포함해서 호출해야합니다.
    :param file_name:
    :return configparser.ConfigParser:
    """
    config = configparser.ConfigParser()

    ini_file_path = "./resources/" + file_name + ".ini"
    config.read(ini_file_path)
    return config


def url_manager(platform: str) -> str:
    """
    실행해야하는 url을 지정합니다.
    기본적으로는 로컬실행이고, pc_web을 제외하는 경우는 appium server를 호출해야하므로 4723을 호출합니다.
    만약 리모트 실행을 하게 된다면 별도의 parameter로 분기처리가 필요하며, 호출주소 또한 localhost가 아닌 다른 주소를 선언해주어야 합니다.

    :param platform: str
    :return: str
    """
    if platform != "pc_web":
        return "http://0.0.0.0:4723"


def desired_caps_manager(platform: str):
    """
    실행 시 드라이버에 설정한 desired_capabilties를 설정하는 함수입니다.
    실행하는 플랫폼에 따라 다르게 설정합니다.

    설정값들은 ./resources/desired_capabilities.ini 에서 읽어옵니다.
    :param platform:
    :return:
    """
    options = None

    if platform == "ios":
        """
        iOS 기기의 경우에는 무조건 udid를 지정해주어야합니다.
        """
        options = XCUITestOptions()
        desired_caps = config_factory("desired_capabilities")["IOS"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.bundle_id = desired_caps["BUNDLE_ID"]
        options.udid = desired_caps["UDID"]

    elif platform == "android":
        """
        안드로이드의 경우 기기 1대를 실행할 때에는 DEVICE_NAME, UDID는 지정해주지 않아도 되며,
        2대이상 실행이 필요한 경우에, 기기 구분을 위해 지정해주어야합니다.
        """
        options = UiAutomator2Options()
        desired_caps = config_factory("desired_capabilities")["ANDROID"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.app_activity = desired_caps["APP_ACTIVITY"]
        options.app_package = desired_caps["APP_PACKAGE"]
        options.device_name = desired_caps["DEVICE_NAME"]

    elif platform == "ios_safari":
        """
        iOS 기기의 경우에는 무조건 udid를 지정해주어야합니다.
        """
        options = XCUITestOptions()
        desired_caps = config_factory("desired_capabilities")["IOS_SAFARI"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.udid = desired_caps["UDID"]
        options.set_capability("browserName", desired_caps["BROWSER_NAME"])

    elif platform == "android_chrome":
        """
        안드로이드의 경우 기기 1대를 실행할 때에는 DEVICE_NAME, UDID는 지정해주지 않아도 되며,
        2대이상 실행이 필요한 경우에, 기기 구분을 위해 지정해주어야합니다.
        """
        options = UiAutomator2Options()
        desired_caps = config_factory("desired_capabilities")["ANDROID_CHROME"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.device_name = desired_caps["DEVICE_NAME"]
        options.set_capability("browserName", desired_caps["BROWSER_NAME"])

    else:  # pc_web
        """
        pc_web의 경우 시작 시에 최대화면설정을 하고, 시크릿모드를 활성화합니다.
        """
        options = WebChromeOptions()
        desired_caps = config_factory("desired_capabilities")["WEB"]

        options.add_argument("--start-fullscreen")
        options.add_argument("--incognito")
        options.add_argument(f"user-agent={desired_caps['USER_AGENT']}")

    return options


def driver_factory(platform: str):
    """
    platform값에 따라 생성해야할 드라이버 객체를 구분하여 리턴합니다.
    pc_web의 경우에는 ChromeDriverManager를 이용하여 자동으로 설치하도록 구현되어있습니다.
    리모트의 경우에는 다른 방법으로 설치해주어야합니다.
    :param platform: str
    :return:
    """
    if platform == "pc_web":
        return selenium_webdriver.Chrome(
            options=desired_caps_manager(platform),
            service=ChromeService(ChromeDriverManager().install())
        )
    else:
        return appium_driver.Remote(
            url_manager(platform), options=desired_caps_manager(platform)
        )


def logger_factory(class_name: str) -> logging.Logger:
    """
    logger 객체를 생성해서 리턴합니다.
    :param class_name: str
    :return:
    """
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.INFO)

    return logger
