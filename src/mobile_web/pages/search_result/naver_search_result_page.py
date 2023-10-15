from src.mobile_web.locators.search_result.naver_search_result_page_locator import NaverSearchResultPageLocator
from src.mobile_web.pages.mobile_page_factory import MobileWebPageFactory


class NaverSearchResultPage(MobileWebPageFactory, NaverSearchResultPageLocator):
    """
    모바일 웹 네이버의 검색결과페이지 입니다.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_query_area(self, text:str)->bool:
        """
        모바일웹 검색결과페이지에서 검색창에 검색어가 존재하는지를 확인합니다.
        :param text: str
        :return: bool
        """
        print(self._find_element(self.QUERY_INPUT_IN_SEARCH_RESULT_PAGE).get_attribute("value"))
        return self._is_visible(self.QUERY_INPUT_IN_SEARCH_RESULT_PAGE) and self._find_element(self.QUERY_INPUT_IN_SEARCH_RESULT_PAGE).get_attribute("value") == text


