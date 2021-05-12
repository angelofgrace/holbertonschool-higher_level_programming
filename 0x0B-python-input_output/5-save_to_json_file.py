#!/usr/bin/python3
""" Write an object to a text file, using JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ Convert my_obj to JSON represenation and write it to filename """

    with open(filename, "w") as WritFile:
        WritFile.write(json.dumps(my_obj))
