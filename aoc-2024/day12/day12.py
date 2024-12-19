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
DAY = 12

dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

def parse_region(pos, grid):  
    to_check = {pos}
    region = set()
    plant = grid[pos.x][pos.y]
    perimeter_len = 0
    perimeter = set()

    while to_check:
        tmp = to_check.pop()
        region.add(tmp)

        start_size = perimeter_len

        for d in dirs:
            n = Point(tmp.x + d[0], tmp.y + d[1])
            if 0 <= n.x < len(grid) and 0 <= n.y < len(grid[0]):                
                if grid[n.x][n.y] == plant:
                    if n not in region:
                        to_check.add(n)
                else:
                    perimeter_len += 1 
            else:
                perimeter_len += 1 

        if perimeter_len > start_size:
            # this is an edge plant
            perimeter.add(tmp)

    return region, perimeter_len, perimeter

def part_one(grid):
    regions = []
    perimeters = []
    cost = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            pos = Point(x,y)
            if any(pos in region for region in regions):
                continue

            region, perimeter_len, perimeter = parse_region(pos, grid)
            regions.append(region)
            perimeters.append(perimeter)
            cost += len(region) * perimeter_len


    for p in perimeters:
        print(p)

    return cost

def part_two(grid):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('aoc-2024/day12/input.txt').readlines()]
    grid = np.array([list(line) for line in _input], dtype="<U100")
    grid = np.swapaxes(grid, 0, 1)

    print(part_one(grid))
    print(part_two(grid))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
