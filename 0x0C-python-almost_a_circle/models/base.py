#!/usr/bin/python3
""" Foundation parent class for shapes """


class Base:
    """ Base shape class, instantiation, methods, attributes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation, id optional, iterating count as default id """
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
