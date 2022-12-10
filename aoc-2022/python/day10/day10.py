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
DAY = 10

def run_pgm(tape):
    screen = [['.' for i in range(40)] for j in range(6)]
    reg = {'X': 1}

    pc = 0
    occupied = 0
    cycle = 0

    strengths = []

    while pc < len(tape):
        cycle += 1
        row, col = (cycle - 1) // 40, (cycle - 1) % 40

        screen[row][col] = '#' if abs(col - reg['X']) <= 1 else '.'

        if cycle in [20, 60, 100, 140, 180, 220]:
            strengths.append(reg['X'] * cycle)

        if occupied:
            reg['X'] += occupied[1]
            occupied = None
            pc += 1
            continue

        if tape[pc][0] == "noop":
            pc += 1
            pass
        elif tape[pc][0] == "addx":
            occupied = (1, int(tape[pc][1]))

    screen = [''.join(row) for row in screen]
    pprint(screen)
    return sum(strengths)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = [line.split() for line in puzzle.input_data.split('\n')]
    #_input = [line[:-1].split() for line in open('input').readlines()]

    print(run_pgm(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
