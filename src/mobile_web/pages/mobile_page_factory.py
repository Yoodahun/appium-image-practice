from src.page_factory import PageFactory
from selenium.webdriver import ActionChains, Keys


class MobileWebPageFactory(PageFactory):
    """
    모바일웹 페이지를 구현할 때 상속받아야하는 MobileWebPageFactory 입니다.

    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def press_enter(self):
        self.action.send_keys(Keys.ENTER).perform()
