from src.page_factory import PageFactory


class WebPageFactory(PageFactory):
    
    def __init__(self, driver):
        super().__init__(driver)

    def refresh_window(self):
        self.driver.refresh()


