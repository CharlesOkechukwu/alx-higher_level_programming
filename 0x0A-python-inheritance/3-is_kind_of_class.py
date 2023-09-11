#!/usr/bin/python3
"""Module checks if an object is
an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """Function to check if an object is an instance of
    or inherited from a specified class
    retruns true or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
