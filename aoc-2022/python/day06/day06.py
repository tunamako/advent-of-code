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
DAY = 6


def part_one(_input):
    for i in range(len(_input)):
        if len(set(_input[i:i+4])) == 4:
            return i + 4

def part_two(_input):
    for i in range(len(_input)):
        if len(set(_input[i:i+14])) == 14:
            return i + 14


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')[0]
    #_input = [line[:-1] for line in open('input').readlines()]
    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
