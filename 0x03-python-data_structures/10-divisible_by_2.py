#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    confirm multiples of two
    """
    if (my_list):
        new_list = []
        for i, num in enumerate(my_list):
            if (num % 2 == 0):
                new_list = new_list + [True]
            else:
                new_list += [False]
        return new_list
