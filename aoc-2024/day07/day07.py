from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, product
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
from multiprocessing import Process, Pool, Value

YEAR = 2024
DAY = 7

Equation = namedtuple("Equation", ['value', 'operands']) 

def evaluate(eq):
    if len(eq) == 3:
        lhs = eq[0]
    else:
        lhs = evaluate(eq[:-2])

    if eq[-2] == '|':
        return int(f"{lhs}{eq[-1]}")
    elif eq[-2] == '*':
        return lhs * eq[-1]
    elif eq[-2] == '+':
        return lhs + eq[-1]

def is_valid(eq, _ops):
    op_orderings = product(_ops, repeat=len(eq.operands)-1)

    for ops in op_orderings:
        ops = list(ops) + ['']
        full_eq = list(chain.from_iterable(zip(eq.operands, ops)))[:-1]

        if evaluate(full_eq) == eq.value:
            return eq.value
    
    return 0

def solve(_input):
    equations = []
    for line in _input:
        value, operands = line.split(": ")
        equations.append(Equation(int(value), tuple(map(int, operands.split(' ')))))

    p1 = sum(is_valid(eq, '*+') for eq in equations)
    print(f"p1: {p1}")
    p2 = sum(is_valid(eq, '*+|') for eq in equations)
    print(f"p2: {p2}")

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day07/input.txt').readlines()]

    solve(_input)

    #cProfile.run('print(solve(_input))')
