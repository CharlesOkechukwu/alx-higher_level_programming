#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) > 0) and (type(my_list) is list):
        num = 0
        for i in my_list:
            if (i > num):
                num = i
        return num
    else:
        return None
