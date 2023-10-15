from selenium.webdriver.common.by import By


class NaverSearchResultPageLocator:
    """
    네이버 검색결과페이지 로케이터입니다.
    """

    QUERY_INPUT_IN_SEARCH_RESULT_PAGE = (By.ID, 'nx_query')