#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for i in str:
        char = ord(i)
        if ((char > 96) and (char < 123)):
            upper = char - 32
            new_str += chr(upper)
        else:
            new_str += i
    print("{}".format(new_str))
