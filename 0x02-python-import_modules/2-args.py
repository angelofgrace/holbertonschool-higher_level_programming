#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv)-1))
    else:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    for x in sys.argv:
        if i > 0:
            print("{:d}: {:s}".format(i, x))
        i += 1
