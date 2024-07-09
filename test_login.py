import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_bug_report_generator import generate_bug_report
from screenshot_utils import capture_screenshot


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://tutorialsninja.com/demo/index.php?route=account/login')
    yield driver
    driver.quit()


def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, 'email')))

    username_field = driver.find_element(By.NAME, 'email')
    username_field.clear()
    username_field.send_keys(email)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
    login_button.click()


def test_login_valid_credentials(driver):
    test_name = 'test_login_valid_credentials'
    try:
        login(driver, 'mail123@gmail.com', '1234563')
        WebDriverWait(driver, 10).until(EC.url_changes('https://tutorialsninja.com/demo/index.php?route=account/login'))
        assert driver.current_url == 'https://tutorialsninja.com/demo/index.php?route=account/account'
    except Exception as e:
        screenshot_path = capture_screenshot(driver, test_name)
        generate_bug_report(test_name, e, screenshot_path)
        raise e


def test_login_invalid_email(driver):
    test_name = 'test_login_invalid_username'
    try:
        login(driver, 'invalid_email', '123456')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        screenshot_path = capture_screenshot(driver, test_name)
        generate_bug_report(test_name, e, screenshot_path)
        raise e


def test_login_invalid_password(driver):
    test_name = 'test_login_invalid_password'
    try:
        login(driver, 'mail123@gmail.com', '12345622')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        screenshot_path = capture_screenshot(driver, test_name)
        generate_bug_report(test_name, e, screenshot_path)
        raise e


def test_login_empty_username(driver):
    test_name = 'test_login_empty_username'
    try:
        login(driver, '', '123456')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        screenshot_path = capture_screenshot(driver, test_name)
        generate_bug_report(test_name, e, screenshot_path)
        raise e


def test_login_empty_password(driver):
    test_name = 'test_login_empty_password'
    try:
        login(driver, 'mail123@gmail.com', '')
        error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
        assert 'Warning: No match for E-Mail Address and/or Password.' in error_message.text
    except Exception as e:
        screenshot_path = capture_screenshot(driver, test_name)
        generate_bug_report(test_name, e, screenshot_path)
        raise e
