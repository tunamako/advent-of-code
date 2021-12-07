from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import statistics as stat

YEAR = 2021
DAY = 7


def part_one(_input, use_p2=False):
    crabs = list(map(int, _input[0].split(',')))

    min_fuel = 99999999999
    for i in range(min(crabs), max(crabs)):
        fuel = 0
        for crab in crabs:
            gap = abs(crab - i)
            fuel += int(((gap*gap)+gap)/2) if use_p2 else gap

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = open('input').readlines()

    print(part_one(_input))
    print(part_one(_input, True))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
