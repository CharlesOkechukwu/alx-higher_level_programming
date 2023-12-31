#!/usr/bin/python3
"""This module prints a square
"""


def print_square(size):
    """This function prints a square
    using '#' and the variable size
    size must be an integer
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == int and size < 0:
        raise ValueError("size must be >= 0")
    if size < 1 and size >= 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
