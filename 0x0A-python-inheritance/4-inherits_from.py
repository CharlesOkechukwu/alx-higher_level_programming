#!/usr/bin/python3
"""Module to chcek for subclass
or inheritance
"""


def inherits_from(obj, a_class):
    """Function return true if object is
    a class that inherited from or a
    class the object class inherited from
    its class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
