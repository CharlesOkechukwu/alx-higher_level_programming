#!/usr/bin/python3
"""Module to convert json file content to
python object
"""
import json


def load_from_json_file(filename):
    """Load json content from json file
    and convert to python object

    filename: the json file to load content from
    """
    with open(filename, "r", encoding="utf-8") as file1:
        return json.load(file1)
