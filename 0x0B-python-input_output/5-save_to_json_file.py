#!/usr/bin/python3
""" Write an object to a text file, using JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ Convert my_obj to JSON represenation and write it to filename """

    """ JSON Conversion """
    jsonStr = json.dumps(my_obj)

    """ Open filename, write to filename """
    with open(filename, mode="w", encoding="utf-8") as WritFile:
        WritFile.write(jsonStr)
