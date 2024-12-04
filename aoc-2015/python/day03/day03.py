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
DAY = 3

def visit_houses(moves):
    x, y = 0, 0
    houses = Counter()

    houses[(x, y)] += 1

    for move in moves:
        if move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        
        houses[(x, y)] += 1

    return houses

def part_one(_input):
    return len(visit_houses(_input[0]))

def part_two(_input):
    santa_moves = _input[0][::2]
    robot_moves = _input[0][1::2]

    return len(visit_houses(santa_moves) + visit_houses(robot_moves))


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
