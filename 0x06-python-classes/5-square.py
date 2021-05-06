#!/usr/bin/python3
""" Store some shapes """


class Square:
    """ A classy square """
    def __init__(self, size=0):
        """ Instantiation of private size variable """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ Retrieve the value using getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size using setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Print a # square the of self.size """
        print("\n".join(["#" * self.__size for i in range(0, self.__size)]))

    def area(self):
        """ Multiple size by size to find area of a Square """
        return self.__size * self.__size
