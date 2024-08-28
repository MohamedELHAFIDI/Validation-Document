import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDynamicElements:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://your-platform-url/upload")
    
    def teardown_method(self):
        self.driver.quit()

    def test_dynamic_elements_appear(self):
        # Select a specific document type that triggers additional fields
        doc_type_element = self.driver.find_element(By.ID, "document_type")
        doc_type_element.select_by_visible_text("Special Type")
        
        # Wait for the dynamic element to appear
        dynamic_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "dynamic_field"))
        )
        
        # Assertion to check if the dynamic element is visible
        assert dynamic_field.is_displayed()
        
        # Optionally, interact with the dynamic element
        dynamic_field.send_keys("Additional Info")

