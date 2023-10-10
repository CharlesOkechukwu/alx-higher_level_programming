#!/usr/bin/python3
"""Write to a file in python
retrun number of characters written
"""


def write_file(filename="", text=""):
    """writes to a text file and return number of characters written"""
    with open(filename, "w") as file1:
        return file1.write(text)
