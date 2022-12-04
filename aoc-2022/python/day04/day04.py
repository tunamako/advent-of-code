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

YEAR = 2022
DAY = 4

def parse_pairs(_input):
    _input = [list(map(int, re.split(',|-', line))) for line in _input]

    return [(set(range(pair[0], pair[1] + 1)), set(range(pair[2], pair[3] + 1))) for pair in _input]

def part_one(_input):
    pairs = parse_pairs(_input)
    return sum((pair[0] <= pair[1] or pair[1] <= pair[0]) for pair in pairs)

def part_two(_input):
    pairs = parse_pairs(_input)
    return sum(bool(pair[0] & pair[1]) for pair in pairs)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]


    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
