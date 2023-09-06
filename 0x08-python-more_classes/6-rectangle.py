#!/usr/bin/python3
"""A class that defines a rectangle
an empty class
"""


class Rectangle:
    """Rectangle class
    contains an empty class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initiate attributes for Rectangle class"""
        Rectangle.number_of_instances += 1
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

    def area(self):
        """calculates and returns area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate and return the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            peri = (self.__height + self.__width) * 2
            return peri

    def __draw(self):
        """Draw a rectangle using height and width"""
        rect = ''
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if i < self.__height - 1:
                rect += '\n'
        return rect

    def __str__(self):
        """print string version"""
        return self.__draw()

    def __repr__(self):
        """rpr initiator function"""
        rec_h = str(self.__height)
        rec_w = str(self.__width)
        return "Rectangle(" + rec_w + ", " + rec_h + ")"

    def __del__(self):
        """print message when class is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
