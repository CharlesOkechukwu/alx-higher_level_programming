#!/usr/bin/python3
"""Module to get arguments from stdout
and add them to a list to save them in
a json file
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    arr = load_from_json_file("add_item.json")
except FileNotFoundError:
    arr = []
arr_len = len(sys.argv)
for i in range(1, arr_len):
    arr.append(sys.argv[i])
save_to_json_file(arr, "add_item.json")
