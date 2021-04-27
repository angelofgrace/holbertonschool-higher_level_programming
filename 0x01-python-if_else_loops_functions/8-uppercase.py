#!/usr/bin/python3

def uppercase(str):
    for e in range(0, len(str)):
        if ord(str[e]) >= 97 and ord(str[e]) <= 122:
            C = ord(str[e]) - 32
        else:
            C = ord(str[e])
        if e == (len(str) - 1):
            print("{:c}".format(C))
        else:
            print("{:c}".format(C), end="")
