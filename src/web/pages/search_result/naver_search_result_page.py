from src.web.locators.search_result.naver_search_result_page_locator import NaverSearchResultPageLocator
from src.web.pages.web_page_factory import WebPageFactory


class NaverSearchResultPage(WebPageFactory, NaverSearchResultPageLocator):
    """
    네이버 검색결과화면의 페이지클래스입니다.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_query_area(self, text:str)->bool:
        """
        검색창의 텍스트가 유지되어있는지를 체크합니다.
        입력받은 텍스트와 검색창에 입력되어있는 텍스트가 동일한지를 체크합니다.
        :param text: str
        :return: bool
        """
        print(self._find_element(self.QUERY_INPUT_IN_SEARCH_RESULT_PAGE).get_attribute("value"))
        return self._is_visible(self.QUERY_INPUT_IN_SEARCH_RESULT_PAGE) and self._find_element(self.QUERY_INPUT_IN_SEARCH_RESULT_PAGE).get_attribute("value") == text


