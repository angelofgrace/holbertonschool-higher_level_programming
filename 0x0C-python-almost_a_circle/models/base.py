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
        """ Convert list of instances of a Base child class to json string """
        inheritorList = []
        with open("{}.json".format
                  (cls.__name__), "w") as inheritorsFile:
            if list_objs is None or len(list_objs) is 0:
                inheritorsFile.write("[]")
            else:
                for elem in list_objs:
                    inheritorList.append(cls.to_dictionary(elem))
                inheritorsFile.write(cls.to_json_string(inheritorList))

    @staticmethod
    def from_json_string(json_string):
        """ Convert JSON string from file to list of inheritor instances """
        newInheritorList = []
        if json_string is None or len(json_string) is 0:
            return newInheritorList
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Instantiate a dummy and update via dict """
        if cls.__name__ is "Square":
            dummy = cls(1, 0, 0)
        else:
            dummy = cls(1, 1, 0, 0)
        dummy.update(**dictionary)
        return dummy
