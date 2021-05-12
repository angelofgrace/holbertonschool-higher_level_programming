#!/usr/bin/python3
""" Input/Output excercise 0: read a file """


def read_file(filename=""):
    """ Open a readable file and print it to stdout """

    with open(filename, mode="r", encoding="utf-8") as theFile:
        print(theFile.read(), end="")
