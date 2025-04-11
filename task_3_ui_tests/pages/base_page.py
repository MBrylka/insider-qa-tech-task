import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def hover_over_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def find_element(self, by, value):
        element = self.is_visible(by, value)
        self.scroll_to_element(element)
        return element

    def click(self, by, value):
        element = self.is_visible(by, value)
        element.click()
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_visible(self, by, value, timeout=30, stablity_duration=1):
        wait = WebDriverWait(self.driver, timeout)
        end_time = time.time() + timeout

        element = wait.until(EC.visibility_of_element_located((by, value)))
        stable_start = None
        while time.time() < end_time:
            try:
                if element.is_displayed():
                    if stable_start is None:
                        stable_start = time.time()
                    elif time.time() - stable_start >= stablity_duration:
                        return element
                else:
                    stable_start = None
                    element = wait.until(EC.visibility_of_element_located((by, value)))
            except StaleElementReferenceException:
                stable_start = None
                element = wait.until(EC.visibility_of_element_located((by, value)))
            time.sleep(0.1)

        raise TimeoutException(f"Element {value} not located")