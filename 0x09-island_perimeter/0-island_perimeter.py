#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
    - grid (List[List[int]]): The 2D grid of 0s and 1s.

    Returns:
    - int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with full perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove top edge if land on top
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove left edge if land on the left
    
    return perimeter
