#!/usr/bin/python3
"""Module to read a file in python
retruns read content
"""


def read_file(filename=""):
    """Read file content in python
    and print to stdout
    """
    with open(filename, "r", encoding="utf-8") as file1:
        content = file1.read()
    print(content, end="")
