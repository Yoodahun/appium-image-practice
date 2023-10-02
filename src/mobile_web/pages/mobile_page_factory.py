from src.page_factory import PageFactory
from selenium.webdriver import ActionChains, Keys


class MobileWebPageFactory(PageFactory):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    def press_enter(self):
        self.action.send_keys(Keys.ENTER).perform()
