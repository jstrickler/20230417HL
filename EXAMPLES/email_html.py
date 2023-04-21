from getpass import getpass  # module for hiding password
import smtplib  # module for sending email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

TIMESTAMP = datetime.now().ctime()  # get a time string for the current date/time

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = 'jstrickler@gmail.com,crgnc3@gmail.com'
MESSAGE_SUBJECT = 'Python SMTP example'

PLAIN_BODY = """
Hello at {}.

Testing email from Python
""".format(TIMESTAMP)

HTML_BODY = """
<html>
<head></head>
<body>
<h1>Hello</h1>
<h2>{}</h2>
<h3>Testing email from Python</h3>
<body>
</html>
""".format(TIMESTAMP)

plain_contents = MIMEText(PLAIN_BODY, "text")
html_contents = MIMEText(HTML_BODY, "html")


SMTP_USER = 'pythonclass'
SMTP_PASSWORD = getpass("Enter SMTP server password:")  # get password (not echoed to screen)

smtp = smtplib.SMTP("smtp2go.com", 2525)  # connect to SMTP server
smtp.login(SMTP_USER, SMTP_PASSWORD)  # log into SMTP server

msg = MIMEMultipart('alternative')  # create empty email message
msg['Subject'] = MESSAGE_SUBJECT  # add the message subject
msg['from'] = SENDER  # add the sender address
msg['to'] = RECIPIENTS  # add a list of recipients

msg.attach(plain_contents)
msg.attach(html_contents)

try:
    smtp.sendmail(SENDER, RECIPIENTS, msg.as_string())  # send the message
except smtplib.SMTPException as err:
    print("Unable to send mail:", err)
finally:
    smtp.quit()  # disconnect from SMTP server
