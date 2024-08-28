import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestMetadataEntry:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://your-platform-url/metadata")

    def teardown_method(self):
        self.driver.quit()

    def test_enter_valid_metadata(self):
        title_element = self.driver.find_element(By.ID, "title")
        title_element.send_keys("Valid Title")
        description_element = self.driver.find_element(By.ID, "description")
        description_element.send_keys("This is a valid description.")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        success_message = self.driver.find_element(By.ID, "success-message")
        assert "Metadata saved successfully" in success_message.text

    def test_enter_invalid_metadata(self):
        title_element = self.driver.find_element(By.ID, "title")
        title_element.clear()
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "error-message")
        assert "Title is required" in error_message.text
