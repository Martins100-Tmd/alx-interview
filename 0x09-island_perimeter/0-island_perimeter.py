#!/usr/bin/python3
'''
Task 0's module
'''


def island_perimeter(grid):
    # base case
    if not grid:
        return 0
 
    M, N = len(grid), len(grid[0])
    count = 0
 
    # traverse each cell of the matrix
    for i in range(0, M):
        for j in range(0, N):
            # if the current cell is a land
            if grid[i][j] == 1:
                # check if top edge is adjacent to the water
                if i == 0 or grid[i - 1][j] == 0:
                    count = count + 1
                # check if bottom edge is adjacent to the water
                if i == M - 1 or grid[i + 1][j] == 0:
                    count = count + 1
                # check if left edge is adjacent to the water
                if j == 0 or grid[i][j - 1] == 0:
                    count = count + 1
                # check if right edge is adjacent to the water
                if j == N - 1 or grid[i][j + 1] == 0:
                    count = count + 1
    return count
