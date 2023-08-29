#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    print only integers
    """
    count = 0
    try:
        for i in range(x):
            if (isinstance(my_list[i], int)):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
    except IndexError:
        print("Index out of range")
    finally:
        return count
