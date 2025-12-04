from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
from functools import cache
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
import os

YEAR = 2025
DAY = 3

@cache
def max_joltage(bank, digits):
    if digits == 0:
        return ''

    ret = 0
    for i in range(len(bank) - digits + 1):
        tmp = bank[i] + max_joltage(bank[i+1:], digits - 1)
        ret = max(ret, int(tmp))

    return str(ret)

def part_one(_input):
    return sum(int(max_joltage(bank, 2)) for bank in _input)

def part_two(_input):
    return sum(int(max_joltage(bank, 12)) for bank in _input)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #_input = [line[:-1] for line in open(os.path.join(dir_path, 'input')).readlines()]

    #print(part_one(_input))
    #print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    cProfile.run('print(part_two(_input))')
