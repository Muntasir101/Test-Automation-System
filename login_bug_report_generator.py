import os
import datetime
from login_bug_report_template import BugReportTemplate
from email_utils import send_email


def generate_bug_report(test_name, exception, screenshot_path):
    details = {
        'title': f"Bug in {test_name}",
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'reporter': 'Automated Test',
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

    bug_report_name = f"{test_name}_bug_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
    bug_report_path = os.path.join(os.path.dirname(__file__), 'bug_reports', bug_report_name)
    os.makedirs(os.path.dirname(bug_report_path), exist_ok=True)

    template.generate_report(details, screenshot_path, bug_report_path)

    print(f"Bug report generated: {bug_report_path}")
    send_email(bug_report_path, 'receiver@gmail.com')
