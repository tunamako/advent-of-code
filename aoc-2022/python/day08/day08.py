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

np.set_printoptions(threshold=sys.maxsize)

YEAR = 2022
DAY = 8

Point = namedtuple("Point", ['x', 'y']) 

def get_spindles(grid, tree):
    return [
        grid[tree.x, :tree.y][::-1],
        grid[tree.x, tree.y + 1:],
        grid[:tree.x, tree.y][::-1],
        grid[tree.x + 1:, tree.y],
    ]

def is_visible(grid, tree):
    if tree.x in [0, len(grid) - 1] or tree.y in [0, len(grid) - 1]:
        return True

    height = grid[tree.x][tree.y]

    return any(all(t < height for t in spindle) for spindle in get_spindles(_input, tree))

def part_one(_input):
    return sum(is_visible(_input, Point(x, y)) for x, y in np.ndindex(_input.shape))

def scenic_score(grid, tree):
    height = grid[tree.x][tree.y]
    up, down, left, right = 0, 0, 0, 0

    ret = 1

    for spindle in get_spindles(grid, tree):
        score = 0
        for t in spindle:
            score += 1
            if t >= height: break
        if score: ret *= score

    return ret

def part_two(_input):
    return max(scenic_score(_input, Point(x, y)) for x, y in np.ndindex(_input.shape))


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = np.array([list(map(int, line)) for line in puzzle.input_data.split('\n')])
    #_input = np.array([list(map(int, line)) for line in [line[:-1] for line in open('input').readlines()]])

    _input = np.swapaxes(_input, 0, 1)

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
