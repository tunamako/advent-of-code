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
import sympy as sp

YEAR = 2024
DAY = 13

Point = namedtuple("Point", ['x', 'y']) 
Machine = namedtuple("Machine", ['A', 'B', 'prize']) 

def parse_machines(_input, prize_offset=0):
    _input = _input.split("\n\n")
    ret = []
    for section in _input:
        amts = re.findall(r'\+(\d+)', section)
        prize = re.findall(r'=(\d+)', section)
        machine = Machine(
            Point(int(amts[0]), int(amts[1])),
            Point(int(amts[2]), int(amts[3])),
            Point(int(prize[0])+prize_offset, int(prize[1])+prize_offset),
        )

        ret.append(machine)
    
    return ret

def solve_machines(machines):
    a, b = sp.symbols('a, b')

    ret = 0
    for m in machines:
        eq1 = sp.Eq(m.A.x*a + m.B.x*b, m.prize.x)
        eq2 = sp.Eq(m.A.y*a + m.B.y*b, m.prize.y)

        solutions = sp.solve((eq1, eq2), (a, b), dict=True)
        cost = sys.maxsize
        for sol in solutions:
            if type(sol[a]) == type(sol[b]) == sp.core.numbers.Integer:
                cost = min(cost, 3 * int(sol[a]) + int(sol[b]))
        
        if cost < sys.maxsize:
            ret += cost
    
    return ret

def part_one(_input):
    machines = parse_machines(_input)

    return solve_machines(machines)

def part_two(_input):
    machines = parse_machines(_input, prize_offset=10000000000000)

    return solve_machines(machines)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data
    #_input = open('aoc-2024/day13/input.txt').read()

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
