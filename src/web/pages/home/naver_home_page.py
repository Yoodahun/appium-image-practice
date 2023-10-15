from src.web.locators.home.naver_home_page_locator import NaverHomePageLocator
from src.web.pages.web_page_factory import WebPageFactory


class NaverHomePage(WebPageFactory, NaverHomePageLocator):
    """
    네이버 홈페이지를 의미하는 페이지클래스입니다.

    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_shortcut_area_is_visible(self)->bool:
        """
        웹페이지 기준으로, 검색창 하단에 숏컷영역이 노출되는지를 체크합니다.
        :return: bool
        """
        print(self.SHORTCUT_AREA)

        return self._is_visible(self.SHORTCUT_AREA)

    def search_text(self, text:str):
        """
        네이버 검색창에 텍스트를 입력하여 검색합니다.
        :param text: str
        :return:
        """
        self._input(self.QUERY_INPUT, text)
        self.press_enter()