#!/usr/bin/python3
""" Create an object from a 'JSON file' """

import json


def load_from_json_file(filename):
    """ Create a new object from a JSON representation """

    """ Read a JSON string from a file """
    with open(filename, "r") as jsonFile:
        pyObj = json.loads(jsonFile.read())
    """ Convert JSON string to a python object """

    """ Return python object """
    return pyObj
