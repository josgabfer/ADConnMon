import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values
import mmap


config = dotenv_values(".env")

EMAIL_ADDRESS = config['EMAIL_ADDRESS']
PASS = config['PASS']
RECIPIENTS = config['RECIPIENTS']

FOLDER = r''
FILE = FOLDER + '\\' + ''

def send_email():
    """This function will send an alert to the desired recipients"""
    msg = EmailMessage()
    msg['Subject'] = 'AD Connector Error Found!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENTS
    msg.set_content('Connection Error found in the AD connector, please check your Umbrella Dashboard and connectivity to all DCs')

    msg.add_alternative("""
    <!DOCTYPE >
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AD Connector Monitor</title>
    </head>
    <body>
        <h1>AD Connector Error</h1>
        <p>The AD Connector Monitor script detected a connectivity error, it is recommended to check your Umbrella dashboard.</p>

        <style type="text/css">
            body{
                margin: 0;
                background-color: #cccccc;
            }
        </style>
        
    </body>
    </html>
    """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,PASS)
        print('login success')
        smtp.send_message(msg)
        print("Email has been sent to: ", RECIPIENTS)

def scan_file():
    """This function will read the [] file and check for errors, if errors are detected send_mail() will be called"""
    errors = ['Exception', 'Failed to sync!', 'ADSync CheckDiff error']
    

    with open (FILE, 'rb', 0) as file:
        s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        for error in errors:
            location = s.find(bytes(error, 'utf-8'))
            if location != -1:
                print("Error logs detected")
                send_email()
                break
                
            else:
                print("No errors found.")

    

if __name__ == '__main__':
    scan_file()

