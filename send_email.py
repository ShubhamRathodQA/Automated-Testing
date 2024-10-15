def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'shubhamrathod172000@gmail.com'
    msg['To'] = 'sandip90306@gmail.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('shubhamrathod172000@gmail.com', 'Gmail.com!')
        server.send_message(msg)

def check_test_results(test_passed):
    if test_passed:
        subject = "Test Results: Passed"
        body = "Congratulations! All tests have passed successfully."
    else:
        subject = "Test Results: Failed"
        body = "Some tests have failed. Please check the code for errors."

    send_email(subject, body)

# Example usage based on test result
test_passed = False  # Simulate test result
check_test_results(test_passed)