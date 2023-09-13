#!/usr/bin/python3
"""Module to return dictionary description"""


def class_to_json(obj):
    """return dictionary description for class"""
    return obj.__dict__
