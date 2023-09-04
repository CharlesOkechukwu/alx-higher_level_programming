#!/usr/bin/python3

"""a module that adds integers
"""


def add_integer(a, b=98):
    """Adds two integers together
    ensure var a is an int or float
    ensures var b is an int or float
    before adding and returning the value
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif (type(b) != int) and (type(b) != float):
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
