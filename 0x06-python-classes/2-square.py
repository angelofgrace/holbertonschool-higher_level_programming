#!/usr/bin/python3
""" Store some shapes """


class Square:
    """ A classy square """
    def __init__(self, size=0):
        """ Initialization of private size variable """
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
