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
DAY = 3


def part_one(_input):
    _input = ''.join(_input)
    mulops = re.findall(r"mul\((\d+),(\d+)\)", _input)

    return sum(int(op[0]) * int(op[1]) for op in mulops)

def part_two(_input):
    _input = ''.join(_input)
    ops = re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", _input)

    active = True
    ret = 0
    for op in ops:
        if active and op.group().startswith("mul"):
            ret += int(op.groups()[0]) * int(op.groups()[1])
        if op.group().startswith("do("):
            active = True
        elif op.group().startswith("don't"):
            active = False
    
    return ret

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day03/bigboy.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
