#!/usr/bin/python3

"""This module divides all elements
in a matrix by a divisor number
"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix
    using a common divisor div
    verify that div is an integer or float
    verify that all elements in the matrix
    is either an integer or a float
    """

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix(list of lists)\
                of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mat_len = len(matrix)
    if mat_len == 0:
        raise TypeError("matrix must be a matrix(list of lists)\
                of integers/floats")
    result = []
    for i in range(mat_len):
        new_arr = []
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix(list of lists)\
                    of integers/floats")
        f_len = len(matrix[0])
        if f_len != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        if len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix(list of lists)\
                    of integers/floats")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix(list of lists)\
                        of integers/floats")
            divisor = round(matrix[i][j] / div, 2)
            new_arr.append(divisor)
        result.append(new_arr)
    return result
