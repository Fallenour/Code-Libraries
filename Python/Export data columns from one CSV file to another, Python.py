'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/7/2017
Date Last Updated: 5/7/2017
Code Source: various
Coded In: Python





############   Intended Purpose of this program   ############

Utilize Python to import data from a CSV file to export specified
data columns from specified CSV file, and write those data columns
to a different, specified CSV file.

OUTPUT:

Print list of Firstname, Lastname, and Email. This tests data sample.

Columns 1-17, CSVFILE1 > FirstName,LastName,Email,PhysicalAddress,
PhysicalCity,PhysicalState,PhysicalZip,HomePhone,WorkPhone,
CellPhone > CSVFILE2

*** Additional Note ***

PANDAS module is useful for working with aggregating datasets
together in order to insert data into databases utilizing the 
mongodb and mysql libaries using import mongodb or import Mysql,
respective to the database desired. 



##############################################################

'''

		 
import csv
exampleFile = open('C:/Users/lhicks/Documents/Corporate/test.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData



import pandas as pd
df = pd.read_csv('C:/Users/lhicks/Documents/Corporate/test.csv', 'r')
saved_column = df.FirstName
saved_column2 = df.LastName
saved_column3 = df.Email

print saved_column
print saved_column2
print saved_column3


Itemlist = [] 
Itemlist.append(saved_column)


print Itemlist






import pandas as pd
fn = 'C:/Users/lhicks/Documents/Corporate/test.csv'
cols = ['FirstName','LastName','Email','PhysicalAddress','PhysicalCity','PhysicalState','PhysicalZip','HomePhone','WorkPhone','CellPhone']
df = pd.read_csv(fn, usecols=cols)

df.to_excel('C:/Users/lhicks/Documents/Corporate/test2.xlsx', index=False)

#if you want to control how many rows should Pandas print:
with pd.option_context("display.max_rows",200):
	print(df)