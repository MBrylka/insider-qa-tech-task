from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import settings

class QualityAsurancePage(BasePage):

    qa_title_xpath = (By.XPATH, "//h1[text()[contains(., 'Quality Assurance')]]")
    all_qa_jobs_button_xpath = (By.XPATH, "//a[text()[contains(., 'See all QA jobs')]]")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = settings.CAREERS_QA_PAGE_URL

    def open(self):
        self.open_url(self.url)

    def verify_page_is_loaded(self):
        assert "https://useinsider.com/careers/quality-assurance/" in self.get_current_url().lower()
        assert self.is_visible(*self.qa_title_xpath)
        assert self.is_visible(*self.all_qa_jobs_button_xpath)
