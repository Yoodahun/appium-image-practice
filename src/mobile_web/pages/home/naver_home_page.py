from src.mobile_web.locators.home.naver_home_page_locator import NaverHomePageLocator
from src.mobile_web.pages.mobile_page_factory import MobileWebPageFactory


class NaverHomePage(MobileWebPageFactory, NaverHomePageLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_shortcut_area_is_visible(self) -> bool:
        print(self.SHORTCUT_AREA)
        return self._is_visible(self.SHORTCUT_AREA)

    def search_text(self, text: str):
        self._click(self.QUERY_INPUT_BEFORE_CLICK)
        self._input(self.QUERY_INPUT_AFTER_CLICK, text)
        self.press_enter()
