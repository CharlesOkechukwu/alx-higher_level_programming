#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1
    argv = sys.argv
    add = 0
    for i in range(1, num + 1):
        add += int(argv[i])
    print("{:d}".format(add))
