'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/6/2017
Date Last Updated: 5/6/2017
Code Source: Derivative
Coded In: Python





############   Intended Purpose of this program   ############

This snippet creates two functions that identifies the largest
and smallest numbers from a series of arguments that are
defined. The largest number is identified with the 1st function.
The smallest number is identified with the second.

Output:

Largest Number: 100
Smallest Number: -100

##############################################################

'''





def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)


biggest_number(-100, -10, 10, 100)
smallest_number(-100, -10, 10, 100)