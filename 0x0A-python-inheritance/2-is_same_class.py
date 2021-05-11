#!/usr/bin/python3
""" Check if an object is an instance of a class """


def is_same_class(obj, a_class):
    """ Is input object an instance of input a_class """
    return type(obj) == a_class
