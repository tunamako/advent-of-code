from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np
from heapdict import heapdict


Point = namedtuple("Point", ['x', 'y']) 

YEAR = 2021
DAY = 15

directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}


def easiest_path(risk_map):
    map_dim = len(risk_map)

    costs = heapdict()
    for x, y in np.ndindex(risk_map.shape):
        costs[Point(x, y)] = float('inf')

    risk_map = {Point(x, y): risk_map[x][y] for x in range(map_dim) for y in range(map_dim)}
    previous = {point: None for point in risk_map}

    queue = set(costs.keys())
    costs[Point(0, 0)] = 0
    sink = Point(map_dim - 1, map_dim - 1)

    while queue:
        pos, value = costs.popitem()
        queue.remove(pos)

        if pos == sink:
            return value

        neighbors = [Point(pos.x + d[0], pos.y + d[1]) for d in directions]
        for n in neighbors:
            if n not in queue:
                continue

            delta = value + risk_map[n]
            if delta < costs[n]:
                costs[n] = delta
                previous[n] = pos


def part_one(_input):
    risk_map = np.array([list(map(int, line)) for line in _input])
    risk_map = np.swapaxes(risk_map, 0, 1)

    return easiest_path(risk_map)


def part_two(_input):
    base_map = np.array([list(map(int, line)) for line in _input])
    base_map = np.swapaxes(base_map, 0, 1)
    base_dim = len(base_map)

    risk_map = np.zeros((base_dim * 5, base_dim * 5), dtype=int)

    for x in range(base_dim * 5):
        for y in range(base_dim * 5):
            modifier = (x // base_dim) + (y // base_dim)
            risk_map[x][y] = int(base_map[x % base_dim][y % base_dim] + modifier)
            if risk_map[x][y] > 9:
                risk_map[x][y] -= 9

    return easiest_path(risk_map)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
