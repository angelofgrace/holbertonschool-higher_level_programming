#!/usr/bin/python3
""" Creating classes of shapes """


class Rectangle:
    """ A class of Rectangles """

    def __init__(self, width=0, height=0):
        """ Istantiation of Rectangle object with optional height and width """
        if type(height) is not int or type(width) is not int:
            raise TypeError("width must be an integer")
        if height < 0 or width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter function for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter function for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter function for width """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
