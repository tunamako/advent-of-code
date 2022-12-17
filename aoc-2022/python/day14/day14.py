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
DAY = 14

Point = namedtuple("Point", ['x', 'y']) 
np.set_printoptions(threshold=sys.maxsize)


def generate_grid(walls):
    points = set()
    for wall in walls:
        corners = [list(map(int, corner.split(','))) for corner in wall.split(' -> ')]
        for i in range(len(corners) - 1):
            a, b = corners[i], corners[i + 1]

            if a[0] == b[0]:
                for j in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                    points.add(Point(a[0], j))
            elif a[1] == b[1]:
                for j in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                    points.add(Point(j, a[1]))

    min_x = min(p[0] for p in points)
    min_y = 0
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    mid_x = (max_x + min_x) // 2

    new_max_x = max_y * 3
    delta = mid_x - (new_max_x // 2)

    tmp = set()
    points = set(Point(p[0] - delta, p[1]) for p in points)

    grid = np.zeros(shape=[max_y * 3, max_y + 3], dtype=np.uint8)

    for x, y in points:
        grid[x, y] = 1

    return delta, grid

def place_sand(spout, grid):
    s = [spout, 0]
    while True:
        if s[0] + 1 >= len(grid) or s[1] + 1 >= len(grid[0]):
            return None
        elif grid[s[0], s[1]]:
            return None

        if grid[s[0], s[1] + 1]:
            if not grid[s[0] - 1, s[1] + 1]:
                s[0] -= 1
                s[1] += 1
            elif not grid[s[0] + 1, s[1] + 1]:
                s[0] += 1
                s[1] += 1
            else:
                return Point(s[0], s[1])
        else:
            s[1] += 1

def part_one(_input):
    shift, grid = generate_grid(_input)
    spout = 500 - shift

    resting_sand = set()

    while True:
        if s := place_sand(spout, grid):
            resting_sand.add(s)
            grid[s[0], s[1]] = 2
        else:
            break

    return len(resting_sand)

def part_two(_input):
    shift, grid = generate_grid(_input)
    spout = 500 - shift

    for i in range(len(grid)):
        grid[i, -1] = 1

    resting_sand = set()

    while True:
        s = place_sand(spout, grid)
        if s is None:
            break
        resting_sand.add(s)
        grid[s[0], s[1]] = 2

    return len(resting_sand)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    #print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
