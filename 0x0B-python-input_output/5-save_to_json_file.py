#!/usr/bin/python3
"""Module to save object to json file
convert object to json before saving
"""
import json


def save_to_json_file(my_obj, filename):
    """Save python object to json file

    my_obj: The object to be saved

    filename: json file object is saved to
    """
    j_str = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file1:
        file1.write(j_str)
