import os
import datetime


def capture_screenshot(driver, test_name):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.path.dirname(__file__), '../failed_screenshots', screenshot_name)
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)
    return screenshot_path
