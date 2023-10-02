from selenium.webdriver.common.by import By


class NaverHomePageLocator:
    QUERY_INPUT_BEFORE_CLICK = (By.XPATH, "//input[@id='MM_SEARCH_FAKE']")
    QUERY_INPUT_AFTER_CLICK = (By.XPATH, "//input[@id='query']")
    SHORTCUT_AREA = (By.XPATH, "//div[@id='HOME_SHORTCUT']")
