'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/6/2017
Date Last Updated: 5/6/2017
Code Source: Derivative
Coded In: Python





############   Intended Purpose of this program   ############

This snippet imports the datetime library and displays the 
date & time right now, then individually displays the year, the month,
and the day in python.

Format is as follows:

2017-05-06 11:56:41.262460
2017
5
6

##############################################################

'''





from datetime import datetime
now = datetime.now()
print datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print current_year
print current_month
print current_day