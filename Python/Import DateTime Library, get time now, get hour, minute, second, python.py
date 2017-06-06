'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/6/2017
Date Last Updated: 5/6/2017
Code Source: Derivative
Coded In: Python





############   Intended Purpose of this program   ############

This snippet imports the datetime library and displays the 
time right now in hours, minutes, and seconds in python.

Format is as follows:

12:11:40

##############################################################

'''





from datetime import datetime
now = datetime.now()
current_hour = now.hour
current_minute = now.minute
current_second = now.second
print '%s:%s:%s' % (now.hour, now.minute, now.second)