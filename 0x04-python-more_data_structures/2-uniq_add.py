#!/usr/bin/python3
def uniq_add(my_list=[]):
    if (my_list):
        num = 0
        new = set(my_list)
        for i in new:
            num += i
        return num
