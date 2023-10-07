from src.page_factory import PageFactory


class AndroidPageFactory(PageFactory):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


