#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print matrix
    """
    if (matrix):
        for i in matrix:
            m_len = len(i) - 1
            for j in i:
                if (j == i[m_len]):
                    print("{:d}".format(j), end='')
                else:
                    print("{:d}".format(j), end=" ")
            print()
