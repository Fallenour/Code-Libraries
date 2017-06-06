'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/7/2017
Date Last Updated: 5/7/2017
Code Source: http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
Coded In: Python





############   Intended Purpose of this program   ############

This snippet creates a list, and utilizes the zip function
to print out the index as well as the variable in the two lists
in Python.

Output:

20.0% red
30.0% green
10.0% blue
40.0% purple


***   Additional Note   ***

Enumerate function is used when the index (relative position)
of the data in question matters. For instance, if you absolutely
need to ensure that data from one table matches with the same 
position as data in another table. E.G. Data in field 3 of list1
is a matching pair with data in field 3 of list2.

##############################################################

'''





colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))
