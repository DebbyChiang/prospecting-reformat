#import libraries 
import pandas as pd
import numpy as np

#import file
prospects = pd.DataFrame(pd.read_csv("/Users/open/Desktop/department.csv"))

#Drop rows with no company
prospects = prospects.dropna(subset=['Company']) 

#Copy orange emails into 'Test Email 1'
prospects['Test Email 1'] = ""

prospects.loc[prospects['Email Type'] == "orange", 'Test Email 1'] = \
prospects.loc[prospects['Email Type'] == "orange", 'Email'] 


#Delete orange emails in original column/filter green emails
prospects.loc[prospects['Email Type'] == "orange", 'Email'] = ""

#Reorder columns
prospects = prospects.drop('Unnamed: 0', axis = 1)
cols = ['Company', 
        'First Name', 
        'Last Name', 
        'Title', 
        'Department', 
        '# of ppl in NYC', 
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

#Export file 
prospects.to_csv('/Users/open/Desktop/emails.csv')
