import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDocumentUpload:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://your-platform-url/upload")

    def teardown_method(self):
        self.driver.quit()

    def test_upload_valid_document(self):
        upload_element = self.driver.find_element(By.ID, "upload")
        upload_element.send_keys("/path/to/valid_document.pdf")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        success_message = self.driver.find_element(By.ID, "success-message")
        assert "Upload Successful" in success_message.text

    def test_upload_invalid_format(self):
        upload_element = self.driver.find_element(By.ID, "upload")
        upload_element.send_keys("/path/to/invalid_document.txt")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "error-message")
        assert "Invalid format" in error_message.text

    def test_upload_exceeds_size(self):
        upload_element = self.driver.find_element(By.ID, "upload")
        upload_element.send_keys("/path/to/large_document.pdf")
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "error-message")
        assert "File exceeds the maximum size" in error_message.text
