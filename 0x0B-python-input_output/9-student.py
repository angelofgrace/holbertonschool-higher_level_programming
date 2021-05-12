#!/usr/bin/python3
""" Student Class instantiation and method to find instance dictionary """


class Student:
    """ A Student is many things, namely, named """

    def __init__(self, first_name, last_name, age):
        """  Establish public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Find all methods and attributes of given instance """
        return self.__dict__
