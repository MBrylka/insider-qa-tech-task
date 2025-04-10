from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from config import settings

class OpenPositionsPage(BasePage):

    select_by_location_xpath = (By.XPATH, '//select[@id="filter-by-location"]')
    select_by_department_xpath = (By.XPATH, '//select[@id="filter-by-department"]')
    jobs_list_xpath = (By.XPATH, "//div[@id='jobs-list']")
    job_list_item_xpath = (By.XPATH, "//div[contains(@class, 'position-list-item')]")
    job_list_item_location_label_xpath = (By.XPATH, "//div[contains(@class, 'position-location')]")
    job_list_item_department_label_xpath = (By.XPATH, "//span[contains(@class,'position-department')]")
    view_role_xpath = (By.XPATH, "//a[text()[contains(., 'View Role')]]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = settings.OPEN_POSITIONS_PAGE_URL

    def open(self):
        self.open_url(self.url)

    def verify_page_is_loaded(self):
        assert "https://useinsider.com/careers/open-positions" in self.get_current_url().lower()

    def _select_from_dropdown(self, option_text):
        option_xpath = (By.XPATH, f'//li[text()[contains(., "{option_text}")]]')
        self.click(*option_xpath)

    def filter_by_location(self, location):
        select_element = self.find_element(*self.select_by_location_xpath)
        select = Select(select_element)
        select.select_by_visible_text(location)

    def filter_by_department(self, department):
        select_element = self.find_element(*self.select_by_department_xpath)
        select = Select(select_element)
        select.select_by_visible_text(department)

    def verify_job_list_is_filtered_by(self, filter_type, filter_value):
        job_list = self.find_element(*self.jobs_list_xpath)
        job_items = job_list.find_elements(*self.job_list_item_xpath)

        for job_item in job_items:
            if filter_type == "location":
                location_label = job_item.find_element(*self.job_list_item_location_label_xpath)
                assert location_label.text == filter_value
            elif filter_type == "department":
                department_label = job_item.find_element(*self.job_list_item_department_label_xpath)
                assert department_label.text == filter_value
            else:
                raise ValueError("Invalid filter type specified.")
            
    def click_on_view_offer(self):
        job_list = self.find_element(*self.jobs_list_xpath)
        job_item = job_list.find_elements(*self.job_list_item_xpath)[0]
        hover = ActionChains(self.driver).move_to_element(job_item)
        hover.perform()
