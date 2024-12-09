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
import time
np.set_printoptions(threshold=sys.maxsize)
Point = namedtuple("Point", ['x', 'y']) 

YEAR = 2024
DAY = 8

def part_one(grid):
    antennae = defaultdict(list)
    antinodes = set()
    for x, y in  zip(*np.where(grid != '.')):
        antennae[str(grid[x][y])].append(Point(int(x), int(y)))


    for signal, points in antennae.items():
        for p, q in combinations(list(points), 2):
            one = Point(p.x + p.x - q.x, p.y + p.y - q.y)
            if 0 <= one.x < len(grid) and 0 <= one.y < len(grid[0]):
                antinodes.add(one)

            two = Point(q.x + q.x - p.x, q.y + q.y - p.y)
            if 0 <= two.x < len(grid) and 0 <= two.y < len(grid[0]):
                antinodes.add(two)

    return len(antinodes)

def part_two(grid):
    antennae = defaultdict(list)
    antinodes = set()
    for x, y in  zip(*np.where(grid != '.')):
        antennae[str(grid[x][y])].append(Point(int(x), int(y)))

    for signal, points in antennae.items():
        for p, q in combinations(list(points), 2):
            antinodes.add(p)
            antinodes.add(q) 

            i = 1
            while True:
                tmp = Point(p.x + i*(p.x - q.x), p.y + i*(p.y - q.y))
                if 0 <= tmp.x < len(grid) and 0 <= tmp.y < len(grid[0]):
                    antinodes.add(tmp)
                    i += 1
                else:
                    break

            i = 1
            while True:
                tmp = Point(q.x + i*(q.x - p.x), q.y + i*(q.y - p.y))
                if 0 <= tmp.x < len(grid) and 0 <= tmp.y < len(grid[0]):
                    antinodes.add(tmp)
                    i += 1
                else:
                    break

    return len(antinodes)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('aoc-2024/day08/bigboy.txt').readlines()]
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)

    start = time.perf_counter()
    print(part_one(grid))
    print(time.perf_counter() - start)
    start = time.perf_counter()
    print(part_two(grid))
    print(time.perf_counter() - start)

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
