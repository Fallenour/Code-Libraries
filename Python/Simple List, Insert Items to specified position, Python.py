'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/7/2017
Date Last Updated: 5/7/2017
Code Source: Derivative
Coded In: Python





############   Intended Purpose of this program   ############

This snippet creates a list named Items, creates Item1 through
Item5, checks to see if Item3 exists, and what position in the
list it is in, and then prints Item3's position in the list. It
also sets Item_index equal to that position number.

It then puts Item6 in the position that Item3 was previously in,
pushing Item3 down a position (from 2 to 3).

Output:

['Item1', 'Item2', 'Item6', 'Item3', 'Item4', 'Item5']

##############################################################

'''





Items = ["Item1", "Item2", "Item3", "Item4", "Item5"]
Item_index = Items.index("Item3")
print Item_index

Items.insert(Item_index,"Item6")


print Items