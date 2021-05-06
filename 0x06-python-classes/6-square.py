#!/usr/bin/python3
""" Store some shapes """


class Square:
    """ A classy square """
    def __init__(self, size=0, position=(0,0)):
        """ Instantiation of private size variable """
        if type(position) is not tuple or min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ Retrieve the position using getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position using setter """
        if type(position) is not tuple and min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """ Retrieve the value using getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size using setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Print a # square the of self.size """
        print("" * self.__position[1])
        print("\n".join([(" " * self.__position[0]) + ("#" * self
              .__size) for i in range(self.__size)]))

    def area(self):
        """ Multiple size by size to find area of a Square """
        return self.__size * self.__size
