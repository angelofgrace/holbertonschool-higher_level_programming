#!/usr/bin/python3
""" Student Class instantiation and method to find instance dictionary """


class Student:
    """ A Student is many things, namely, named """

    def __init__(self, first_name, last_name, age):
        """  Establish public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Find and store all methods and attributes of given instance """
        if attrs is None:
            return self.__dict__
        else:
            stdDict = {}
            for att in attrs:
                if att in self.__dict__:
                    """ Set new dict key/element pair to   """
                    stdDict[att] = self.__dict__[att]
            return stdDict

    def reload_from_json(self, json):
        """ Retrieve and rpelace all attributes for new instance """
        """ Iterate through dict json to reassign attributes """
        for key in json.keys():
            self.__dict__[key] = json[key]
