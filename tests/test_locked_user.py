from selenium import webdriver
from selenium.webdriver.common.by import By


def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")
    password = driver.find_element(By.ID, "password")

    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.is_displayed()
    assert "locked out" in error_message.text

    driver.quit()