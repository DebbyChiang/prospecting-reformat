#Code can be shortened by using more string operations

#import libraries
import pandas as pd
import numpy as np

#import csv file
prospects = pd.DataFrame(pd.read_csv("/Users/open/Desktop/reformatted.csv"))

#IT keywords --> fill corresponding Department column/row w/"IT"
#Keyword: CTO
prospects['IT'] = prospects['Title'].str.contains("CTO ")
prospects['IT'] = prospects['Title'].str.contains(" CTO")
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains(" cto")
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("cto ")

#Keyword: Technology
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("Technology")
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("TECHNOLOGY")
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("technology")

#Keyword: IT
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("IT")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" IT")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("IT ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" IT ")

#Keyword: Solution
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("Solution")
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("SOLUTION")
prospects['IT'] = prospects ['IT'] | prospects['Title'].str.contains("solution")

#reference the positions where you want to change the value
prospects.loc[prospects.IT >= 1, 'Department']  = "IT"

#Keyword: Facilities/Facility
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Facilities")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Facilities ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("facilities")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("FACILITIES")
prospects['HR'] = prospects['IT'] | prospects['Title'].str.contains("Facility")
prospects['HR'] = prospects['IT'] | prospects['Title'].str.contains("facility")
prospects['HR'] = prospects['IT'] | prospects['Title'].str.contains("FACILITY")

#Keyword: Sustainability
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Sustainability")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("sustainability")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("SUSTAINABILITY")

#Keyword: Infrastructure
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Infrastructure")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" Infrastructure")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" Infrastructure ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Infrastructure ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("infrastructure")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("INFRASTRUCTURE")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Infrastucture")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("infrastucture")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Infrastucture")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Infrastucture".lower())
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Infrastucture".upper())
 

#Keyword: Systems/System
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Systems")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" Systems")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" Systems ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("systems")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("SYSTEMS")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("System")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("System ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" System")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" System ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("system")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("SYSTEM")

#need this, not sure why
prospects.loc[prospects.IT >= 1, 'Department']  = "IT"

#Keyword: Sys
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Sys")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Sys ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" Sys ")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains(" Sys")


#Keyword: Data
prospects['IT'] =  prospects['Title'].str.contains("Data")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("data")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("DATABASE")

#Keyword: Information
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Information")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("information")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("INFORMATION")


#Keyword: Technical
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("Technical")
prospects['IT'] = prospects['IT'] | prospects['Title'].str.contains("technical")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("TECHNICAL")

#Keyword: Desk
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Desk")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("HDESK")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Desk")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains(" Desk")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("desk ")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains(" desk ")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains(" DESK ")


#Keyword: Networks/network
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Networks")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("networks")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("NETWORKS")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("NetWorks")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Network")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("network")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("NETWORK")

#Keyword: Technologist
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Technologist")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("technologist")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("TECHNOLOGIST")

#Desktop
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Desktop")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("desktop")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("DESKTOP")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("DeskTop")

#Tech 
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("Tech")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("tech")
prospects['IT'] = prospects['IT'] |  prospects['Title'].str.contains("TECH")

#IT Department fill-in, df.loc[<row selection>, <column selection>]
prospects.loc[prospects.IT >= 1, 'Department']  = "IT"

#Human Resources keywords --> fill corresponding Department column/row w/"HR"
#HR Keywords Check

#Keyword: Operations Manager
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Operations Manager")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("operations manager")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("OPERATIONS MANAGER")

#Keyword: Procurement
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Procurement")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("procurement")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("PROCUREMENT")

#Keyword: HR/hris
prospects['HR'] = prospects['Title'].str.contains("HR")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("hr ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains(" hr")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains(" hr ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("hris")

#Keyword: Hiring
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("Hiring")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("hiring")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("hiring ")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("Hiring ")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains(" hiring ")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains(" Hiring")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("HIRING")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("HIRING ")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains(" HIRING")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains(" HIRING ")

#Keyword: Career
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("Career ")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("career")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("CAREER")

#Keyword: Human
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("Human ")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("human")
prospects['HR'] = prospects['HR'] | prospects['Title'].str.contains("HUMAN")


#Keyword: Office
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Office ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("office ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("OFFICE ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Offices ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("offices ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("OFFICES ")

#Keyword: Corporate Social Responsibility - NEED TO TEST 
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Responsibility")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("responsibility")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("RESPONSIBILITY")

#Keyword: CSR - NEED TO TEST
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("CSR")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("csr")

#Keyword: Employee Engagement
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("employee")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Employee")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("EMPLOYEE")

#Keyword: People
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("People")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("people")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("PEOPLE")

#Keyword: Talent
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("talent")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("TALENT")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Talent")

#Keyword: Employee
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Employee")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("employee")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("EMPLOYEE")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Employees")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("employees")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("EMPLOYEES")

#Keyword: Training
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Training")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("training")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("TRAINING")

#Keyword: Receptionist
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Receptionist")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("receptionist")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("RECEPTIONIST")

#Keyword: Leadership Development
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Leadership Development")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("leadership development")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("LEADERSHIP DEVELOPMENT")

#Keyword: Office Services
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Office Services")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("office services")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("OFFICE SERVICES")

#Keyword: Staff
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Staff")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("staff")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("STAFF")

#Keyword: Compensation & Benefits
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Compensation")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("compensation")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("COMPENSATION")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Benefits")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("benefits")

#Keyword: Recruit
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("recruit")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Recruit")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("RECRUIT")


#Keyword: Concierge
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Concierge")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("concierge")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("CONCIERGE")

#Keyword: Offices/Office
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Offices")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("offices")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("OFFICE")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("office ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Office ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("OFFICE ")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains(" Office")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains(" office")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains(" OFFICE")

#Engagement
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Engagement")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("engagement")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("ENGAGEMENT")

#Assistant
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("Assistant")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("assistant")
prospects['HR'] = prospects['HR'] |  prospects['Title'].str.contains("ASSISTANT")

#HR Department fill-in, df.loc[<row selection>, <column selection>]
#>= 1 not 1?
prospects.loc[prospects.HR >= 1, 'Department']  = "HR"

#fill remaining Department column/row with "Executives"
prospects['Department'] = prospects.Department.fillna("Executives")

#Drop unneeded columns
prospects = prospects.drop(['Unnamed: 0', 'IT', 'HR' ], axis = 1)

#Export file 
prospects.to_csv('/Users/open/Desktop/department.csv')
