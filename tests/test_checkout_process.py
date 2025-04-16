import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@allure.title("Test: Complete Checkout Process")
def test_checkout_process(driver):
    driver.get("https://www.saucedemo.com/v1/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url, "Login failed"

    sort = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort.select_by_visible_text("Price (low to high)")
    time.sleep(1)

    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    product_name = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    first_item.find_element(By.CLASS_NAME, "btn_inventory").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url, "Cart page not loaded"

    driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()

    assert "checkout-step-one" in driver.current_url, "Checkout Step 1 not loaded"

    driver.find_element(By.ID, "first-name").send_keys("Kaustubh")
    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.XPATH, "//input[@value='CONTINUE']").click()


    assert "checkout-step-two" in driver.current_url, "Checkout Step 2 not loaded"
    driver.find_element(By.XPATH, "//a[@class='btn_action cart_button']").click()


    complete_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    allure.attach(complete_header, name="Order Confirmation", attachment_type=allure.attachment_type.TEXT)

    assert "THANK YOU FOR YOUR ORDER" in complete_header.upper(), "Order not confirmed"

    allure.attach(driver.get_screenshot_as_png(), name="Checkout Confirmation", attachment_type=allure.attachment_type.PNG)
