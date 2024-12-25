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

YEAR = 2024
DAY = 25

def print_state(grid):
    for line in np.swapaxes(grid, 0, 1):
        print(''.join(line))
    print()

def partition(alist, indices):
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]

def parse_input(_input):
    splits = [i for i, x in enumerate(_input) if x == '']
    height = 0
    keys = []
    locks = []

    for part in partition(_input, splits):
        if part[0] == '':
            part = part[1:]
        item = np.array([list(line) for line in part])
        item = np.swapaxes(item, 0, 1)

        as_ints = []
        if all(x == '.' for x in item[:,0]):
            # key
            height = len(x) - 1
            for x in item:
                as_ints.append(len(x) - list(x).index('#') - 1)
            keys.append(as_ints)
        elif all(x == '#' for x in item[:,0]):
            # lock
            for x in item:
                as_ints.append(list(x).index('.') - 1)
            locks.append(as_ints)
        
    return locks, keys, height

def part_one(_input):
    locks, keys, height = parse_input(_input)
    print(height)
    ret = 0
    for l in locks:
        for k in keys:
            if all(l[i] + k[i] < height for i in range(len(l))):
                ret += 1
    return ret

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open("aoc-2024/day25/input.txt").readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
