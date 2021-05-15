#!/usr/bin/python3
""" A square is just a straightedge Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square has all the attributes of a Rectangle """

    attrs = ["id", "size", "x", "y"]

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiate a Square, size all 4 sides, id defined or automated """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        astring = "[Square] ({}) {}/{} - {}"\
                  .format(self.id, self.x, self.y, self.width)
        return astring

    def update(self, *args, **kwargs):
        """ No-keyword arguments for Rectangle """
        if args:
            arguments = []
            for x in args:
                arguments.append(x)
            for (a, b) in zip(attrs, arguments):
                setattr(self, a, b)
        else:
            for argKey in kwargs.keys():
                setattr(self, argKey, kwargs[argKey])

    def to_dictionary(self):
        """ Create a dictionary representation of a Rectangle """
        attrDict = {}
        for item in self.attrs:
            attrDict[item] = getattr(self, item)
        return attrDict

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validate("width", self.width)
        self.width = value
        self.height = value
