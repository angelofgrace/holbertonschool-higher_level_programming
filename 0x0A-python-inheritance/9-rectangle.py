#!/usr/bin/python3
""" A little bit of geometrics """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Geometric quadrilateral with two pairs of even sides """
    def __init__(self, width, height):
        """ Instantiation, incl. values to measure sides """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method to find the area of a ssuqare """
        return self.__width * self.__height

    def __str__(self):
        """ More practical str return """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
