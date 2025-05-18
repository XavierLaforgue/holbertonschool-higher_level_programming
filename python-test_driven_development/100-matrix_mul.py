#!/usr/bin/python3
"""
Module Name: 100-matrix_mul.py

Description:
    This module includes a function to multiple two matrices.

Functions:
    matrix_mul: multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul - multiplies two matrices

    Args:
        m_a: first matrix to multiply
        m_b: second matrix to multiply

    Returns:
        Result of the multiplication

    Raises:
        TypeError:
    """
    msg_list_type = "{:s} must be a list"
    msg_list_of_lists_type = msg_list_type + " of lists"
    msg_empty = "{:s} can't be empty"
    msg_int_float = "{:s} should contain only integers or floats"
    msg_rect = "each row of {:s} must be of the same size"
    matrices = [(m_a, "m_a"), (m_b, "m_b")]
    for mat, m_str in matrices:
        if not isinstance(mat, list):
            raise TypeError(msg_list_type.format(m_str))
    for mat, m_str in matrices:
        if not mat or any(not isinstance(row, list) for row in mat):
            raise TypeError(msg_list_of_lists_type.format(m_str))
    for mat, m_str in matrices:
        if not mat[0]:
            raise ValueError(msg_empty.format(m_str))
    for mat, m_str in matrices:
        if any(not isinstance(elem, (int, float)) for row in mat
               for elem in row):
            raise TypeError(msg_int_float.format(m_str))
    for mat, m_str in matrices:
        if any(map(lambda r: len(r) != len(mat[0]), [row for row in mat])):
            raise TypeError(msg_rect.format(m_str))
    """ if not isinstance(m_a, list):
        raise TypeError(msg_list_type.format("m_a"))
    if not isinstance(m_b, list):
        raise TypeError(msg_list_type.format("m_b")) """
    """ if not m_a or any(not isinstance(row, list) for row in m_a):
        raise TypeError(msg_list_of_lists_type.format("m_a"))
    if not m_b or any(not isinstance(row, list) for row in m_b):
        raise TypeError(msg_list_of_lists_type.format("m_b")) """
    """ if not m_a[0]:
        raise ValueError(msg_empty.format("m_a"))
    if not m_b[0]:
        raise ValueError(msg_empty.format("m_b")) """
    """ if any(not isinstance(elem, (int, float)) for row in m_a
                for elem in row):
        raise TypeError(msg_int_float.format("m_a"))
    if any(not isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError(msg_int_float.format("m_b")) """
    """ if any(map(lambda r: len(r) != len(m_a[0]), [row for row in m_a])):
        raise TypeError(msg_rect.format("m_a"))
    if any(map(lambda r: len(r) != len(m_b[0]), [row for row in m_b])):
        raise TypeError(msg_rect.format("m_b")) """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = []
    for i in range(len(m_a)):
        res.append([])
        for j in range(len(m_b[0])):
            res[i].append(0)
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res
