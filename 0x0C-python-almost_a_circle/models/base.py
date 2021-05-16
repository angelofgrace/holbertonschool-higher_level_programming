#!/usr/bin/python3
""" Foundation parent class for shapes """

import json


class Base:

    """ Base shape class, instantiation, methods, attributes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation, id optional, iterating count as default id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert instance dictionary to JSON string """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        inheritorList = []
        for elem in list_objs:
            inheritorList.append(cls.to_dictionary(elem))
        with open("{}.json".format
                  (cls.__name__), "w") as inheritorsFile:
            if list_objs is None:
                return inheritorList
            else:
                inheritorsFile.write(cls.to_json_string(inheritorList))
