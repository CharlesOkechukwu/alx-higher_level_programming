#!/usr/bin/python3
"""A class that defines a rectangle
an empty class
"""


class Rectangle:
    """Rectangle class
    contains an empty class
    """
    def __init__(self, width=0, height=0):
        """initiate attributes for Rectangle class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height value setter function"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
