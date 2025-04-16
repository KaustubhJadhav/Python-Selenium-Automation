from selenium import webdriver
import os

def get_driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    temp_profile = os.path.join(os.getenv("TEMP"), "chrome-temp-profile")
    options.add_argument(f"incognito")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver

