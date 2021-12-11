from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from statistics import median

YEAR = 2021
DAY = 10


brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {')': 1, ']': 2,  '}': 3,    '>': 4}


def is_corrupt(line):
    stack = []
    for c in line:
        if c in brackets.keys():
            stack.append(c)
        elif c != brackets[stack.pop()]:
            return scores1[c]
    return 0


def part_one(_input):
    return sum([is_corrupt(line) for line in _input])


def auto_complete(line):
    stack = []

    for c in line:
        if c in brackets.keys():
            stack.append(c)
        else:
            stack.pop()

    score = 0
    for c in [brackets[c] for c in stack[::-1]]:
        score *= 5
        score += scores2[c]

    return score


def part_two(_input):
    return median([auto_complete(line) for line in _input if not is_corrupt(line)])


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
