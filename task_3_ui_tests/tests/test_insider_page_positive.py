from pages.landing_page import LandingPage
from pages.careers_page import CareersPage
from pages.careers.quality_assurance_page import QualityAsurancePage

def test_careers_link(driver):
    landing_page = LandingPage(driver)
    careers_page = CareersPage(driver)

    landing_page.open()
    
    landing_page.click_menu_item("Company")
    landing_page.click_menu_item("Careers")
    
    careers_page.verify_page_is_loaded()


def test_career_page_job_filtering(driver):
    qa_page = QualityAsurancePage(driver)
    
    qa_page.open()
    
    qa_page.verify_page_is_loaded()
