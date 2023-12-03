from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *
import numpy as np
import sys
from copy import deepcopy

YEAR = 2023
DAY = 3

Point = namedtuple("Point", ['x', 'y']) 

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
]

def is_symbol(c):
    return not c.isnumeric() and c != '.'

def get_full_number(x, y, grid):
    ret = grid[x, y]
    i = x + 1
    while i < grid.shape[0]:
        if grid[i, y].isnumeric():
            ret+= grid[i, y]
            i += 1
        else:
            break

    i = x - 1
    while i >= 0:
        if grid[i, y].isnumeric():
            ret = grid[i, y] + ret
            i -= 1
        else:
            break

    return int(ret)
        
def find_part_numbers(x, y, grid):
    parts = set()
    for d in directions:
        adj = grid[x+d[0], y+d[1]]
        if adj.isnumeric():
            parts.add(get_full_number(x+d[0], y+d[1], grid))

    ratio = 0
    if len(parts) == 2 and grid[x, y] == '*':
        ratio = 1
        for part in parts:
            ratio *= part
    else:
        ratio = 0  

    return (sum(parts), ratio)

def part_one(grid):
    ret = 0
    for x, y in np.ndindex(grid.shape):
        if is_symbol(grid[x, y]):
            ret += find_part_numbers(x, y, grid)[0]

    return ret

def part_two(grid):
    ret = 0
    for x, y in np.ndindex(grid.shape):
        if is_symbol(grid[x, y]):
            ret += find_part_numbers(x, y, grid)[1]

    return ret


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    _input = np.array([list(line) for line in _input])
    _input = np.swapaxes(_input, 0, 1)

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
