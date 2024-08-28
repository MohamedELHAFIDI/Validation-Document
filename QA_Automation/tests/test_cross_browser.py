import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

class TestCrossBrowser:

    def setup_method(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService())
        elif browser == "firefox":
            self.driver = webdriver.Firefox(service=FirefoxService())
        elif browser == "edge":
            self.driver = webdriver.Edge(service=EdgeService())
        self.driver.get("http://your-platform-url/upload")

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
    def test_cross_browser(self, browser):
        self.setup_method(browser)

        upload_element = self.driver.find_element(By.ID, "upload")
        upload_element.send_keys("/path/to/valid_document.pdf")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        success_message = self.driver.find_element(By.ID, "success-message")
        assert "Upload Successful" in success_message.text
        
        self.teardown_method()
