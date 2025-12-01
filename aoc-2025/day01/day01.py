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
DAY = 1


def part_one(_input):
    dial = deque(range(100))
    dial.rotate(50)

    ret = 0
    for step in _input:
        delta = int(step[1:])
        if step[0] == 'R':
            delta *= -1
        
        dial.rotate(delta)

        if dial[0] == 0:
            ret += 1

    return ret


def part_two(_input):
    dial = 50
    ret = 0
    for step in _input:
        dir = 1 if step[0] == 'R' else -1
        delta = int(step[1:])

        while delta:
            if dial == 0:
                ret += 1
            
            dial += dir
            if dial < 0:
                dial = 99
            elif dial > 99:
                dial = 0

            delta -= 1

    return ret

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #_input = [line[:-1] for line in open(os.path.join(dir_path, 'input.txt')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
