#!/usr/bin/python3
"""Module is a class that inherits
form BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class is a subclass of
    BaseGeometry, with its own private variables
    """
    def __init__(self, width, height):
        """Initialize private attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
