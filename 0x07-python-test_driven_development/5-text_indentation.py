#!/usr/bin/python3
""" Indent some text, bb """


def text_indentation(text):
    """ This is where the magic happens """

    if type(text) is not str:
        raise TypeError("text must be a string")

    xstr = text.split(".")
    newtxt = ".\n\n".join(xstr)

    ystr = newtxt.split("?")
    newtxt = "?\n\n".join(ystr)

    zstr = newtxt.split(":")
    newtxt = ":\n\n".join(zstr)

    finalstr = ""
    x = 0
    while x < len(newtxt):
        if newtxt[x] is '\n' and x < len(newtxt) - 1:
             while newtxt[x + 1] is " ":
                 x += 1 
        finalstr += newtxt[x]
        x += 1

    finalstr = finalstr.split("\n ")
    finalstr = "\n\n".join(finalstr)

    print(finalstr, end="")
