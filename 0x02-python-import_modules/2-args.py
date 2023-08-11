#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1
    i = 1
    if (num == 0):
        print("{:d} arguments.".format(num))
    elif (num >= 1):
        if (num == 1):
            print("{:d} argument:".format(num))
        else:
            print("{:d} arguments:".format(num))
        for s in range(1, num + 1):
            print("{:d}: {}".format(i, sys.argv[s]))
            i += 1
