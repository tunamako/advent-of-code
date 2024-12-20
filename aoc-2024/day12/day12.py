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
    cost = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            pos = Point(x,y)
            if any(pos in region for region in regions):
                continue

            region, perimeter_len, perimeter = parse_region(pos, grid)
            regions.append(region)
            cost += len(region) * perimeter_len

    return cost

def get_sidecount(grid, r):
    plant = grid[next(iter(r))]
    count = 0
    # Horizontal sides
    top_flag, bottom_flag = False, False
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            pos = Point(x, y)
            if pos not in r:
                top_flag = False
                bottom_flag = False
                continue

            up =   Point(pos.x, pos.y - 1)
            down = Point(pos.x, pos.y + 1)

            if (up.y < 0 or up not in r):
                if top_flag == False:
                    # Starting a new side on top
                    top_flag = True
                    count += 1
            else:
                top_flag = False


            if (down.y > len(grid[0]) or down not in r):
                if bottom_flag == False:
                    # Starting a new side on bottom
                    bottom_flag = True
                    count += 1
            else:
                bottom_flag = False

    # Vertical sides
    left_flag, right_flag = False, False
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            pos = Point(x, y)
            if pos not in r:
                left_flag = False
                right_flag = False
                continue

            left =  Point(pos.x - 1, pos.y)
            right = Point(pos.x + 1, pos.y)

            if (left.x < 0 or left not in r):
                if left_flag == False:
                    # Starting a new side on top
                    left_flag = True
                    count += 1
            else:
                left_flag = False


            if (right.x > len(grid) or right not in r):
                if right_flag == False:
                    # Starting a new side on bottom
                    right_flag = True
                    count += 1
            else:
                right_flag = False
    
    print(plant, count)
    return count


def part_two(grid):
    regions = []
    cost = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            pos = Point(x,y)
            if any(pos in region for region in regions):
                continue

            region, perimeter_len, perimeter = parse_region(pos, grid)
            regions.append(region)
            cost += len(region) * perimeter_len

    return sum(get_sidecount(grid, r) * len(r) for r in regions)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day12/input.txt').readlines()]
    grid = np.array([list(line) for line in _input], dtype="<U100")
    grid = np.swapaxes(grid, 0, 1)

    #print(part_one(grid))
    print(part_two(grid))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
