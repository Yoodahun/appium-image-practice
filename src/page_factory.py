import re
from typing import List

from appium.webdriver import Remote, WebElement
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from utilities import get_logger


class PageFactory:
    def __init__(self, driver):
        self.driver: Remote = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(type(self).__name__)

    def _find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    def _find_element_for_wait(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _find_elements_for_wait(self, locator: tuple) -> List[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def _get_text(self, locator: tuple) -> str:
        return self._find_element_for_wait(locator).text

    def _input(self, locator: tuple, text: str):
        input_element = self._find_element_for_wait(locator)
        input_element.clear()
        input_element.send_keys(text)

    def _click(self, locator: tuple):
        self._find_element_for_wait(locator).click()

    def _is_visible(self, locator: tuple) -> bool:
        try:
            return self._find_element_for_wait(locator).is_displayed()
        except TimeoutException:
            return False

    def _get_select_tag_element(self, locator: tuple) -> Select:
        return Select(self._find_element_for_wait(locator))

    def _scroll_up_on_mobile(self, start_position: float = 0.7, end_position: float = 0.3):
        size = self.driver.get_window_size()
        start_y = size["height"] * start_position
        end_y = size["height"] * end_position

        start_x = size["width"] / 2

        self.driver.swipe(start_x, start_y, start_x, end_y, 600)

    def _scroll_down_on_mobile(self, start_position: float = 0.7, end_position: float = 0.3):
        size = self.driver.get_window_size()
        start_y = size["height"] * start_position
        end_y = size["height"] * end_position

        start_x = size["width"] / 2

        self.driver.swipe(start_x, end_y, start_x, start_y, 600)

    def _click_using_javascript_executor(self, locator: tuple):
        element = self._find_element_for_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def _change_window_taps(self, tap_index: int):
        self.driver.switch_to.window(self.driver.window_handles[tap_index])

    def _convert_string_to_int(self, text: str) -> int:
        return int(re.sub(r"[^0-9]", "", text))

    def _pull_to_refresh_on_mobile(self):
        self._scroll_up_on_mobile(0.9, 0.3)
