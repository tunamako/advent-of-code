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
DAY = 2

win_map = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}
lose_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}


def calc_points1(p1, p2):
    p1 = ord(p1)
    p2 = ord(p2) - 23

    if p1 == p2:
        win_value = 3
    elif p2 - p1 in [1, -2]:
        win_value = 6
    else:
        win_value = 0

    return win_value + (p2 - 64)

def calc_points2(p1, p2):
    # Draw
    if p2 == 'Y':
        return 3 + (ord(p1) - 64)
    # Lose
    if p2 == 'X':
        return ord(lose_map[p1]) - 64
    # Win
    if p2 == 'Z':
        return 6 + ord(win_map[p1]) - 64 


def part_one(_input):
    rounds = [rnd.split(' ') for rnd in _input]

    return sum([calc_points1(*rnd) for rnd in rounds])

def part_two(_input):
    rounds = [rnd.split(' ') for rnd in _input]

    return sum([calc_points2(*rnd) for rnd in rounds])


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
