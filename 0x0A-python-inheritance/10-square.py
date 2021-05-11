#!/usr/bin/python3
""" All squares are rectangles, not all rectangles are squares """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle where all sides are equal """

    def __init__(self, size):
        """ Receive and validate size, the length of all sides """
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.__size = size

    def area(self):
        """ Area of a square """
        return self.__size ** 2

    def __str__(self):
        """ A simpler print string """
        return "[Square] {}/{}".format(self.__size, self.__size)
