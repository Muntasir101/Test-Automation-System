import yagmail

def send_email(report_path, to_email):
    yag = yagmail.SMTP('test@gmail.com', 'nnsw mynz')  # password must be an app password
    subject = "Automated Bug Report"
    contents = "Please find the attached bug report."
    yag.send(to_email, subject, contents, attachments=[report_path])
    print(f"Bug report sent to {to_email}")
