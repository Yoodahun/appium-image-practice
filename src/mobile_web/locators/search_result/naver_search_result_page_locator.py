from selenium.webdriver.common.by import By


class NaverSearchResultPageLocator:
    """
    모바일웹 네이버 검색결과페이지 로케이터 클래스입니다.
    """
    QUERY_INPUT_IN_SEARCH_RESULT_PAGE = (By.XPATH, "//input[@id='nx_query']")
