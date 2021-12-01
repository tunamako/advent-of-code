from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 1


def part_one(_input):
    return sum(b > a for a, b in zip(_input, _input[1:]))

def part_two(_input):
    _sums = [sum(_input[i:i+3]) for i in range(len(_input) - 2)]
    return part_one(_sums)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = list(map(int, puzzle.input_data.split('\n')))
    #_input = open('bigboy').readlines()

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
