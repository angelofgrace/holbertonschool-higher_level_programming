#!/usr/bin/python3
""" Method to divide and conquer """


def matrix_divided(matrix, div):
    """ Divide a matrix by an input divisor """
    c = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if len(i) is not c:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")

    new_matrix = [[]]
    new_matrix = [[round((x / div), 2) for x in y] for y in matrix]
    return new_matrix
