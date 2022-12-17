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
DAY = 16

def parse_valves(_input):
    valves = dict()

    pattern = re.compile(r"Valve (.*) has flow rate=(\d*);[\sa-z]*([,\sA-Z]*)\n")
    res = re.search(pattern, _input)
    for match in pattern.finditer(_input):
        name, flow, adjacents = match.groups()
        valves[name] = (int(flow), False, adjacents.split(', '))

    return valves

def part_one(_input):
    valves = parse_valves(_input)
    cur = 'AA'

    seen_paths = set()
    timer = 30
    while timer > 0:



    pprint(valves)

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data
    _input = open('input').read()

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
