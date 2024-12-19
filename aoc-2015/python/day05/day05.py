from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, tee
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy

YEAR = 2015
DAY = 5

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))

def part_one(_input):
    def is_nice(string):
        nice = True

        vowels = "aeiou"
        nice &= len([c for c in string if c in vowels]) >= 3
    
        nice &= any(pair[0] == pair[1] for pair in pairwise(string))

        nice &= all(sub not in string for sub in ["ab", "cd", "pq", "xy"])

        return nice

    return sum(is_nice(string) for string in _input)

def part_two(_input):
    def is_nice(string):
        nice = True

        vowels = "aeiou"
        nice &= len([c for c in string if c in vowels]) >= 3
    
        nice &= any(pair[0] == pair[1] for pair in pairwise(string))

        nice &= all(sub not in string for sub in ["ab", "cd", "pq", "xy"])

        return nice

    return sum(is_nice(string) for string in _input)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
