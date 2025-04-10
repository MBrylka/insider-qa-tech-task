from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CareersPage(BasePage):

    teams_section_xpath = (By.XPATH, "//section[@id='career-find-our-calling']")
    locations_section_xpath = (By.XPATH, "//section[@id='career-our-location']")
    life_at_insider_xpath = (By.XPATH, "//h2[text()[contains(., 'Life at Insider')]]")

    def verify_page_is_loaded(self):
        assert "https://useinsider.com/careers" in self.get_current_url().lower()
        assert self.is_visible(*self.teams_section_xpath)
        assert self.is_visible(*self.locations_section_xpath)
        assert self.is_visible(*self.life_at_insider_xpath)
