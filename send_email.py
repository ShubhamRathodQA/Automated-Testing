import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender_email = "shubhamrathod172000@gmail.com"
    receiver_email = "rathodshubhamqa@gmail.com"
    password = "kohu iafh afsv himb"

    # Create the email headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Send the email using SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server here
        server.starttls()  # Enable encryption
        server.login(sender_email, password)  # Log in to your email account
        server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
send_email("Test Results", "All tests passed! No issues found.")

####