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
            self.__width = value

        @property
        def height(self):
            """getter of private attribute height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter of height"""
            self.__height = value

        @property
        def x(self):
            """getter of private attribute x"""
            return self.__x

        @x.setter
        def x(self, value):
            """set value of private attribute x"""
            self.__x = value

        @property
        def y(self):
            """getter of private attribute y"""
            return self.__y

        @y.setter
        def y(self, value):
            """set the value of __y"""
            self.__y = value
