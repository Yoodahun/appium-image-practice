from src.page_factory import PageFactory


class AndroidPageFactory(PageFactory):
    """
    안드로이드 앱에서 페이지를 구현할 때 상속받아야하는 AndroidPageFactory 클래스 입니다.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


