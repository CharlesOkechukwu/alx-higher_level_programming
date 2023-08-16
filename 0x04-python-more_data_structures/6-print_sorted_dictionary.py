#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    sort dictionary by keys in alphabetical order
    """
    sort_dict = dict(sorted(a_dictionary.items()))
    keys = sort_dict.keys()
    for k in keys:
        print("{}: {}".format(k, sort_dict[k]))
