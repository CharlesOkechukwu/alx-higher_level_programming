#!/usr/bin/python3
def islower(c):
    alph = ord(c)
    if (alph > 96) and (alph < 123):
        return True
    else:
        return False
