from aocd.models import Puzzle
from advent_lib.grid_helpers import parse_text_to_ndarray, get_neighbors, Point, DIRECTIONS

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
import os
from functools import cache

YEAR = 2025
DAY = 7


def part_one(_input):
    grid = parse_text_to_ndarray(_input)
    start = Point(*next(zip(*np.where(grid == 'S'))))

    beam_locs = {start.x}
    splits = 0
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] == '^' and x in beam_locs:
                splits += 1
                beam_locs.remove(x)
                beam_locs.add(x + 1)
                beam_locs.add(x - 1)
    
    return splits

grid = None

@cache
def beam_path(pos):
    global grid
    next_pos = Point(pos.x, pos.y + 1)

    if next_pos.y == len(grid[0]):
        return 1
    
    if grid[next_pos] == '.':
        return beam_path(next_pos)
    
    if grid[next_pos] == '^':
        left = Point(next_pos.x - 1, next_pos.y)
        right = Point(next_pos.x + 1, next_pos.y)

        return beam_path(left) + beam_path(right)

def part_two(_input):
    global grid
    grid = parse_text_to_ndarray(_input)
    start = Point(*next(zip(*np.where(grid == 'S'))))

    return beam_path(Point(int(start.x), int(start.y)))

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #_input = [line[:-1] for line in open(os.path.join(dir_path, 'input')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
