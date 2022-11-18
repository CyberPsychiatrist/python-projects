from email.message import EmailMessage
from secure import password

import ssl
import smtplib

email_sender = "janedoe@gmail.com"
email_password = password

email_receiver = ''

subject = "First Email with Python"
body = """Python is fun, we can send email with it."""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
