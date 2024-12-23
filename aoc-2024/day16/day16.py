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

YEAR = 2024
DAY = 16

Point = namedtuple("Point", ['x', 'y'])
moves_ordered = "^<v>"
moves = {
    'v': (0, 1),
    '>': (1, 0),
    '^': (0, -1),
    '<': (-1, 0),
}
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
def print_state(grid):
    for line in np.swapaxes(grid, 0, 1):
        print(''.join(line))
    print()

def get_neighbors(pos, grid):
    """
    facing_idx = moves_ordered.index(facing)
    l_facing = moves_ordered[facing_idx - 3]
    r_facing = moves_ordered[facing_idx - 1]
    b_facing = moves_ordered[facing_idx - 2]

    fwd =   Point(pos.x + moves[facing][0], pos.y + moves[facing][1])
    left =  Point(pos.x + moves[l_facing][0], pos.y + moves[l_facing][1])
    right = Point(pos.x + moves[r_facing][0], pos.y + moves[r_facing][1])
    back =  Point(pos.x + moves[b_facing][0], pos.y + moves[b_facing][1])

    return [
            (fwd, facing),
            (left, l_facing),
            (right, r_facing),
            (back, b_facing),
    ]
    """

    return [Point(pos.x + d[0], pos.y + d[1]) for d in directions]


def score_paths(grid, path):
    tmp = grid.copy()

    for pos in path:
        tmp[pos] = 'X'
    
    #print_state(tmp)

def part_one(grid):
    print_state(grid)
    score = 0
    start = np.where(grid == 'S')
    start = Point(int(start[0][0]), int(start[1][0]))
    facing = '>'
    visited = set()
    
    path = (start,)
    stack = [path]
    complete_paths = []

    while stack:
        path = stack.pop()
        pos = path[-1]

        if grid[pos] == 'E':
            print("wah")
            complete_paths.append(path)
            continue

        for n in get_neighbors(pos, grid):
            if n not in path and grid[n] in ".E":
                stack.append(path + (n,))

    for path in complete_paths:
        score_paths(grid, path)

    print(len(complete_paths))

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day16/input.txt').readlines()]
    grid = np.array([list(line) for line in _input], dtype="<U100")
    grid = np.swapaxes(grid, 0, 1)

    print(part_one(grid))
    print(part_two(grid))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
