#!/usr/bin/python3
"""
Module Name: 101-lazy_matrix_mul.py

Description:
    This module includes a function to multiple two matrices "lazily",
    i.e, using NumPy.

Functions:
    lazy_matrix_mul: multiplies two matrices and returns the result.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - multiplies two matrices using NumPy

    Args:
        m_a: first matrix to multiply
        m_b: second matrix to multiply

    Returns:
        Result of the multiplication

    Raises:
        Left to NumPy.
    """
    msg_list_type = "Scalar operands are not allowed, use '*' instead"
    msg_empty = "{:s} can't be empty"
    msg_int_float = "invalid data type for einsum"
    msg_rect = "setting an array element with a sequence."
    matrices = [(m_a, "m_a"), (m_b, "m_b")]
    for mat, m_str in matrices:
        if not isinstance(mat, list):
            raise TypeError(msg_list_type)
    for mat, m_str in matrices:
        if not mat or any(not isinstance(row, list) for row in mat):
            raise TypeError(msg_list_type)
    """ for mat, m_str in matrices:
        if not mat[0]:
            raise ValueError(msg_empty.format(m_str)) """
    for mat, m_str in matrices:
        if any(not isinstance(elem, (int, float)) for row in mat
               for elem in row):
            raise TypeError(msg_int_float)
    for mat, m_str in matrices:
        if any(map(lambda r: len(r) != len(mat[0]), [row for row in mat])):
            raise TypeError(msg_rect)
    if not m_a[0] or not m_b[0] or (len(m_a[0]) != len(m_b)):
        raise ValueError(f"shapes ({len(m_a)},{len(m_a[0])}) and "
                         f"({len(m_b)},{len(m_b[0])}) not aligned:"
                         f" {len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)")

    return np.matmul(np.array(m_a), np.array(m_b))
