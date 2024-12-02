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
DAY = 1


def part_one(_input):
    list_1 = sorted([int(entry.split('   ')[0]) for entry in _input])
    list_2 = sorted([int(entry.split('   ')[1]) for entry in _input])

    return sum([abs(list_1[i] - list_2[i]) for i in range(len(list_1))])
    
def part_two(_input):
    list_1 = sorted([int(entry.split('   ')[0]) for entry in _input])
    list_2 = sorted([int(entry.split('   ')[1]) for entry in _input])

    count = Counter(list_2)

    return sum([item * count[item] for item in list_1])

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
