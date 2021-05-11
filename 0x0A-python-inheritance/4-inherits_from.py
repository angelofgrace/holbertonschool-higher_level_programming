#!/usr/bin/python3
""" Does an object inherit from a given class """


def inherits_from(obj, a_class):
    """ Return T/F, determine if obj inherits from a_class """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
