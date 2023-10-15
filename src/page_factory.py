import re
from typing import List

from appium.webdriver import Remote, WebElement
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from utilities import logger_factory


class PageFactory:
    """
    PageFactory 클래스는 페이지들에서 수행해야할 기본적인 행위들을 정의합니다.
    생성자에서는 드라이버, wait, action, logger 객체를 생성합니다.
    wait 객체는 기본 대기시간 10초입니다.

    """
    def __init__(self, driver):
        self.driver: Remote = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)
        self.logger = logger_factory(type(self).__name__)

    def _find_element(self, locator: tuple) -> WebElement:
        """
        find_element를 수행하여 element를 return합니다.

        :param locator:
        :return:
        """
        return self.driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        """
        find_elements를 수행하여 list형태의 element들을 리턴합니다.
        :param locator:
        :return: List[WebElement]
        """
        return self.driver.find_elements(*locator)

    def _find_element_for_wait(self, locator: tuple) -> WebElement:
        """
        wait를 이용하여 element를 식별하고, 리턴합니다.
        대기시간은 10초이며 조건은 visibility_of_element_located() 입니다.
        :param locator:
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _find_elements_for_wait(self, locator: tuple) -> List[WebElement]:
        """
        wait를 이용하여 element를 식별하고, 찾아낸 element들을 list에 담아 리턴합니다.
        대기시간은 10초이며 조건은 visibility_of_elements_located() 입니다.
        :param locator:
        :return:
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def _get_text(self, locator: tuple) -> str:
        """
        wait를 이용하여 element를 식별한다음, text를 리턴합니다.

        :param locator:
        :return: str
        """
        return self._find_element_for_wait(locator).text

    def _input(self, locator: tuple, text: str):
        """
        wait를 이용하여 element를 식별한 다음, 텍스트값을 입력합니다.
        이때 입력하기 전에, 입력해야하는 element에 대해 clear() 동작을 수행합니다.

        :param locator:
        :param text:
        :return:
        """
        input_element = self._find_element_for_wait(locator)
        input_element.clear()
        input_element.send_keys(text)

    def _click(self, locator: tuple):
        """
        wait를 이용하여 element를 식별한다음, click()을 수행합니다.
        :param locator:
        :return:
        """
        self._find_element_for_wait(locator).click()

    def _is_visible(self, locator: tuple) -> bool:
        """
        wait를 이용하여 element를 식별한다음 is_displayed()를 수행합니다.
        TimeoutException이 발생하는 경우에는 False를 리턴합니다.

        :param locator:
        :return: bool
        """
        try:
            return self._find_element_for_wait(locator).is_displayed()
        except TimeoutException:
            return False

    def _get_select_tag_element(self, locator: tuple) -> Select:
        """
        wait를 이용하여 element를 식별한다음, Select객체를 생성하여 리턴합니다.

        :param locator:
        :return: selenium.webdriver.support.select.Select
        """
        return Select(self._find_element_for_wait(locator))

    def _scroll_up_on_mobile(self, start_position: float = 0.7, end_position: float = 0.3):
        """
        모바일단말기의 화면에서, 단말기의 윈도우사이즈를 계산한다음 화면을 위로 스크롤합니다.
        기본값은 시작위치는 화면 상단으로부터 70%아래에 위치한 부분, 종료위치는 화면 상단으로부터 30% 아래에 위치한 부분입니다.

        :param start_position:
        :param end_position:
        :return:
        """
        size = self.driver.get_window_size()
        start_y = size["height"] * start_position
        end_y = size["height"] * end_position

        start_x = size["width"] / 2

        self.driver.swipe(start_x, start_y, start_x, end_y, 600)

    def _scroll_down_on_mobile(self, start_position: float = 0.7, end_position: float = 0.3):
        """
        모바일단말기의 화면에서, 단말기의 윈도우사이즈를 계산한다음 화면을 위로 스크롤합니다.
        기본값은 시작위치는 화면 상단으로부터 30%아래에 위치한 부분, 종료위치는 화면 상단으로부터 70% 아래에 위치한 부분입니다.

        :param start_position: int
        :param end_position: int
        :return:
        """
        size = self.driver.get_window_size()
        start_y = size["height"] * start_position
        end_y = size["height"] * end_position

        start_x = size["width"] / 2

        self.driver.swipe(start_x, end_y, start_x, start_y, 600)

    def _click_using_javascript_executor(self, locator: tuple):
        """
        javascript executor를 이용하여 해당 element에 대해 click()을 수행합니다.
        element는 wait를 이용하여 식별합니다.
        :param locator:
        :return:
        """
        element = self._find_element_for_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def _change_window_taps(self, tap_index: int):
        """
        현재 열려져있는 브라우저의 윈도우 창을 변경합니다.
        :param tap_index: int

        """
        self.driver.switch_to.window(self.driver.window_handles[tap_index])

    def _convert_string_to_int(self, text: str) -> int:
        """
        숫자가 섞인 문자열 데이터를 정수형 데이터로 변환하여 리턴합니다.
        :param text:
        :return:
        """
        return int(re.sub(r"[^0-9]", "", text))

    def _pull_to_refresh_on_mobile(self):
        """
        모바일 단말기에서 화면 상단을 끌어내려 리프레쉬를 시도하는 동작입니다.
        :return:
        """
        self._scroll_up_on_mobile(0.9, 0.3)
