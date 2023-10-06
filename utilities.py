import configparser
import logging

from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from selenium.webdriver.chrome.options import Options as WebChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_driver
from webdriver_manager.chrome import ChromeDriverManager


def get_config(file_name:str)-> configparser.ConfigParser:
    config = configparser.ConfigParser()

    ini_file_path = "./resources/"+ file_name + ".ini"
    config.read(ini_file_path)
    return config

def url_manager(platform:str)->str:
    if platform != "pc_web":
        return "http://0.0.0.0:4723"

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
        desired_caps = get_config("desired_capabilities")["ANDROID_CHROME"]

        options.platform_name = desired_caps["PLATFORM_NAME"]
        options.automation_name = desired_caps["AUTOMATION_NAME"]
        options.device_name = desired_caps["DEVICE_NAME"]
        options.set_capability("browserName", desired_caps["BROWSER_NAME"])

    else: #pc_web
        options = WebChromeOptions()
        desired_caps = get_config("desired_capabilities")["WEB"]

        options.add_argument("--start-fullscreen")
        options.add_argument("--incognito")
        options.add_argument(f"user-agent={desired_caps['USER_AGENT']}")

    return options

def driver_factory(platform:str):
    if platform == "pc_web":
        return selenium_webdriver.Chrome(
            options=desired_caps_manager(platform),
            service=ChromeService(ChromeDriverManager().install())
        )
    else:
        return appium_driver.Remote(
            url_manager(platform),options=desired_caps_manager(platform)
        )


def get_logger(class_name:str)->logging.Logger:
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.INFO)

    return logger
