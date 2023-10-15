from src.mobile_web.locators.home.naver_home_page_locator import NaverHomePageLocator
from src.mobile_web.pages.mobile_page_factory import MobileWebPageFactory


class NaverHomePage(MobileWebPageFactory, NaverHomePageLocator):
    """
    모바일웹 네이버홈페이지 클래스입니다.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_shortcut_area_is_visible(self) -> bool:
        """
        모바일웹 네이버 홈페이지 검색창 하단의 숏컷 영역이 노출되는지를 확인합니다.
        :return: bool
        """
        print(self.SHORTCUT_AREA)
        return self._is_visible(self.SHORTCUT_AREA)

    def search_text(self, text: str):
        """
        모바일웹 네이버 홈페이지에서 검색창을 클릭한 다음, 검색어를 입력하고 검색합니다.
        :param text: str
        :return:
        """
        self._click(self.QUERY_INPUT_BEFORE_CLICK)
        self._input(self.QUERY_INPUT_AFTER_CLICK, text)
        self.press_enter()
