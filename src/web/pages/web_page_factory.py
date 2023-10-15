from src.page_factory import PageFactory
from selenium.webdriver import Keys


class WebPageFactory(PageFactory):
    """
    웹페이지들의, 각 페이지 클래스들이 상속받는 WebPageFactory 클래스입니다.
    실제 페이지를 구현할 때 이 페이지를 상속받아 구현해야합니다.
    """
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def refresh_window(self):
        """
        현재 열린 브라우저를 새로고침합니다.
        :return:
        """
        self.driver.refresh()

    def scroll_to_element(self, locator:tuple):
        """
        wait를 사용하여 특정 element를 확인한 다음, 해당 element의 위치로 action 객체를 사용하여 이동합니다.
        :param locator:
        :return:
        """
        element = self._find_element_for_wait(locator)

        self.action.move_to_element(element).perform()

    def press_enter(self):
        """
        웹에서 action객체를 이용하여 return키를 입력합니다.
        :return:
        """
        self.action.send_keys(Keys.RETURN).perform()



