import smtplib
from email.mime.text import MIMEText
from dotenv import dotenv_values

config = dotenv_values(".env")

EMAIL_ADDRESS = config['EMAIL_ADDRESS']
PASS = config['PASS']
RECEIPIENTS = config['RECEIPIENTS']

msg = MIMEText('There was a connection error detected in the AD Connector')
msg['Subject'] = 'AD Connector Error notification'
msg['From'] = 'josgabfer@gmail.com'
msg['To'] = RECEIPIENTS

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,PASS)



print('login success')
server.sendmail(sender, receivers, msg.as_string())
print("Email has been sent to: ", receivers)

