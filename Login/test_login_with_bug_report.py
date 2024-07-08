import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime


class BugReportTemplate:
    def __init__(self):
        self.template = """
        Bug Report
        ==========
        Title: {title}
        Date: {date}
        Reported by: {reporter}

        Description:
        ------------
        {description}

        Steps to Reproduce:
        -------------------
        1. {step1}
        2. {step2}
        3. {step3}

        Expected Result:
        ----------------
        {expected_result}

        Actual Result:
        --------------
        {actual_result}

        Severity: {severity}
        Priority: {priority}
        """

    def generate_report(self, details):
        return self.template.format(
            title=details['title'],
            date=details['date'],
            reporter=details['reporter'],
            description=details['description'],
            step1=details['step1'],
            step2=details['step2'],
            step3=details['step3'],
            expected_result=details['expected_result'],
            actual_result=details['actual_result'],
            severity=details['severity'],
            priority=details['priority']
        )


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://tutorialsninja.com/demo/index.php?route=account/login')
    yield driver
    driver.quit()


def capture_screenshot(driver, test_name):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.path.dirname(__file__), 'failed_screenshots', screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    return screenshot_path


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


def generate_bug_report(test_name, exception, screenshot_path):
    details = {
        'title': f"Bug in {test_name}",
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'reporter': 'Muntasir Abdullah',
        'description': f"An exception occurred: {str(exception)}",
        'step1': 'Open the login page.',
        'step2': 'Enter the username and password.',
        'step3': 'Click the login button.',
        'expected_result': 'User should be logged in successfully.',
        'actual_result': 'An error occurred during the login process.',
        'severity': 'High',
        'priority': 'High'
    }

    template = BugReportTemplate()
    report = template.generate_report(details)

    bug_report_name = f"{test_name}_bug_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    bug_report_path = os.path.join(os.path.dirname(__file__), 'bug_reports', bug_report_name)
    os.makedirs(os.path.dirname(bug_report_path), exist_ok=True)

    with open(bug_report_path, 'w') as file:
        file.write(report)

    print(f"Bug report generated: {bug_report_path}")


def test_login_valid_credentials(driver):
    test_name = 'test_login_valid_credentials'
    try:
        login(driver, 'mail123@gmail.com', '1234536')
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
