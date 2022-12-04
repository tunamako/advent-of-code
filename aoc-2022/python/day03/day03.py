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
DAY = 3


def priority(item):
    return ord(item) - (38 if item.isupper() else 96)

def parse_sacks(_input):
    sacks = []
    for sack in _input:
        midpoint = int(len(sack)/2)
        comp_1 = set(map(priority, sack[:midpoint]))
        comp_2 = set(map(priority, sack[midpoint:]))
        sacks.append((comp_1, comp_2, comp_1.union(comp_2)))

    return sacks

def part_one(_input):
    sacks = parse_sacks(_input)
    return sum(sack[0].intersection(sack[1]).pop() for sack in sacks)

def part_two(_input):
    sacks = parse_sacks(_input)

    total = 0
    for i in range(0, len(sacks), 3):
        total += sacks[i][2].intersection(sacks[i+1][2], sacks[i+2][2]).pop()

    return total

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
