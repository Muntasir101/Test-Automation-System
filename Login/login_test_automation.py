from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify browser
driver = webdriver.Firefox()

# Open the target login page
url = 'https://tutorialsninja.com/demo/index.php?route=account/login'
driver.get(url)


def login_test(username, password):
    try:
        # Wait until the username field is present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))

        # Find the username field and enter the username
        username_field = driver.find_element(By.NAME, 'email')
        username_field.clear()
        username_field.send_keys(username)

        # Find the password field and enter the password
        password_field = driver.find_element(By.NAME, 'password')
        password_field.clear()
        password_field.send_keys(password)

        # Find the login button and click it
        login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
        login_button.click()

        # Wait until the login process completes and the next page is loaded
        WebDriverWait(driver, 10).until(EC.url_changes(url))

        # Verify if login was successful
        success_url = 'https://tutorialsninja.com/demo/index.php?route=account/account'
        if driver.current_url == success_url:
            print('Login successful')
        else:
            print('Login failed')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    # Replace with valid credentials
    username = 'mail123@gmail.com'
    password = '123456'

    login_test(username, password)
