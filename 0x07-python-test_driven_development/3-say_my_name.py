#!/usr/bin/python3
"""This module prints a name
and returns none
"""

def say_my_name(first_name, last_name=""):
    """This function prints out two strings
    after verifying they are strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print("My name is {} {}".format(first_name, last_name))
