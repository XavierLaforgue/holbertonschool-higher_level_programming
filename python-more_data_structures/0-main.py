#!/usr/bin/python3
sq_matrix_simple = __import__('0-square_matrix_simple').sq_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = sq_matrix_simple(matrix)
print(new_matrix)
print(matrix)
