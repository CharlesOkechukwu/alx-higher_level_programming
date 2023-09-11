#!/usr/bin/python3
"""Module t create mylist a sub class of list
prints list in sorted order
"""


class MyList(list):
    """My List a subclass of list
    prints out list in sorted order
    """
    def print_sorted(self):
        """Prints sorted list of parent"""
        print(sorted(self))
