#!/usr/bin/python3
""" Input/Output task 2 Append given text to a file """


def append_write(filename="", text=""):
    """ Write given text to the end of a file """
    with open(filename, mode="a", encoding="utf-8") as AppendMe:
        return AppendMe.write(text)
