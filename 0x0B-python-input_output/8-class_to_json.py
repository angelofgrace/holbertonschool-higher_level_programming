#!/usr/bin/python3
""" Return the dictionary description of a class for JSON obj serialization """


def class_to_json(obj):
    """ Return dict description of obj class instance for JSON serialzation """
    return obj.__dict__
