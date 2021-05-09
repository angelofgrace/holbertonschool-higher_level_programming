#!/usr/bin/python3
""" We're printing squares again """


def print_square(size):
    """ Printing is for squares """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for length in range(0, size):
        for height in range(0, size):
            print("#", end = "")
        print("")
