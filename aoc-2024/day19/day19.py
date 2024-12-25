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
DAY = 19

memo = defaultdict(int)

def get_valid_designs(design, towels, cur_towels):
    if len(design) == 0:
        return 1

    if design in memo:
        return memo[design]

    for t in towels:
        if design.startswith(t):
            memo[design] += get_valid_designs(design[len(t):], towels, cur_towels + [t])

    return memo[design]

def part_one(_input):
    towels = set(_input[0].split(', '))
    designs = _input[2:]

    print(get_valid_designs("guuggwbugbrrwgwgrwuburuggwwguwbgrrbbguugrbgwugu", towels, []))

    ret = 0
    for d in designs:
        if get_valid_designs(d, towels, []):
            ret += 1
    return ret

def part_two(_input):
    towels = set(_input[0].split(', '))
    designs = _input[2:]

    return sum(get_valid_designs(d, towels, []) for d in designs)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day19/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
