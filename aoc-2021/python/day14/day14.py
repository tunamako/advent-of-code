from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np
from pprint import *
import sys
sys.setrecursionlimit(30000)

YEAR = 2021
DAY = 14


def solve(_input, step_count):
    template  = _input[0]
    pair_count = Counter([''.join(pair) for pair in zip(template, template[1:])])
    rules = [rule.split(' -> ') for rule in _input[2:]]

    for step in range(step_count):
        changes = Counter()
        for rule in rules:
            if pair_count[rule[0]] <= 0:
                continue

            count = pair_count[rule[0]]
            changes[rule[0]] += -1 * count
            changes[rule[0][0] + rule[1]] += count
            changes[rule[1] + rule[0][1]] += count

        for pair, change in changes.items():
            pair_count[pair] += change

    total_count = Counter()
    for pair, count in pair_count.items():
        total_count[pair[0]] += count

    return total_count.most_common()[0][1] - total_count.most_common()[-1][1] + 1


def part_one(_input):
    return solve(_input, 10)


def part_two(_input):
    return solve(_input, 40)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
