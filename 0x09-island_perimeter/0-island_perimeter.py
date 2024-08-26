#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): A 2D grid where 1 represents land
    and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check each side of the land cell
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # Top
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # Bottom
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # Left
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # Right

    return perimeter
