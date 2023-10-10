#!/usr/bin/python3
"""Create a class with attributes"""


class Student(object):
    """Student class with attributes:
    firstname;
    lastname;
    age;
    """
    def __init__(self, first_name, last_name, age):
        """initialize attributes of student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict rep<F2>resentation of student class"""
        d_attr = self.__dict__
        obj = dict()
        if type(attrs) is list:
            for att in attrs:
                if type(att) is not str:
                    return d_attr
                if att in d_attr:
                    obj[att] = d_attr[att]
            return obj
        return d_attr
