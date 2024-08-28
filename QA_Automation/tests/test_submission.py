import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSubmission:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://your-platform-url/review")

    def teardown_method(self):
        self.driver.quit()

    def test_submit_with_missing_fields(self):
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "error-message")
        assert "Please fill out all required fields" in error_message.text

    def test_submit_with_valid_data(self):
        title_element = self.driver.find_element(By.ID, "title")
        title_element.send_keys("Valid Title")
        description_element = self.driver.find_element(By.ID, "description")
        description_element.send_keys("This is a valid description.")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        success_message = self.driver.find_element(By.ID, "success-message")
        assert "Form submitted successfully" in success_message.text
