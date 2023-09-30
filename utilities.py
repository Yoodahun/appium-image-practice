import configparser

from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from selenium.webdriver.chrome.options import Options as WebChromeOptions


def get_config(file_name:str)-> configparser.ConfigParser:
    config = configparser.ConfigParser()

    ini_file_path = "./resources/"+ file_name + ".ini"
    config.read(ini_file_path)
    return config

def desired_caps_manager(platform:str):
    options = None

    if platform == "ios":
        options = XCUITestOptions()
        desired_caps = get_config("desired_capabilities")["IOS"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.bundle_id = desired_caps["BUNDLE_ID"]
        options.udid = desired_caps["UDID"]

    elif platform == "android":
        options = UiAutomator2Options()
        desired_caps = get_config("desired_capabilities")["ANDROID"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.app_activity = desired_caps["APP_ACTIVITY"]
        options.app_package = desired_caps["APP_PACKAGE"]
        options.device_name = desired_caps["DEVICE_NAME"]

    elif platform == "ios_safari":
        options = XCUITestOptions()
        desired_caps = get_config("desired_capabilities")["IOS_SAFARI"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.udid = desired_caps["UDID"]
        options.set_capability("browserName", desired_caps["BROWSER_NAME"])

    elif platform == "android_chrome":
        options = UiAutomator2Options()
        desired_caps = get_config("desired_capabilities")["ANDROID"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.device_name = desired_caps["DEVICE_NAME"]
        options.set_capability("browserName", desired_caps["BROWSER_NAME"])

    else: #WEB
        options = WebChromeOptions()
        desired_caps = get_config("desired_capabilities")["WEB"]

        options.add_argument("--start-fullscreen")
        options.add_argument("--incognito")
        options.add_argument(f"user-agent={desired_caps['USER_AGENT']}")

    return options

