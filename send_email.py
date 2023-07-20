import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "bhaveshgadag46@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = "bhaveshgadag46@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == '__main__':
    test_message = f"""\
Subject: Test email

From :test@example.com
This is a test email from gmail smtp.
"""

    test_receiver = "bhaveshgadag46@gmail.com"
    send_mail(test_receiver, test_message)
