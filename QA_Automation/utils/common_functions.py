from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, element_id, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, element_id))
    )

def fill_input_field(driver, field_id, text):
    field = driver.find_element(By.ID, field_id)
    field.clear()
    field.send_keys(text)
