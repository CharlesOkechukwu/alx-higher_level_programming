#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class which is a subclass of base
    it inherits all the attribute of Base Class


    contains private attributes:
    __width
    __height
    __x
    __y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """intialize private variables"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of private class attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set value of private attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of __y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle using height and width property"""
        for r in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Override __str__ method and return string representation of class"""
        string = "[Rectangle]"
        string += f" ({self.id}) {self.__x}/{self.__y}"
        string += f" - {self.__width}/{self.__height}"
        return string
