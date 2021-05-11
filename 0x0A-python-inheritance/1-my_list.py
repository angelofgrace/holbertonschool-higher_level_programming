#!/usr/bin/python3
""" Priting a sorted object that inherits from list """


class MyList(list):
    """ Inherits all methods and attributes from list """

    def print_sorted(self):
        """ prints a sorted copy of instance """
        print(sorted(self))
