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
np.set_printoptions(threshold=sys.maxsize)
Point = namedtuple("Point", ['x', 'y']) 

YEAR = 2024
DAY = 10

def get_valid_neighbors(p, grid):
    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    ret = []
    for d in directions:
        n = Point(p.x + d[0], p.y + d[1])
        if 0 <= n.x < len(grid) and 0 <= n.y < len(grid[0]):
            if int(grid[n.x][n.y]) - int(grid[p.x][p.y]) == 1:
                ret.append(n)

    return ret

def hike_score(pos, grid):
    if grid[pos.x][pos.y] == 9:
        return {pos}

    ret = set()
    for n in get_valid_neighbors(pos, grid):
        ret = ret.union(hike_score(n, grid))

    return ret

def part_one(grid):
    trailheads = {Point(int(x), int(y)) for x, y in zip(*np.where(grid == 0))}

    return sum(len(hike_score(head, grid)) for head in trailheads) 

def hike_rating(pos, grid, path):
    if grid[pos.x][pos.y] == 9:
        return [path]

    ret = []
    for n in get_valid_neighbors(pos, grid):
        ret += hike_rating(n, grid, path + [pos])

    return ret

def part_two(grid):
    trailheads = {Point(int(x), int(y)) for x, y in zip(*np.where(grid == 0))}

    return sum(len(hike_rating(head, grid, [head])) for head in trailheads)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day10/input.txt').readlines()]
    grid = np.array([list(line) for line in _input], dtype="<U100")
    grid = np.swapaxes(grid, 0, 1)
    grid[grid == '.'] = -1
    grid = grid.astype(int)

    print(part_one(grid))
    print(part_two(grid))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
