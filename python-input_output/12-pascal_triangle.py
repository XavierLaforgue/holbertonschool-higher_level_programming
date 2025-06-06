#!/usr/bin/python3
"""
Module Name: 12-pascal_triangle.

Contain a function that returns a list of lists representing a Pascal's
triangle.
"""


def pascal_triangle(n):
    """Return list of lists representing Pascal's triangle depth n."""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(6))
