#!/usr/bin/python3
def best_score(a_dictionary):
    """
    return largest value in a dictionary
    """
    if a_dictionary is None:
        return None
    keys = list(a_dictionary.keys())
    num = a_dictionary[keys[0]]
    key = keys[0]
    for k in keys:
        if (a_dictionary[k] > num):
            num = a_dictionary[k]
            key = k
    return key
