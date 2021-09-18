#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 1:
        print("{:d} argument:".format(n))
    elif n == 0:
        print("{:d} argument.".format(n))
    else:
        print("{:d} arguments:".format(n))
    for i in range(1, n + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
