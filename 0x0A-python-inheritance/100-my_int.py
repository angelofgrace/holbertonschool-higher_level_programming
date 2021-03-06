#!/usr/bin/python3
""" What is equal is no longer so """


class MyInt(int):
    """ Switching it up, up in here """

    def __init__(self, value):
        """ Something to compare yourself to """
        super().__init__()
        self.value = value

    def __eq__(self, other):
        """ No longer equals """
        if self.value is other:
            if self.value < 0:
                return False
            else:
                return False
        else:
            return True

    def __ne__(self, other):
        """ Suddenly it equals """
        if self.value is not other:
            if self.value < 0:
                return True
            else:
                return False
        else:
            return True

    def __str__(self):
        return "{}".format(self.value)
