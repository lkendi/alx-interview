#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island
    described in grid

    Approach:
        For each land cell, check its 4 neighbours. If the
        neigbour is water or the cell is at the boundary of the grid,
        it contributes to the perimeter (increase the perimeter)

    Args:
        grid (list): list of list of integers representing an island
            0 represents water, 1 represents land
    Returns:
        The perimeter of the island
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
