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
DAY = 17

Point = namedtuple("Point", ['x', 'y']) 
moves = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1),
}

def print_state(grid):
    tmp = np.swapaxes(grid, 0, 1)
    for line in tmp:
        print(''.join(line))
    print()

def part_one(grid):
    print_state(grid)
    score = 0
    start = np.where(grid == 'S')
    start = Point(int(start[0][0]), int(start[1][0]))
    facing = '>'
    visited = set()

    stack = [start]
    while stack:
        pos = stack.pop()
        visited.add((pos, facing))


        for n in get_neighbors(pos, facing, grid):
            if (n, facing) not in visited:
                stack.append(n)

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('aoc-2024/day16/input.txt').readlines()]
    grid = np.array([list(line) for line in _input], dtype="<U100")
    grid = np.swapaxes(grid, 0, 1)

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
