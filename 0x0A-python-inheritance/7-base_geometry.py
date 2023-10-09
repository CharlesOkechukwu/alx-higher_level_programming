#!/usr/bin/python3
"""Module for BaseGeometry class
currently empty but would add attributes soon
"""


class BaseGeometry(object):
    """A class for the BaseGeometry
    object contains attributes and
    methods
    """
    def area(self):
        """calculates the area of two objects"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to chcek if
        it is an integer or an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
