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
    return np.matmul(m_a, m_b)
