#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square a matrix
    """
    if (matrix):
        new_mat = []
        for i in matrix:
            mat = list(map(lambda x: x ** 2, i))
            new_mat.append(mat)
        return new_mat
