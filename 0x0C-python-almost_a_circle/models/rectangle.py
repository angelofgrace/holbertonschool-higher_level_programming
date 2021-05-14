#!/usr/bin/python3
""" All rectangles are shapes """

from models.base import Base


class Rectangle(Base):
    """ Rectangle is a parrallelagram with four right angles """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Establish id, validate and assign private attribute inputs """
        super().__init__(id)
        self.validate("width", width)
        self.__width = width
        self.validate("height", height)
        self.__height = height
        self.validate("x", x)
        self.__x = x
        self.validate("y", y)
        self.__y = y

    def __str__(self):
        string = "[Rectangle] ({}) {}/{} - {}/{}"\
                  .format(self.id, self.x, self.y, self.width, self.height)
        return string

    def validate(self, attr, value):
        """ Raise attribute value errors if wrong type or beyond range """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if attr is "x" or attr is "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif attr is "width" or attr is "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(attr))

    def area(self):
        """ Calculate the area of a rectangle """
        return (self.width * self.height)

    def display(self):
        """ Print the rectangle as an array of hash marks """
        for i in range(0, self.height):
            for j in range(0, self.width):
                print("#", end="")
            print("")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value
