#!/usr/bin/env python3
"""
Pascal Triangle Module
"""


def pascal_triangle(n: int) -> list:
    """
    Function to generate Pascal's triangle

    Args:
        n(int): number of rows in Pascal's triangle

    Returns:
        A list of integers representing the Pascal's triangle
        of n
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
