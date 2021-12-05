from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *

Point = namedtuple("Point", ['x', 'y']) 

YEAR = 2021
DAY = 5


def count_overlap(_input, use_diags=False):
    lines = []
    seen = defaultdict(int)

    for line in _input:
        p1, p2 = [Point(*map(int, p.split(','))) for p in line.split(" -> ")]

        if p1.x == p2.x:
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                seen[Point(p1.x, y)] += 1
        elif p1.y == p2.y:
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                seen[Point(x, p1.y)] += 1
        elif use_diags:
            if p1.x < p2.x:
                start, end = p1, p2
            else:
                start, end = p2, p1

            y = start.y
            for x in range(start.x, end.x + 1):
                seen[Point(x, y)] += 1
                y += 1 if end.y > start.y else -1

    return sum([count > 1 for p, count in seen.items()])


def part_one(_input):
    return count_overlap(_input)


def part_two(_input):
    return count_overlap(_input, True)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = open('input').readlines()

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
