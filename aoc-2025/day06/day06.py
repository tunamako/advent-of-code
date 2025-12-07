from aocd.models import Puzzle
from advent_lib.grid_helpers import parse_text_to_ndarray, get_neighbors, Point, DIRECTIONS

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
import ast

YEAR = 2025
DAY = 6

def part_one(_input):
    numbers = [re.findall(r'\d+', line) for line in _input[:-1]]
    numbers = np.array(numbers)
    numbers = np.swapaxes(numbers, 0, 1)

    operators = re.findall(r'[\*\+]', _input[-1])

    return sum(eval(op.join(numbers[i])) for i, op in enumerate(operators))

def part_two(_input):
    numbers = parse_text_to_ndarray(_input[:-1])
    operators = _input[-1]

    operands = []
    acc = 0
    for i in range(len(numbers) - 1, -1, -1):
        digits = ''.join(numbers[i])
        if all(d == ' ' for d in digits):
            continue
        operands.append(digits)

        if operators[i] != ' ':
            acc += eval(operators[i].join(operands))
            operands = []

    return acc

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #_input = [line[:-1] for line in open(os.path.join(dir_path, 'bigboy.txt')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
