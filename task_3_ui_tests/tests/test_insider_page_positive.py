from pages.landing_page import LandingPage
from pages.careers_page import CareersPage
from pages.careers.quality_assurance_page import QualityAsurancePage
from pages.careers.open_positions_page import OpenPositionsPage
from helpers.browser import BrowserHelper
import time

def test_careers_link(driver):
    landing_page = LandingPage(driver)
    careers_page = CareersPage(driver)

    landing_page.open()
    
    landing_page.click_menu_item("Company")
    landing_page.click_menu_item("Careers")
    
    careers_page.verify_page_is_loaded()


def test_career_page_job_filtering(driver):
    qa_page = QualityAsurancePage(driver)
    open_positions_page = OpenPositionsPage(driver)
    browser = BrowserHelper(driver)
    qa_page.open()
    
    qa_page.verify_page_is_loaded()
    qa_page.click_see_all_qa_jobs()
    open_positions_page.verify_page_is_loaded()
    # Not nice but i didnt have time to investigate how page is loading
    # I would need to know the workflow of frontend for reloading the page when filer
    # is selected. For now i applied a sleep but i know it might result in flaky tests
    time.sleep(20) 
    open_positions_page.filter_by_location("Istanbul, Turkiye")
    open_positions_page.filter_by_department("Quality Assurance")
    time.sleep(20)
    open_positions_page.verify_job_list_is_filtered_by("location", "Istanbul, Turkiye")
    open_positions_page.verify_job_list_is_filtered_by("department", "Quality Assurance")
    open_positions_page.click_on_view_offer()
    browser.check_if_tab_containg_url_is_open("https://jobs.lever.co/useinsider")