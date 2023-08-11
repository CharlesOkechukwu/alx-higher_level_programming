#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    nlen = len(sys.argv) - 1
    argv = sys.argv
    if nlen < 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if (argv[2] == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        exit(0)
    elif (argv[2] == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        exit(0)
    elif (argv[2] == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        exit(0)
    elif (argv[2] == "/"):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
