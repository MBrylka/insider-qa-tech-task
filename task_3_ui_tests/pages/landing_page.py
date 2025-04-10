from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import settings

class LandingPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = settings.LANDING_PAGE_URL

    def open(self):
        self.open_url(self.url)

    def click_menu_item(self, item):
        menu_item_xpath = (By.XPATH, f'//a[text()[contains(., "{item}")]]')
        self.click(*menu_item_xpath)
