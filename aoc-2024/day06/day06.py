from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, cycle
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
from multiprocess import Process, Pool, Value
import time

np.set_printoptions(threshold=sys.maxsize)

YEAR = 2024
DAY = 6

Point = namedtuple("Point", ['x', 'y']) 

moves = {
    '>': Point(1, 0),
    'v': Point(0, 1),
    '<': Point(-1, 0),
    '^': Point(0, -1),
}

def run_guardbot(grid, start_pos, obstacle=None, return_keys=False):
    facing = '^'
    facings = cycle(">v<^")
    visited = defaultdict(set)
    visited[start_pos].add(facing)

    guard_pos = start_pos

    while 0 <= guard_pos.x <= len(grid) and 0 <= guard_pos.y <= len(grid[0]):
        if facing in visited[guard_pos] and len(visited.keys()) > 1:
            return -1

        visited[guard_pos].add(facing)
        next_pos = Point(guard_pos.x + moves[facing].x, guard_pos.y + moves[facing].y)

        try:
            if grid[next_pos.x][next_pos.y] == '#':
                facing = next(facings)
            elif obstacle and next_pos == obstacle:
                facing = next(facings)
            else:
                guard_pos = next_pos
        except IndexError:
            break
    
    return set(visited.keys()) if return_keys else len(visited.keys())

def part_one(_input):
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)
    start_pos = np.where(np.isin(grid, ['^','>','v','<']) == True)
    start_pos = Point(int(start_pos[0][0]), int(start_pos[1][0]))

    return run_guardbot(grid, start_pos)

def part_two(_input):
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)
    start_pos = np.where(np.isin(grid, ['^','>','v','<']) == True)
    start_pos = Point(int(start_pos[0][0]), int(start_pos[1][0]))

    base_path = run_guardbot(grid, start_pos, return_keys=True)
    base_path.remove(start_pos)

    args = [[grid, start_pos, obstacle] for obstacle in base_path]
    pool_size = 15
    with Pool(pool_size) as p:
        results = p.starmap(run_guardbot, args, 100)

    return results.count(-1)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day06/input.txt').readlines()]

    start = time.perf_counter()
    print(part_one(_input), time.perf_counter() - start)
    start = time.perf_counter()

    print(part_two(_input), time.perf_counter() - start)

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
