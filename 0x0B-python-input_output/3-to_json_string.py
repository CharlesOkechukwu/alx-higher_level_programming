#!/usr/bin/python3
"""Module that converts python object to JSON
string and return the JSON string
"""
import json


def to_json_string(my_obj):
    """Convert python object to
    json string
    """
    return json.dumps(my_obj)
