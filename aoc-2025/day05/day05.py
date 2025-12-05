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
DAY = 5


def part_one(_input):
    ranges = _input[:_input.index('')]
    ids = _input[_input.index('')+1:]

    ranges = [tuple(map(int, r.split('-'))) for r in ranges]
    ids = list(map(int, ids))

    ret = 0
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                ret += 1
                break
    return ret

def part_two(_input):
    ranges = _input[:_input.index('')]
    ranges = {tuple(map(int, r.split('-'))) for r in ranges}

    while True:
        to_merge = dict()
        for r1 in ranges:
            if r1 in to_merge:
                continue
            for r2 in ranges:
                if r2 in to_merge or r1 in to_merge or r1 == r2:
                    continue
                if max(r1[0], r2[0]) <= min(r1[1], r2[1]):
                    to_merge[r1] = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                    to_merge[r2] = to_merge[r1]

        if not to_merge:
            break

        for r, merged in to_merge.items():
            ranges.remove(r)
            ranges.add(merged)

    return sum(r[1] - r[0] + 1 for r in ranges)


if __name__ == '__main__':
    #puzzle = Puzzle(year=YEAR, day=DAY)
    #_input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    _input = [line[:-1] for line in open(os.path.join(dir_path, 'input')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
