#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[0])):
            new_matrix[i].append([])
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
