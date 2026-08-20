from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_item_checkout():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")

    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

    add_to_cart_btn.click()
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert cart_item.is_displayed()
    checkout_btn = driver.find_element(By.ID, "checkout")

    checkout_btn.click()
    driver.find_element(By.ID, "first-name").send_keys("Humna")
    driver.find_element(By.ID, "last-name").send_keys("Ahmed")

    driver.find_element(By.ID, "postal-code").send_keys("74200")
    driver.find_element(By.ID, "continue").click()
    overview_title = driver.find_element(By.CLASS_NAME, "title")

    assert overview_title.text == "Checkout: Overview"
    driver.find_element(By.ID, "finish").click()
    success_message = driver.find_element(By.CLASS_NAME, "complete-header")

    assert success_message.is_displayed()
    assert success_message.text == "Thank you for your order!"
    driver.quit()
