#!/usr/bin/python3
"""
Pascal's Triangle Module
This module contains a function, pascal_triangle(n), that generates
Pascal's triangle up to the nth row. For n <= 0, it returns an empty list.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle of height n.

    Args:
        n (int): The height of the triangle.

    Returns:
        list of lists: A list containing the rows of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)


return triangle
