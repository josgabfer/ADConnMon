import smtplib
from email.mime.text import MIMEText
from dotenv import dotenv_values

config = dotenv_values(".env")
passw = config['PASS']


sender = 'josgabfer@gmail.com'
receivers = 'jduartef@cisco.com'

msg = MIMEText('There was a connection error detected in the AD Connector')
msg['Subject'] = 'AD Connector Error notification'
msg['From'] = 'josgabfer@gmail.com'
msg['To'] = 'jduartef@cisco.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,passw)

print('login success')
server.sendmail(sender, receivers, msg.as_string())
print("Email has been sent to: ", receivers)

