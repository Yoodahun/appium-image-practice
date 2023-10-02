from selenium.webdriver.common.by import By


class NaverSearchResultPageLocator:
    QUERY_INPUT_IN_SEARCH_RESULT_PAGE = (By.XPATH, "//input[@id='nx_query']")
