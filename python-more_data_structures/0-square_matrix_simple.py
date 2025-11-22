#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        result = []
        for j in i:
            result.append(j * j)
        new_matrix.append(result)
    return new_matrix
