import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values, find_dotenv
from getToken import generate_auth_string
import requests
from requests.models import HTTPError
from termcolor import colored
import http.client as http_client


config = dotenv_values(".env")

EMAIL_ADDRESS = config['EMAIL_ADDRESS']
PASS = config['PASS']
RECIPIENTS = config['RECIPIENTS']
count = 0

def send_email(connectorName):
    """This function will send an alert to the desired recipients"""
    msg = EmailMessage()
    msg['Subject'] = 'AD Connector Error Found!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENTS
    msg.set_content(f'Connection Error found in {connectorName}. Please check your Umbrella Dashboard and connectivity to all DCs')

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
        <p>The AD Connector Monitor script detected an error with: """ + connectorName + """. Please check your Umbrella dashboard.</p>

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

def get_request(): 
    """This function will send a GET request to get a list of all AD integration components"""
    url = "https://api.umbrella.com/deployments/v2/virtualappliances"
    global count
    count += 1
    if (count == 3):
        print(colored(f"\nMaximum attempts to reach {url} exceeded", "red"))
        return
    config = dotenv_values(find_dotenv())
    token = config.get('TOKEN')
    if (token == None):
        token = (generate_auth_string())
    headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }
    print(colored(f"Contacting API: {url}", "green"))
    print("\n")

    try:
        response = requests.get(url, headers=headers)
        if (response.status_code == 401 or response.status_code == 403):
            token = generate_auth_string()
            return get_request()
        elif (response.status_code == 200):
            print(colored("Get request successfully executed!", "green"))
            print("\n")
            return response.json()
    except HTTPError as httperr:
        print(colored(f'HTPP error occured: {httperr}','red'))
        

    except Exception as e:
        print(colored(f'HTPP error occured: {e}','red'))

def alert():
    """This function will search for all the AD connectors in error state to call the send email function"""
    adComponents = get_request()
    for component in adComponents:
        if (component.get("type") == "connector" and component.get("health") == "error"):
            send_email(component.get("name"))

if __name__ == '__main__':
    alert()
