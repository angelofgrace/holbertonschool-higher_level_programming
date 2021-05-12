#!/usr/bin/python3
""" Input/Output task 1: write a file to stdout """


def write_file(filename="", text=""):
    """ Write a given string to a writable file and return # chars written """
    with open(filename, mode="w", encoding="utf-8") as WriteMe:
        return WriteMe.write(text)
