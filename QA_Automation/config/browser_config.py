from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

def get_browser_driver(browser_name):
    if browser_name == "chrome":
        return ChromeService()
    elif browser_name == "firefox":
        return FirefoxService()
    elif browser_name == "edge":
        return EdgeService()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")
