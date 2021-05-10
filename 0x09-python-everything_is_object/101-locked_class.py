#!/usr/bin/python3
""" Receive names but nothing else """


class LockedClass:
    """ Class for names that prevents new attribute creation"""

    __allowed_attributes = ('first_name')

    def __setattr__(self, attribute, value):
        if attribute not in self.__allowed_attributes:
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(attribute))
        else:
            super().__setattr__(attribute, value)
            self.__dict__.clear()
