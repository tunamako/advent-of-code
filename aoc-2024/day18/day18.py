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
DAY = 18
Point = namedtuple("Point", ['x', 'y'])
moves = {
    Point(0, 1),
    Point(1, 0),
    Point(0, -1),
    Point(-1, 0),
}
def print_state(grid):
    for line in np.swapaxes(grid, 0, 1):
        print(''.join(line))
    print()

def get_neighbors(grid, pos):
    neighbors = []
    for m in moves:
        n = Point(pos.x + m.x, pos.y + m.y)
        if 0 <= n.x < len(grid) and 0 <= n.y < len(grid[0]) and grid[n] != '#':
            neighbors.append(n)
    return neighbors

def generate_graph(grid):
    graph = nx.Graph()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x, y] == '#':
                continue
            pos = Point(x, y)
            for n in get_neighbors(grid, pos):
                graph.add_edge(pos, n)

    return graph

def part_one(_input):
    space = 70
    bites = [Point(*map(int, line.split(','))) for line in _input]
    grid = np.full((space + 1, space + 1), '.')

    for i in range(1024):
        grid[bites[i]] = '#'

    graph = generate_graph(grid)
    path = nx.shortest_path(graph, Point(0,0), Point(space, space))

    return len(path) - 1

def part_two(_input):
    space = 70
    bites = [Point(*map(int, line.split(','))) for line in _input]
    grid = np.full((space + 1, space + 1), '.')

    for bite in bites[:1024]:
        grid[bite] = '#'

    graph = generate_graph(grid)
    path = nx.shortest_path(graph, Point(0,0), Point(space, space))
    for bite in bites[1024:]:
        grid[bite] = '#'

        if bite in path:
            graph = generate_graph(grid)
            try:
                path = nx.shortest_path(graph, Point(0,0), Point(space, space))
            except nx.exception.NetworkXNoPath:
                return f"{bite.x},{bite.y}"


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day18/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
