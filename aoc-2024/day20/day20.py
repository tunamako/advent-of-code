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
import networkx as nx

YEAR = 2024
DAY = 20

Point = namedtuple("Point", ['x', 'y'])

moves = {
    Point(0, 1),
    Point(1, 0),
    Point(0, -1),
    Point(-1, 0),
}

cheat_moves = {
    (0, 2),
    (2, 0),
    (0, -2),
    (-2, 0),
}

def print_state(grid):
    for line in np.swapaxes(grid, 0, 1):
        print(''.join(line))
    print()

def get_neighbors(grid, pos):
    neighbors = []
    for m in moves:
        n = Point(pos.x + m.x, pos.y + m.y)
        if grid[n] != '#':
            neighbors.append(n)
    return neighbors

def generate_graph(grid):
    graph = nx.Graph()

    for x, y in  zip(*np.where(grid == '.')):
        pos = Point(int(x), int(y))
        for n in get_neighbors(grid, pos):
            graph.add_edge(pos, n)

    return graph

def man_dist(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)

def gen_man_points(p, r, grid):
    if r == 0:
        return set()

    points = set()
    for offset in range(r):
        invOffset = r - offset
        points.add(Point(p.x + offset, p.y + invOffset))
        points.add(Point(p.x + invOffset, p.y - offset))
        points.add(Point(p.x - offset, p.y - invOffset))
        points.add(Point(p.x - invOffset, p.y + offset))

    return points.union(gen_man_points(p, r - 1, grid))

def find_cheats(path_info, grid, max_cheat=2):
    cheats = []
    for p, info in path_info.items():
        for q in gen_man_points(p, max_cheat, grid):
            if q not in path_info:
                continue
            elif not (1 <= q.x < len(grid)-1 and 1 <= q.y < len(grid[0])-1):
                continue
            elif path_info[q]["from_src"] <= info["from_src"]:
                continue

            time_saved = info["to_sink"] - (path_info[q]["to_sink"] + man_dist(p, q))
            if time_saved > 0:
                cheats.append((p, q, int(time_saved)))

    return cheats

def part_one(grid):
    start = np.where(grid == 'S')
    start = Point(int(start[0][0]), int(start[1][0]))
    end = np.where(grid == 'E')
    end = Point(int(end[0][0]), int(end[1][0]))

    path = nx.shortest_path(generate_graph(grid), start, end)
    path_info = dict()
    for i, pos in enumerate(path):
        path_info[pos] = {
            "from_src": i,
            "to_sink": len(path) - i
        }

    cheats = find_cheats(path_info, grid, max_cheat=20)
    count = 0
    for c in cheats:
        if c[2] >= 100:
            count += 1

    return count

def part_two(grid):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day20/input.txt').readlines()]
    grid = np.array([list(line) for line in _input], dtype="<U100")
    grid = np.swapaxes(grid, 0, 1)

    print(part_one(grid))
    #print(part_two(grid))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
