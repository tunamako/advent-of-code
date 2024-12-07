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
from multiprocessing import Process, Pool, Value
import time

np.set_printoptions(threshold=sys.maxsize)

YEAR = 2024
DAY = 6

Point = namedtuple("Point", ['x', 'y']) 
moves = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1),
}

def run_guardbot(grid, start_pos, obstacle=None, return_keys=False):
    x, y = start_pos[0], start_pos[1]
    facing = '^'
    facings = cycle(">v<^")
    visited = defaultdict(set)
    visited[(x, y)].add(facing)


    while 0 <= x and 0 <= y:
        if facing in visited[(x, y)] and len(visited.keys()) > 1:
            return -1

        visited[(x, y)].add(facing)
        next_x, next_y = x + moves[facing][0], y + moves[facing][1]

        try:
            if grid[next_x][next_y] == '#':
                facing = next(facings)
            elif obstacle and next_x == obstacle[0] and next_y == obstacle[1]:
                facing = next(facings)
            else:
                x, y = next_x, next_y
        except IndexError:
            break
    
    return set(visited.keys()) if return_keys else len(visited.keys())

def solve(_input):
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)
    start_pos = np.where(np.isin(grid, ['^','>','v','<']) == True)
    start_pos = (int(start_pos[0][0]), int(start_pos[1][0]))

    base_path = run_guardbot(grid, start_pos, return_keys=True)
    print("p1:", len(base_path) + 1)
    base_path.remove(start_pos)

    args = [[grid, start_pos, obstacle] for obstacle in base_path]
    pool_size = 16
    with Pool(pool_size) as p:
        results = p.starmap(run_guardbot, args, 100)

    print("p2:", results.count(-1))
    #print("p2:", sum(run_guardbot(grid, start_pos, obstacle) for obstacle in base_path))

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day06/input.txt').readlines()]

    start = time.perf_counter()
    solve(_input)    
    print(time.perf_counter() - start)

    #cProfile.run('print(solve(_input))')
