from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CareersPage(BasePage):

    teams_xpath = (By.XPATH, "//h3[text()[contains(., 'Find your calling')]]")
    life_at_insider_xpath = (By.XPATH, "//h2[text()[contains(., 'Life at Insider')]]")

    def verify_page_is_loaded(self):
        assert "https://useinsider.com/careers" in self.get_current_url().lower()
        assert self.is_visible(*self.teams_xpath)
        assert self.is_visible(*self.life_at_insider_xpath)
