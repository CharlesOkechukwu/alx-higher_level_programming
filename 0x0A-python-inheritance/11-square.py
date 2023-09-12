#!/usr/bin/python3
"""Module creates a class square
which is a subclass of the class
Rectangle and inherits its attributes
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a subclass of Rectangle
    inherits all the arrtributes of Rectangle and
    BaseGeometry
    """
    def __init__(self, size):
        """initialize size of square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print square using magic str"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
