from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, tee
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy

YEAR = 2024
DAY = 2

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))

def is_safe(report):
    adj_pairs = pairwise(report)
    # check ascending or descending
    is_ascending = True
    is_descending = True

    for x, y in adj_pairs:
        if not (0 < abs(x - y) < 4):
            return False

        if x < y:
            is_descending = False
        else:
            is_ascending = False

    return True

def part_one(_input):
    reports = [list(map(int, report.split(' '))) for report in _input]
    return sum(is_safe(report) for report in reports)

def part_two(_input):
    reports = [list(map(int, report.split(' '))) for report in _input]
    ret = 0

    for report in reports:
        if is_safe(report):
            ret += 1
        else:
            for i in range(len(report)):
                tmp = report[::]
                del tmp[i]

                if is_safe(tmp):
                    ret += 1
                    break
    
    return ret




if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1].strip() for line in open('aoc-2024/day02/bigboy.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
