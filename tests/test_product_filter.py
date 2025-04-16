import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@allure.title("Test: Product Sorting - Price Low to High")
def test_product_sorting_low_to_high(driver):
    driver.get("https://www.saucedemo.com/v1/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url, "Did not reach inventory page"

    sort_select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_select.select_by_visible_text("Price (low to high)")

    item_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    names = [item.text for item in item_names]
    prices = [float(price.text.replace("$", "")) for price in item_prices]

    product_list = "\n".join([f"{name} - ${price:.2f}" for name, price in zip(names, prices)])
    allure.attach(product_list, name="Sorted Product List", attachment_type=allure.attachment_type.TEXT)

    assert prices == sorted(prices), "Product prices are not sorted correctly (Low to High)"
