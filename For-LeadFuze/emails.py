#import libraries 
import pandas as pd
import numpy as np

#import file
prospects = pd.DataFrame(pd.read_csv("/Users/open/Desktop/department.csv"))

#Drop rows with no company
prospects = prospects.dropna(subset=['Company']) 

#Copy orange emails into 'Test Email 1'
prospects['Test Email 1'] = ""

prospects['Test Email 1'] = prospects['Email'] 


#Delete orange emails in original column/filter green emails
prospects['Email'] = ""

#Reorder columns
prospects = prospects.drop('Unnamed: 0', axis = 1)
cols = ['Company', 
        'First Name', 
        'Last Name', 
        'Title', 
        'Department', 
        '# of ppl in Target City', 
        '# of ppl', 
        'Lead Owner', 
        'Industry', 
        'Email', 
        'Test Email 1', 
        'Rating', 
        'Notes', 
        'Address', 
        'City', 
        'State', 
        'Postal Code', 
        'Country', 
        'Phone', 
        'Website', 
        'Hook', 
        'Email Type']

prospects = prospects[cols]

#Set up Full Contact API
import requests
import json

api_key = 'xxx'
url = "https://api.fullcontact.com/v2/person.json"

def whois(**kwargs):
    if 'xxx' not in kwargs:
        kwargs['xxx'] = api_key
    r = requests.get(url, params=kwargs)
    return json.loads(r.text)

#Prepare emails for testing
orange = list(prospects['Test Email 1'])
green = list(prospects['Email'])

#Test emails
for i in range(0, len(orange)):
    email = orange[i]
    parameters = {
        'email': email,
        'apiKey': 'xxx'
    }
    response = requests.get('https://api.fullcontact.com/v2/person.json', parameters)
    data = json.loads(response.text)
    if data['status'] == 200:
        green[i] = orange[i]
        orange[i] = "" 

#Replace emails
prospects['Email'] = green
prospects['Test Email 1'] = orange

#Export file 
prospects.to_csv('/Users/open/Desktop/emails.csv')



