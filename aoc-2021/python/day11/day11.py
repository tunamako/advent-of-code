from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np
from pprint import *
import operator

YEAR = 2021
DAY = 11

adjacents = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
]

def print_array(energies):
    for line in np.swapaxes(energies, 0, 1):
        print(''.join(list(map(str, line))))
    print('')


def flash(energies, flashed, pos):
    flashed.add(pos)
    for adj in adjacents:
        adj = tuple(map(operator.add, adj, pos))

        if adj in flashed or not (0 <= adj[0] < len(energies) and 0 <= adj[1] < len(energies[0])):
            continue
        else:
            energies[adj[0]][adj[1]] += 1
            if energies[adj[0]][adj[1]] >= 10:
                flash(energies, flashed, adj)


def part_one(_input):
    energies = np.swapaxes(np.array([[int(c) for c in s] for s in _input]), 0, 1)
    flashcount = 0

    for step in range(100):
        flashed = set()
        for x in range(len(energies)):
            for y in range(len(energies[0])):
                energies[x][y] += 1
                if energies[x][y] >= 10 and (x, y) not in flashed:
                    flash(energies, flashed, (x, y))

        flashcount += len(flashed)
        for f in flashed:
            energies[f[0]][f[1]] = 0

    return flashcount


def part_two(_input):
    energies = np.swapaxes(np.array([[int(c) for c in s] for s in _input]), 0, 1)

    step = 0
    while step := step + 1:
        flashed = set()
        for x in range(len(energies)):
            for y in range(len(energies[0])):
                energies[x][y] += 1
                if energies[x][y] >= 10 and (x, y) not in flashed:
                    flash(energies, flashed, (x, y))

        for f in flashed:
            energies[f[0]][f[1]] = 0

        if len(flashed) == 100:
            return step


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
