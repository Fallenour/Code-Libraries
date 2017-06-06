'''

Author: Logan Hicks, (Fallenour)
Contact Information: Fallenour@yahoo.com, Skype: Fallenour
Date Created: 5/6/2017
Date Last Updated: 5/6/2017
Code Source: Derivative
Coded In: Python





############   Intended Purpose of this program   ############

This snippet creates a simple Function with IF ELSE ELIF statement
in python.

Output of Program:

"Feature not loaded, skipping feature"

##############################################################

'''





def selection_boxes(answer):
    if answer == "Checked":
        return "Loading Feature 1"
    elif answer == "Unchecked":          
        return "Feature not loaded, skipping feature"
    else:
        return "Invalid input detected"
		
print selection_boxes("Unchecked")