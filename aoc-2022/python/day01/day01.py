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
DAY = 1


def part_one(_input):
    return max(map(sum, _input))

def part_two(_input):
    return sum(sorted(map(sum, _input))[-3:])


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = [[int(meal) for meal in elf.split('\n')] for elf in puzzle.input_data.split('\n\n')]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
