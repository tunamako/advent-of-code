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
import heapq
import heapdict

YEAR = 2022
DAY = 12

Point = namedtuple("Point", ['x', 'y']) 

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def get_valid_neighbors(grid, p):
    ret = []
    for d in directions:
        n = Point(p.x + d[0], p.y + d[1])
        try:
            if grid[p.x, p.y] - grid[n.x, n.y] >= -1 \
                and len(grid) > n.x >= 0 \
                and len(grid[0]) > n.y >= 0:
                ret.append(n)
        except:
            pass

    return ret

def minimum_path(grid, src, sink):
    neighbor_grid = dict()
    distances = dict()

    for x, y in np.ndindex(grid.shape):
        p = Point(x, y)
        neighbor_grid[p] = get_valid_neighbors(grid, p)
        distances[p] = math.inf

    distances[src] = 0
    unvisited = heapdict.heapdict(distances)
    visited = set()

    while len(visited) < len(distances):
        u = unvisited.popitem()[0]

        for n in neighbor_grid[u]:
            dist = distances[u] + 1
            if n not in visited \
                and distances[n] > dist:

                distances[n] = dist
                unvisited[n] = dist

        visited.add(u)

    return distances[sink]

def part_one(grid):
    grid = np.array([list(map(lambda x: ord(x) - 97, line)) for line in grid])
    grid = np.swapaxes(grid, 0, 1)

    for x, y in np.ndindex(grid.shape):
        if grid[x, y] == ord('S') - 97:
            start = Point(x, y)
        elif grid[x, y] == ord('E') - 97:
            end = Point(x, y)

    grid[start.x, start.y] = 0
    grid[end.x, end.y] = ord('z') - 97

    return minimum_path(grid, start, end)

def part_two(grid):
    grid = np.array([list(map(lambda x: ord(x) - 97, line)) for line in grid])
    grid = np.swapaxes(grid, 0, 1)

    for x, y in np.ndindex(grid.shape):
        if grid[x, y] == ord('S') - 97:
            print("")
            start = Point(x, y)
        elif grid[x, y] == ord('E') - 97:
            end = Point(x, y)

    grid[start.x, start.y] = 0
    grid[end.x, end.y] = ord('z') - 97

    starting_points = [Point(x, y) for x, y in zip(*np.where(grid == 0))]
    min_len = math.inf
    print(len(starting_points))
    for i, p in enumerate(starting_points):
        print(i, p, min_len)
        path = minimum_path(grid, p, end)
        min_len = min(min_len, path)

    return min_len

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    #print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
