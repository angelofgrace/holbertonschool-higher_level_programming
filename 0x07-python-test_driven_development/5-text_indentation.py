#!/usr/bin/python3
""" Indent some text, bb """


def text_indentation(text):
    """ This is where the magic happens """

    if type(text) is not str:
        raise TypeError("text must be a string")

    xstr = text.split(".")
    newtxt = "\n\n".join(xstr)

    ystr = newtxt.split("?")
    newtxt = "\n\n".join(ystr)

    zstr = newtxt.split(":")
    newtxt = "\n\n".join(zstr)

    linestr = newtxt.split("\n ")
    newtxt = "\n".join(linestr)

    print(newtxt, end="")
