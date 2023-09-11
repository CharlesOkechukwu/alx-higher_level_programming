#!/usr/bin/python3
"""Module that returns a list of:
    1. Attributes
    2. Methods in a class
    """


def lookup(obj):
    """Lookup function retruns
    a list of arrtributes and methods in an object
    """
    return dir(obj)
