#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not bool(a_dictionary):
        return
    del a_dictionary[key]
    return a_dictionary
