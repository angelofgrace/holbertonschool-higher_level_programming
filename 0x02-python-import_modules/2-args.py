#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    else:
        i = 0
        for x in sys.argv:
            if i > 0:
                print("{:d}: {:s}".format(i, x))
            i += 1
