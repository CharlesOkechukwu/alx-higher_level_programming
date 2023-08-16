#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiply dictionary values by 2
    """
    new_dict = {}
    keys = a_dictionary.keys()
    for k in keys:
        new_dict[k] = a_dictionary[k] * 2
    return new_dict
