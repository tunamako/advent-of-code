from advent_lib.grid_helpers import get_neighbors, parse_text_to_ndarray, Point

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
import os

YEAR = 2025
DAY = 4


def remove_rolls(grid):
    while rolls := {Point(*p) for p in zip(*np.where(grid == '@'))}:
        to_remove = set()

        for r in rolls:
            if len(get_neighbors(grid, r, value='@')) < 4:
                to_remove.add(r)

        for p in to_remove:
            grid[p] = '.'

        yield len(to_remove)

def part_one(_input):
    grid = parse_text_to_ndarray(_input)
    return next(remove_rolls(grid))

def part_two(_input):
    grid = parse_text_to_ndarray(_input)
    return sum(remove_rolls(grid))


if __name__ == '__main__':
    #puzzle = Puzzle(year=YEAR, day=DAY)
    #_input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    _input = [line[:-1] for line in open(os.path.join(dir_path, 'input')).readlines()]

    print(part_one(_input))
    #print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
