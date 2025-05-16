#!/usr/bin/python3
"""
Module Name: 2-matrix_divided.py

Description:
    This module includes a function to divide all elements of a matrix.

Functions:
    matrix_divided(matrix, div): Returns a new matrix whose elements
        will be the ones of the input matrix divided by div.
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divides all elements of a matrix by a number.

    Args:
        matrix: list of lists of integers or floats.
            Each row must be of the same size.
            Matrix to be divided by a number.
        div: number (integer or float), different from zero.

    Returns:
        The new matrix resulting by dividing each element of the
        original matrix by div and rounding to 2 decimal places.

    Raises:
        TypeError: if input matrix is not a list of lists of integers
            or floats.
        TypeError: if each row of the input matrix is not of the same
            size.
        TypeError: if div is not an integer or a float.
        ZeroDivisionError: if div is equal to 0.
    """
    if not (isinstance(matrix, list) and
            all([isinstance(row, list) for row in matrix]) and
            all([isinstance(elem, (int, float)) for row in matrix for
                elem in row])):
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')
    if not all([len(row) == len(matrix[0]) for row in matrix]):
        raise TypeError('Each row of the matrix must have the same'
                        ' size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for elem in matrix[i]:
            new_matrix[i].append(round(elem / div, 2))
    return new_matrix
