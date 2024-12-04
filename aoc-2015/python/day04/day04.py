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
import hashlib

YEAR = 2015
DAY = 4


def part_one(_input):
    secret = _input[0]

    i = 0
    while True:
        full_key = secret + str(i)
        md5hash = hashlib.md5(full_key.encode()).hexdigest()

        if md5hash.startswith("000000"):
            return i
        else:
            i += 1

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
