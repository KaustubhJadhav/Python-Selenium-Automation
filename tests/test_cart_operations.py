import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@allure.title("Test: Add Product to Cart After Sorting (Low to High)")
def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/v1/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url, "Login failed or inventory page not reached"

    sort_select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_select.select_by_visible_text("Price (low to high)")
    time.sleep(1)

    first_product = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text

    first_product.find_element(By.CLASS_NAME, "btn_inventory").click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Cart count is not updated to 1 after adding product"

    allure.attach(
        f"Product Added: {product_name} - {product_price}",
        name="Cart Item Info",
        attachment_type=allure.attachment_type.TEXT
    )

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_item_names = [item.text for item in cart_items]

    assert product_name in cart_item_names, "Product not found in cart after adding"
