'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/7/2017
Date Last Updated: 5/7/2017
Code Source: http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
Coded In: Python





############   Intended Purpose of this program   ############

This snippet creates a list, and utilizes the enumerate function
to print out the index as well as the variabale in the list
in Python.

Output:

President 1: Washington
President 2: Adams
President 3: Jefferson
President 4: Madison
President 5: Monroe
President 6: Adams
President 7: Jackson

***   Additional Note   ***

Enumerate function is used when the index (relative position)
of the data in question matters. For instance, if you absolutely
need to ensure that data from one table matches with the same 
position as data in another table. E.G. Data in field 3 of list1
is a matching pair with data in field 3 of list2.

##############################################################

'''





presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
