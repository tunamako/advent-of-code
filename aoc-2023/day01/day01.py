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

YEAR = 2023
DAY = 1

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_one(_input):
    ret = 0
    for line in _input:
        first = next(c for c in line if c.isnumeric())
        last = next(c for c in reversed(line) if c.isnumeric())
        ret += int(first + last)

    return ret

def part_two(_input):
    ret = 0
    for line in _input:
        indices = dict()

        for text, n in numbers.items():
            for i, _ in enumerate(line):
                if line[i:i+len(text)] == text or line[i] == n:
                    indices[i] = n

        first, last = min(indices.keys()), max(indices.keys())
        ret += int(str(indices[first]) + str(indices[last]))

    return ret


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
