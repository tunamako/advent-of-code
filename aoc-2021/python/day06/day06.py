from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *

YEAR = 2021
DAY = 6

def simulate(_input, days):
    fishes = Counter(map(int, _input.split(',')))

    for i in range(days):
        new_fish = fishes[0]
        fishes[0] = 0

        for age in range(1, 9):
            fishes[age - 1] += fishes[age]
            fishes[age] = 0

        fishes[8] = new_fish
        fishes[6] += new_fish

    return sum(fishes.values())


def part_one(_input):
    return simulate(_input, 18)

def part_two(_input):
    return simulate(_input, 256)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')[0]
    _input = open('input').readlines()[0]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
