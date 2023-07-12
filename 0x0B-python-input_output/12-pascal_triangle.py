#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle as a list of lists of integers.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
