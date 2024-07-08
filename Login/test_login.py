import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime


def capture_screenshot(driver, test_name):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.path.dirname(__file__), 'failed_screenshots', screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)


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
    test_name = 'test_login_valid_credentials'
    try:
        login(driver, 'mail123@gmail.com', '123456')
        WebDriverWait(driver, 10).until(EC.url_changes('https://tutorialsninja.com/demo/index.php?route=account/login'))
        assert driver.current_url == 'https://tutorialsninja.com/demo/index.php?route=account/account'
    except Exception as e:
        capture_screenshot(driver, test_name)
        raise e


def test_login_invalid_email(driver):
    test_name = 'test_login_invalid_email'
    try:
        login(driver, 'invalid_email', '123456')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        capture_screenshot(driver, test_name)
        raise e


def test_login_invalid_password(driver):
    test_name = 'test_login_invalid_password'
    try:
        login(driver, 'mail123@gmail.com', 'invalid_password')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        capture_screenshot(driver, test_name)
        raise e


def test_login_empty_email(driver):
    test_name = 'test_login_empty_email'
    try:
        login(driver, '', 'invalid_password')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        capture_screenshot(driver, test_name)
        raise e


def test_login_empty_password(driver):
    test_name = 'test_login_empty_password'
    try:
        login(driver, 'mail123@gmail.com', '')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        capture_screenshot(driver, test_name)
        raise e
