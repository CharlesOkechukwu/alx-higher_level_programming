#!/usr/bin/python3
"""Creating a locked class
for an object
"""


class LockedClass(object):
    """LockedClass is an empty class
    Permited attribute: first_name
    """
    __slots__ = 'first_name'
