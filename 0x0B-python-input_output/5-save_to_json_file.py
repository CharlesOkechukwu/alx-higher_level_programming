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
    with open(filename, "w", encoding="utf-8") as file1:
        json.dump(my_obj, file1)
