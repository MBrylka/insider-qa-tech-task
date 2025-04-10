class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()
    
    def is_visible(self, by, value):
        element = self.find_element(by, value)
        return element.is_displayed()