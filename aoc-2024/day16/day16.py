from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, pairwise
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
import networkx as nx

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

def print_state(grid):
    for line in np.swapaxes(grid, 0, 1):
        print(''.join(line))
    print()

def get_edges(pos, facing, grid):
    facing_idx = moves_ordered.index(facing)
    l_facing = moves_ordered[facing_idx - 3]
    r_facing = moves_ordered[facing_idx - 1]
    b_facing = moves_ordered[facing_idx - 2]

    fwd =   Point(pos.x + moves[facing][0], pos.y + moves[facing][1])
    left =  Point(pos.x + moves[l_facing][0], pos.y + moves[l_facing][1])
    right = Point(pos.x + moves[r_facing][0], pos.y + moves[r_facing][1])
    back =  Point(pos.x + moves[b_facing][0], pos.y + moves[b_facing][1])

    return [
            ((pos, facing), (fwd, facing), 1 if grid[fwd] in ".E" else sys.maxsize),
            ((pos, facing), (left, l_facing), 1001 if grid[left] in ".E" else sys.maxsize),
            ((pos, facing), (right, r_facing), 1001 if grid[right] in ".E" else sys.maxsize),
            ((pos, facing), (back, b_facing), 2001 if grid[back] in ".E" else sys.maxsize),
    ]

def generate_graph(grid):
    graph = nx.Graph()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x, y] in '#E':
                continue
            pos = Point(x, y)
            for m in moves_ordered:
                graph.add_weighted_edges_from(get_edges(pos, m, grid))

    start = np.where(grid == 'S')
    start = Point(int(start[0][0]), int(start[1][0]))
    graph.add_edge("start", (start, '>'), weight=0)

    end = np.where(grid == 'E')
    end = Point(int(end[0][0]), int(end[1][0]))
    graph.add_edge((end, '^'), "end", weight=0)
    graph.add_edge((end, '>'), "end", weight=0)
    graph.add_edge((end, 'v'), "end", weight=0)
    graph.add_edge((end, '<'), "end", weight=0)

    return graph

def part_one(grid):
    graph = generate_graph(grid)
    path = nx.single_source_dijkstra(graph, "start", "end", weight="weight")
    return path[0]

def part_two(_input):
    graph = generate_graph(grid)
    paths = nx.all_shortest_paths(graph, "start", "end", weight="weight")

    seen = set()
    for path in paths:
        for node in path:
            if node not in ["start", "end"]:
                seen.add(node[0])
 
    return len(seen)


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
