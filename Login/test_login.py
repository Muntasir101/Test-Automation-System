import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Set up the web driver (make sure to specify the correct path to your WebDriver)
    driver = webdriver.Firefox()
    driver.get('https://tutorialsninja.com/demo/index.php?route=account/login')
    yield driver
    driver.quit()


def login(driver, email, password):
    wait = WebDriverWait(driver, 10)

    # Wait for the username field to be present
    wait.until(EC.presence_of_element_located((By.NAME, 'email')))

    # Find and fill the username field
    username_field = driver.find_element(By.NAME, 'email')
    username_field.clear()
    username_field.send_keys(email)

    # Find and fill the password field
    password_field = driver.find_element(By.NAME, 'password')
    password_field.clear()
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
    login_button.click()


def test_login_valid_credentials(driver):
    login(driver, 'mail123@gmail.com', '123456')
    WebDriverWait(driver, 10).until(EC.url_changes('https://tutorialsninja.com/demo/index.php?route=account/login'))
    assert driver.current_url == 'https://tutorialsninja.com/demo/index.php?route=account/account'


def test_login_invalid_email(driver):
    login(driver, 'invalid_email', '123456')
    error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text


def test_login_invalid_password(driver):
    login(driver, 'mail123@gmail.com', 'invalid_password')
    error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text


def test_login_empty_email(driver):
    login(driver, '', '123456')
    error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text


def test_login_empty_password(driver):
    login(driver, 'mail123@gmail.com', '')
    error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text