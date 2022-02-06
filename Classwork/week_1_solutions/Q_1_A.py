# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:47:59 2022

@author: Ariel

"""


"""
Q1: 
    A:
        Create a function that converts miles to kilometers and kilometers to miles.
        You should be able to specify whether you want to do a mile or kilometer conversion.
    
    #############
    Where I wrote documentation # lines there is either an important insight or something for you to try as an exercise. This code works and is written with redundencies (also some error testing) but there are places where it could be better and as noted below a case where the same output prints twice for one statement. Consider ways to improve this.
"""
#helper functions:

    
#There is a better way to code these that make more sense with the non general approach this problem is asking. Can you find the way to make this code easier to read?
def unit_converter(unit_dict, unit_request) -> float:
    """
    

    Parameters
    ----------
    unit_dict : dict
        The set of units and the conversion they undergo, given a known conversion space (ie miles to kilometers)
    unit_request : str
        one letter to signify request for type of unit in the unit dict

    Returns
    -------
    TYPE : float
        Return the conversion of the units.

    """
    
    
    try:
        return unit_dict[unit_request]
    except KeyError:
        print(f'the unit requested is invalid, please request an acceptable unit metric from the list {list(unit_dict.keys())}. The current unit supplied is {unit_request.lower()}.')
        return None
        
    

def unit_pretty_convert(unit_name_dict, unit_request):
    #can you try to write an acceptable doc string for this helper function yourself?
    #also note that the try except statement may not be necessary for this toy example if the unit_converter will all ready complain about the same issue.
    try:
        return unit_name_dict[unit_request]
    except KeyError:
        print(f'the unit requested is invalid, please request an acceptable unit metric from the list {list(unit_name_dict.keys())}. The current unit supplied is {unit_request.lower()}.')
        return None

#main function

def distance_convert(distance, unit) -> float:
    """
    

    Parameters
    ----------
    distance : FLOAT
        A distance that is an integer or float value.
    unit : str
        One letter to signifiy a request for kilometers (k) or miles (m). It is assumed that the input received is the opposite of this letter.

    Returns
    -------
    
        A distance with the appropriate unit

    """
    
    allowed_units = {'k' : 1.60934, 'm' : .621371}
    pretty_units = {'k': 'Kilometers', 'm': 'Miles'}
    
    conversion = unit_converter(allowed_units, unit)
    pretty_unit = unit_pretty_convert(pretty_units, unit)
    
    
    #might be a good idea to look up truthy and falsy in python. Also do you think this would be better as a try except conditional? Why or why not?
    if conversion and pretty_unit:
        print(f'your total distance is {round(conversion*distance, 3)} {pretty_unit}')
        return conversion, pretty_unit
    
    print()
    return None

#testing:

if __name__ == "__main__":
    
    test_values = [1,1.5,.6201,17]
    
    distance_convert(test_values[0], 'k')
    distance_convert(test_values[0], 'm')
    distance_convert(test_values[1], 'k')
    distance_convert(test_values[2], 'm')
    distance_convert(test_values[2], 'miles')
    distance_convert(test_values[3], '?')
    distance_convert(test_values[3], 'k')
    
    
    