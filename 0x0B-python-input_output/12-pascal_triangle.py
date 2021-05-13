#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Return a list of lists of integers, Pascal's triangle for n """

    triangle = []

    if n <= 0:
        return triangle

    i = 0
    while i < n:
        tmp = []
        if i == 0:
            tmp.append(1)
        else:
            for x in range(0, i + 1):
                if x == 0 or x == i:
                    tmp.append(1)
                else:
                    tmp.append(triangle[i - 1][x] + triangle[i - 1][x - 1])
        triangle.append(tmp)
        i += 1
    return(triangle)
