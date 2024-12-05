from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy

np.set_printoptions(threshold=sys.maxsize)

YEAR = 2024
DAY = 4

Point = namedtuple("Point", ['x', 'y']) 

def has_xmas(grid, p):
    valid = ["XMAS"]
    count = 0
    try:
        right = ''.join([grid[p.x][p.y], grid[p.x+1][p.y], grid[p.x+2][p.y], grid[p.x+3][p.y]])
        if right in valid:
            count += 1
    except:
        pass
    try:
        if p.x >= 3:
            left = ''.join([grid[p.x][p.y], grid[p.x-1][p.y], grid[p.x-2][p.y], grid[p.x-3][p.y]])
            if left in valid:
                count += 1
    except:
        pass

    try:
        if p.y >= 3:
            up = ''.join([grid[p.x][p.y], grid[p.x][p.y-1], grid[p.x][p.y-2], grid[p.x][p.y-3]])
            if up in valid:
                count += 1
    except:
        pass
    try:
        down = ''.join([grid[p.x][p.y], grid[p.x][p.y+1], grid[p.x][p.y+2], grid[p.x][p.y+3]])
        if down in valid:
            count += 1
    except:
        pass

    try:    
        diag_right_down = ''.join([grid[p.x][p.y], grid[p.x+1][p.y+1], grid[p.x+2][p.y+2], grid[p.x+3][p.y+3]])
        if diag_right_down in valid:
            count += 1
    except:
        pass
    
    try:
        if p.y >= 3:
            diag_right_up = ''.join([grid[p.x][p.y], grid[p.x+1][p.y-1], grid[p.x+2][p.y-2], grid[p.x+3][p.y-3]])
            if diag_right_up in valid:
                count += 1
    except:
        pass

    try:
        if p.x >= 3:
            diag_left_down = ''.join([grid[p.x][p.y], grid[p.x-1][p.y+1], grid[p.x-2][p.y+2], grid[p.x-3][p.y+3]])
            if diag_left_down in valid:
                count += 1
    except:
        pass
    
    try:
        if p.x >= 3 and p.y >= 3:
            diag_left_up = ''.join([grid[p.x][p.y], grid[p.x-1][p.y-1], grid[p.x-2][p.y-2], grid[p.x-3][p.y-3]])
            if diag_left_up in valid:
                count += 1
    except:
        pass

    return count    

def part_one(_input):
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)

    ret = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'X':
                ret += has_xmas(grid, Point(x, y))
    
    return ret

def has_mas(grid, p):
    up_left, up_right, down_left, down_right = grid[p.x-1][p.y-1], grid[p.x+1][p.y-1], grid[p.x-1][p.y+1], grid[p.x+1][p.y+1]
    tmp = ''.join([up_left, up_right, down_left, down_right])

    valid = [
        "MSMS",
        "MMSS",
        "SMSM",
        "SSMM",
    ]
    if tmp in valid:
        return 1

    return 0

def part_two(_input):
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)

    ret = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if grid[x][y] == 'A':
                ret += has_mas(grid, Point(x, y))
    
    return ret


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('aoc-2024/day04/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
