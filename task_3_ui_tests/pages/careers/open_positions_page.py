from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import settings

class OpenPositionsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = settings.OPEN_POSITIONS_PAGE_URL

    def open(self):
        self.open_url(self.url)

    def verify_page_is_loaded(self):
        assert "https://useinsider.com/careers/open-positions" in self.get_current_url().lower()
