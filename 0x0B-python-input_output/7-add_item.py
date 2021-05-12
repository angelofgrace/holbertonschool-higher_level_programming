#!/usr/bin/python3
""" Add command line args to a Python list and save them to a file """

import sys
import json
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    """ Add all agrv args to a Python list, save to a JSON file """

    PyList = []
    TargetFile = "add_item.json"

    if os.path.exists(TargetFile):
        if os.path.getsize(TargetFile) is not 0:
            """ Load from existing JSON fil to pyobj """
            PyList.extend(load_from_json_file(TargetFile))
    else:
        """ Create new JSON file """
        j = open(TargetFile, "x")
        j.close()
    """ Append argvs to list """
    for i in range(1, len(sys.argv)):
        PyList.append(sys.argv[i])
    """ convert new Python list to JSON str, save to add_item JSON file """
    save_to_json_file(PyList, TargetFile)
