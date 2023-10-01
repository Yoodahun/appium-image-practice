from src.page_factory import PageFactory
from selenium.webdriver import ActionChains, Keys


class WebPageFactory(PageFactory):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    def refresh_window(self):
        self.driver.refresh()

    def scroll_to_element(self, locator:tuple):
        element = self._find_element_for_wait(locator)

        self.action.move_to_element(element).perform()

    def press_enter(self):
        self.action.send_keys(Keys.RETURN).perform()



