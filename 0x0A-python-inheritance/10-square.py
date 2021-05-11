#!/usr/bin/python3
""" All squares are rectangles, not all rectangles are squares """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Rectangle where all sides are equal """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.__size = size

    def area(self):
        return self.__size ** 2
