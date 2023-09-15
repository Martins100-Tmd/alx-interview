#!/usr/bin/env python3
'''
Task 0's module
'''


def rotate_2d_matrix(matrix):
    matrix[:] = map(list, zip(*reversed(matrix)))
