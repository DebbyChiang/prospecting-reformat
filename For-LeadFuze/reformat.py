#import libraries
import pandas as pd
import numpy as np

#import file
prospects = pd.DataFrame(pd.read_csv("/Users/open/Desktop/prospects.csv"))

#Drop Unnecessary columns
dropped_columns = [
   'picture',
   'twitter',
   'facebook',
   'phone-number',
   'linkedin'
]

prospects = prospects.drop(dropped_columns, axis = 1)

#Rename column names
renamed_columns = {
	'first': 'First Name', 
    'last': 'Last Name', 
    'title': 'Title', 
    'email': 'Email',
    'domain': 'Website',
    'phone-number': 'Phone',
    'company': 'Company'
}

prospects = prospects.rename(columns = renamed_columns)

#Insert missing columns
prospects['Campaign Start Date'] = ""
prospects['Department'] = ""
prospects['# of ppl in Target City'] = "" 
prospects['# of ppl'] = ""
prospects['Lead Owner'] = ""
prospects['Rating'] = ""
prospects['Notes'] = ""
prospects['Hook'] = ""
prospects['Industry'] = ""
prospects['Address'] = ""
prospects['City'] = ""
prospects['State'] = ""
prospects['Postal Code'] = ""
prospects['Country'] = ""
prospects['Hook'] = ""
prospects['Email Type'] = ""

#reorder columns
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

#export --> CSV
prospects.to_csv('/Users/open/Desktop/reformatted.csv')

