#import libraries
import pandas as pd
import numpy as np

#import file
prospects = pd.DataFrame(pd.read_csv("/Users/open/Desktop/prospecting.csv"))

#Drop Unnecessary columns
dropped_columns = [
    'Starred', 
    'LinkedIn Company URL',
    'LeadSource',
    'Connections', 
	'Industry',
	'Locality Country', 
	'Locality State Code',
	'Locality State',
	'Locality City', 
	'Locality', 
	'LinkedIn public profile URL', 
	'Size', 
	'Company Formatted Address'
]

prospects = prospects.drop(dropped_columns, axis = 1)

#Rename column names
renamed_columns = {
	'Company Address': 'Address', 
    'Company City': 'City', 
    'Company State': 'State', 
    'Company Postal Code': 'Postal Code', 
	'Company Country': 'Country', 
	'LinkedIn Company Industry': 'Industry'
}

prospects = prospects.rename(columns = renamed_columns)

#Insert missing columns
prospects['Campaign Start Date'] = ""
prospects['Department'] = ""
prospects['# of ppl in NYC'] = "" 
prospects['# of ppl'] = ""
prospects['Lead Owner'] = ""
prospects['Rating'] = ""
prospects['Notes'] = ""
prospects['Hook'] = ""

#reorder columns
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
