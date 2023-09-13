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

    def to_json(self):
        """return dict representation of student class"""
        return self.__dict__
