#!/usr/bin/python3
"""Create a base class name Base"""


class Base():
    """Base class which would serve as the base
    of all classes

    contains:
    __nb_objects : a private class attribute

    id : a class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize self and id class attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
