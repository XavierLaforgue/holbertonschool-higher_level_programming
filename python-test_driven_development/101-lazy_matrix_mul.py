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
    msg_list_of_lists_type = msg_list_type + " of lists"
    msg_empty = "{:s} can't be empty"
    msg_int_float = "{:s} should contain only integers or floats"
    msg_rect = "each row of {:s} must be of the same size"
    matrices = [(m_a, "m_a"), (m_b, "m_b")]
    for mat, m_str in matrices:
        if not isinstance(mat, list):
            raise TypeError(msg_list_type.format(m_str))

    return np.matmul(np.array(m_a), np.array(m_b))
