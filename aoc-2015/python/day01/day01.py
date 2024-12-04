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
DAY = 2


def part_one(_input):
    ret = 0
    for box in _input:
        l, w, h = map(int, box.split('x'))

        sides = [l*w, w*h, h*l]
        ret += 2 * sum(sides) + min(sides)
    
    return ret


def part_two(_input):
    ret = 0
    for box in _input:
        dims = sorted(list(map(int, box.split('x'))))
        bow = math.prod(dims)
        ret += 2*dims[0] + 2*dims[1] + bow
    
    return ret

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
