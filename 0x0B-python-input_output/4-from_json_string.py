#!/usr/bin/python3
"""Module converts a json string to
a python object abd returns it
"""
import json


def from_json_string(my_str):
    """Converts json string to python object

    my_str: json string to convert

    Returns: python object
    """
    return json.loads(my_str)
