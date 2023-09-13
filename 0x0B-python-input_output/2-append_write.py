#!/usr/bin/python3
"""Module appends to a file in python
and creates a new file if the file does not exist
"""


def append_write(filename="", text=""):
    """appends text to a text file
    creates new file if file does not exist
    """
    with open(filename, "a+", encoding="utf-8") as file1:
        return file1.write(text)
