from selenium.webdriver.common.by import By


class NaverHomePageLocator:
    """
    네이버홈페이지 로케이터입니다.
    """

    QUERY_INPUT = (By.ID, 'query')
    SHORTCUT_AREA = (By.ID, 'shortcutArea')