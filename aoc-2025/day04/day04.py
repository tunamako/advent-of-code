from advent_lib.grid_helpers import parse_text_to_ndarray, get_neighbors, Point, DIRECTIONS

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
import time

YEAR = 2025
DAY = 4

def remove_rolls(rolls):
    while to_remove := {r for r in rolls if len(rolls[r]) < 4}:
        for r in to_remove:
            for n in rolls[r]:
                rolls[n].remove(r)
            del rolls[r]

        yield len(to_remove)

def parse_rolls(_input):
    grid = parse_text_to_ndarray(_input)
    rolls = dict()
    for r in {Point(*p) for p in zip(*np.where(grid == '@'))}:
        rolls[r] = set(get_neighbors(grid, r, value='@'))

    return rolls

def part_one(_input):
    return next(remove_rolls(parse_rolls(_input)))

def part_two(_input):
    return sum(remove_rolls(parse_rolls(_input)))


if __name__ == '__main__':
    #puzzle = Puzzle(year=YEAR, day=DAY)
    #_input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    _input = [line[:-1] for line in open(os.path.join(dir_path, 'input')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
