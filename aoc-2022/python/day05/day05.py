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
DAY = 5

def parse_input(_input):
    crates_raw, moves_raw = _input.split('\n\n')
    crates_raw = crates_raw.split('\n')
    moves_raw = moves_raw.split('\n')

    moves = [list(map(int, re.findall(r'\b\d+\b', move))) for move in moves_raw]
    moves = [[move[0], move[1] - 1, move[2] - 1] for move in moves]

    stacks = [list() for i in range(int(len(crates_raw[0])/4) + 1)]

    for line in crates_raw[:-1]:
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[int((i - 1)/4)].insert(0, line[i])

    return stacks, moves

def part_one(_input):
    stacks, moves = parse_input(_input)

    for move in moves:
        amount, src, dst = move
        for i in range(amount):
            stacks[dst].append(stacks[src].pop())

    return ''.join([stack[-1] for stack in stacks])


def part_two(_input):
    stacks, moves = parse_input(_input)

    for move in moves:
        amount, src, dst = move

        stacks[dst] += stacks[src][-amount:]
        stacks[src] = stacks[src][:-amount]

    return ''.join([stack[-1] for stack in stacks])

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
