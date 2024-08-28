from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_dynamic_element(driver, element_id, timeout=10):
    dynamic_element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, element_id))
    )
    return dynamic_element
