#!/usr/bin/python3
""" A little bit of geometrics """


class BaseGeometry:
    """ The basic elements of geometry """
    def area(self):
        """ Return an exception for some reason """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Ensure input value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
