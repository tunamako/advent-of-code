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

YEAR = 2015
DAY = 1


def part_one(_input):
    ret = 0
    for c in _input[0]:
        if c == '(':
            ret += 1
        elif c == ')':
            ret -= 1
    
    return ret


def part_two(_input):
    ret = 0
    for i, c in enumerate(_input[0]):
        if c == '(':
            ret += 1
        elif c == ')':
            ret -= 1

        if ret == -1:
            return i + 1

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
