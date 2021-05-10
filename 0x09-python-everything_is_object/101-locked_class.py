#!/usr/bin/python3
""" Receive names but nothing else """


class LockedClass:
    """ Class for names that prevents new attribute creation"""

    __allowed_attributes=('first_name')

    def __setattr__(self, attribute, value):
        if not attribute in self.__allowed_attributes:
            raise AttributeError
        else:
            super().__setattr__(attribute, value)
