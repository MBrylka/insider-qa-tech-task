class BrowserHelper:
    def __init__(self, driver):
        self.driver = driver
    
    def check_if_tab_containg_url_is_open(self, text):
        browserTabs = self.driver.window_handles
        self.driver.switch_to.window(browserTabs[1])
        current_url = self.driver.current_url
        assert text in current_url