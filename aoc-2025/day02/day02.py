from aocd.models import Puzzle

import os
import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy

YEAR = 2025
DAY = 2


def is_valid_p2(_id):
    s = str(_id)

    for i in range(len(s)):
        pattern = s[:i+1]
        if len(s) % len(pattern) != 0:
            continue
        pattern_count = int(len(s) / len(pattern))

        if pattern_count > 1 and pattern * pattern_count == s:
            return False

    return True

def part_one(_input):
    ret = 0
    for r in _input[0].split(','):
        r = tuple(map(int, r.split('-')))

        for i in range(r[0], r[1]+1):
            _id = str(i)
            if _id[:len(_id)//2] == _id[len(_id)//2:]:
                ret += i

    return ret

def part_two(_input):
    ret = 0
    for r in _input[0].split(','):
        r = tuple(map(int, r.split('-')))

        for i in range(r[0], r[1]+1):
            if not is_valid_p2(i):
                ret += i

    return ret

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #_input = [line[:-1] for line in open(os.path.join(dir_path, 'input')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
