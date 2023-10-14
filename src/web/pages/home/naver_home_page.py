from src.web.locators.home.naver_home_page_locator import NaverHomePageLocator
from src.web.pages.web_page_factory import WebPageFactory


class NaverHomePage(WebPageFactory, NaverHomePageLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_shortcut_area_is_visible(self)->bool:

        return self._is_visible(self.SHORTCUT_AREA)

    def search_text(self, text:str):
        self._input(self.QUERY_INPUT, text)
        self.press_enter()