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


def gather_bug_details():
    title = input("Enter bug title: ")
    date = input("Enter date (YYYY-MM-DD): ")
    reporter = input("Enter your name: ")
    description = input("Enter bug description: ")
    step1 = input("Enter step 1 to reproduce: ")
    step2 = input("Enter step 2 to reproduce: ")
    step3 = input("Enter step 3 to reproduce: ")
    expected_result = input("Enter the expected result: ")
    actual_result = input("Enter the actual result: ")
    severity = input("Enter the severity (Low/Medium/High/Critical): ")
    priority = input("Enter the priority (Low/Medium/High): ")

    return {
        "title": title,
        "date": date,
        "reporter": reporter,
        "description": description,
        "step1": step1,
        "step2": step2,
        "step3": step3,
        "expected_result": expected_result,
        "actual_result": actual_result,
        "severity": severity,
        "priority": priority
    }


def generate_bug_report(details, template):
    return template.format(
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


if __name__ == "__main__":
    template = BugReportTemplate().template
    details = gather_bug_details()
    report = generate_bug_report(details, template)
    print(report)
