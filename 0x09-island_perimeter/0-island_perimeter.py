#!/usr/bin/python3
'''
Task 0's module
'''


def island_perimeter(grid):
    '''
    find island perimter of grid ocean
    '''

    gridLand = [land for area in grid for land in area if land > 0]
    boxRep = list(map(lambda x: x * 2, gridLand))
    return sum(boxRep, 0) + 2
