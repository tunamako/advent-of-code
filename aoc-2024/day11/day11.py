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
DAY = 11

memo = dict()

def blink(stone, depth, max_depth):
    _id = (depth, stone)
    if depth == max_depth:
        return 1
    elif _id in memo:
        return memo[_id]

    if stone == '0':
        memo[_id] = blink('1', depth+1, max_depth)
    elif len(stone) % 2 == 0:
        midpoint = len(stone)//2
        memo[_id] = blink(stone[:midpoint], depth+1, max_depth)
        memo[_id] += blink(stone[midpoint:], depth+1, max_depth)
    else:
        memo[_id] = blink(str(int(stone) * 2024), depth+1, max_depth)

    return memo[_id]

def part_one(_input):
    memo.clear()
    return sum(blink(stone, 0, 25) for stone in _input)

def part_two(_input):
    memo.clear()
    return sum(blink(stone, 0, 75) for stone in _input)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('aoc-2024/day11/input.txt').readlines()]
    _input = _input[0].split(' ')


    #print(part_one(_input))
    #print(part_two(_input))

    cProfile.run('print(part_one(_input))')
    cProfile.run('print(part_two(_input))')
