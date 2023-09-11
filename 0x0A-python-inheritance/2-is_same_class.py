#!/usr/bin/python3
"""Module to confirm if an object
is the instance of a class
"""


def is_same_class(obj, a_class):
    """Check if an object is an instance
    of a_class, return true or false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
