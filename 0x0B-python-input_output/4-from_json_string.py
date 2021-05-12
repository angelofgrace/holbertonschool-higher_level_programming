#!/usr/bin/python3
""" Convert from JSON string to associated python object """

import json


def from_json_string(my_str):
    """ Return the Python object equivalent of input json my_str """

    return json.loads(my_str)
