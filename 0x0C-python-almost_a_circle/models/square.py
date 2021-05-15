#!/usr/bin/python3
""" A square is just a straightedge Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square has all the attributes of a Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiate a Square, size all 4 sides, id defined or automated """
        super().__init__(size, size, x, y, id)
