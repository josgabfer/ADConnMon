# AD Connector Monitor

The AD Connector Monitor script sends email alerts when it detects an AD connector in error state.  
This is achieved by sending a GET request to https://api.umbrella.com/deployments/v2/virtualappliances to get all the AD integration components (VAs, DCs and AD connectors) from the dashboard. After this, the script checks the status of all AD connectors in the dashboard and if it finds an AD connector in error state, it will send an email alert to the specified recipients.

## Installation

Use git to clone the repository files to your machine:

```bash
git clone https://github.com/josgabfer/ADConnMon.git
```

## Files

ADConnectorMonitor.py - this python file perform 3 tasks:  
    1) Send a GET request to https://api.umbrella.com/deployments/v2/virtualappliances to get a list of all the AD integration components in the Umbrella dashboard.  
    2) Check the status of all AD connectors.  
    3) Send email alerts if it detects an AD connector in error state.  

getToken.py - this python file will take care of generating a new authentication token if needed.

.env - this file is not included in the repository files since it needs to be created locally on the machine. The .env file is where we store the parameters that the ADConnectorMonitor.py file needs to work. Please follow the next instructions:  
    1) Create the .env file in the same location where the ADConnectorMonitor.py is stored and copy & paste the following text and fill:  
        EMAIL_ADDRESS = ''  
        PASS = ''  
        RECIPIENTS = ''  
        KEY = ''  
        SECRET = ''  
    2) Add the values between the '' for each parameter:  
        EMAIL_ADDRESS: the sender's email address  
        PASS: password created by the sender that authorizes applications send  
        RECIPIENTS: the recipient's email address that will receive the email alerts (If you plan on adding more than one recipient, please use a coma to separate each email address)  
        KEY: API Key obtained from the Umbrella dashboard (Make sure that the API Key you created has "Virtual Appliances" included in the Key scope)  
        SECRET: Key secret  

## Usage

You can run the script

## Usage

Run the script manually:
```python
Windows: python ADConnectorMonitor.py
Mac: python3 ADConnectorMonitor.py
```

Run the script automatically:
Multiple tools can be used to automate the script execution, however, this is up to the user as we don't recommend any specific ways to achieve automation. Here is an example on how to use the Task Scheduler in windows to automate python script executions: https://www.jcchouinard.com/python-automation-using-task-scheduler/
