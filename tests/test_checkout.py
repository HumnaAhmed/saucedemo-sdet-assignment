from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_item_checkout():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert cart_item.is_displayed()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Humna")
        driver.find_element(By.ID, "last-name").send_keys("Ahmed")
        driver.find_element(By.ID, "postal-code").send_keys("74200")
        driver.find_element(By.ID, "continue").click()

        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Checkout: Overview"))
        overview_title = driver.find_element(By.CLASS_NAME, "title")
        assert overview_title.text == "Checkout: Overview"

        driver.find_element(By.ID, "finish").click()

        success_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert success_message.text == "Thank you for your order!"

    finally:
        driver.quit()
