#!/usr/bin/python3
""" Convert an object(string) to JSON representation """

import json


def to_json_string(my_obj):
    """ Return my_obj as a JSON string """

    return json.dumps(my_obj)
