'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/7/2017
Date Last Updated: 5/7/2017
Code Source: http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
Coded In: Python





############   Intended Purpose of this program   ############

This snippet creates a list, and utilizes the zip function
to print out the index as well as the variabale in the two lists
in Python.

Output:

20.0% red
30.0% green
10.0% blue
40.0% purple


***   Additional Note   ***

Zip function is used when the index (relative position)
of the data in question DOES NOT matter. Please note that
zip with different size lists will stop after the shortest list 
runs out of items.

E.G If the zip function is used, and list 1 has twenty entries,
and list 2 has twelve entries, zip function will stop for loop
after the 12th entry is looped.

##############################################################

'''





colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))
