from selenium.webdriver.common.by import By


class NaverHomePageLocator:
    """
    모바일웹 네이버홈페이지 로케이터 클래스입니다.
    """
    QUERY_INPUT_BEFORE_CLICK = (By.XPATH, "//input[@id='MM_SEARCH_FAKE']")
    QUERY_INPUT_AFTER_CLICK = (By.XPATH, "//input[@id='query']")
    SHORTCUT_AREA = (By.XPATH, "//div[@id='HOME_SHORTCUT']")
