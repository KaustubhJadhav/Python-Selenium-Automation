import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils.read_excel import get_login_data

login_data = get_login_data("data/login_data.xlsx")

@pytest.mark.parametrize("username,password", login_data)
@allure.title("Login Test with Different Credentials")
def test_login(driver, username, password):
    driver.get("https://www.saucedemo.com/v1/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if username == "standard_user" and password == "secret_sauce":
        assert "inventory.html" in driver.current_url, f"Login failed for valid user: {username}"
    else:
        try:
            error_elem = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            error_msg = error_elem.text

            allure.attach(
                error_msg,
                name="Login Error Message",
                attachment_type=allure.attachment_type.TEXT
            )

            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Login Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            assert error_elem.is_displayed(), "Expected error message not displayed."

        except NoSuchElementException:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="No Error Message Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Expected error message for invalid user '{username}', but none found.")
