from selenium import webdriver
from selenium.webdriver.common.by import By

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID,"user-name")

    username.send_keys("standard_user")
    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID,"login-button")
    login_button.click()
    successful_element = driver.find_element(By.CLASS_NAME, "title")

    assert successful_element.is_displayed()
    driver.quit()

