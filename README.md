# Test Automation System

This project contains a test automation script written in Python using Selenium. The script captures screenshots of failed tests, generates bug reports in Word format, and sends them to developers.


## Directories and Files

- **bug_report_generator/**: Contains scripts for generating bug reports.
  - `login_bug_report_generator.py`: Script to generate bug reports for login-related issues.
  
- **bug_report_templates/**: Contains templates for bug reports.
  - `login_bug_report_template.py`: Template for login-related bug reports.
  
- **bug_reports/**: Stores generated bug reports.
  - `test_login_valid_credentials_bug_report.docx`: Example bug report for login test with valid credentials.
  
- **failed_screenshots/**: Stores screenshots captured during failed tests.
  - `test_login_valid_credentials_20240709.png`: Screenshot for a failed login test with valid credentials.
  
- **tests/**: Contains test scripts.
  - `test_login.py`: Script to test the login functionality.
  
- **utils/**: Contains utility scripts.
  - `email_utils.py`: Utilities for sending emails.
  - `screenshot_utils.py`: Utilities for capturing screenshots.
  
- **requirements.txt**: Lists the dependencies required to run the project.

## Prerequisites

- Python 3.x
- pip

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your Selenium WebDriver. For example, download the ChromeDriver and place it in your PATH.

## Running Tests

To run the tests, execute the following command:
```sh
pytest
```

## Capturing Screenshots and Generating Bug Reports
When a test fails, the script will automatically capture a screenshot and generate a bug report in the bug_reports/ directory. The screenshot will be saved in the failed_screenshots/ directory.

## Sending Bug Reports
The email_utils.py script contains utilities for sending the generated bug reports via email to developers. Ensure you have configured the email settings in the script(email_utils.py) before sending emails.
