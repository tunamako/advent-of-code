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
DAY = 14

dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

def parse_robots(_input):
    robots = []
    for line in _input:
        p, v = line.split(' ')
        p = list(map(int, p.split('=')[1].split(',')))
        v = list(map(int, v.split('=')[1].split(',')))

        robots.append([p, v])

    return robots

def move_robots(robots, w, h):
    for r in robots:
        p, v = r
        p[0] = (p[0] + v[0]) % w
        p[1] = (p[1] + v[1]) % h

    return robots

def safety_factor(robots, w, h):
    h_mid = w // 2
    v_mid = h // 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for r in robots:
        p, _ = r

        if p[0] < h_mid and p[1] < v_mid:
            q1 += 1
        elif p[0] > h_mid and p[1] < v_mid:
            q2 += 1
        elif p[0] < h_mid and p[1] > v_mid:
            q3 += 1
        elif p[0] > h_mid and p[1] > v_mid:
            q4 += 1

    print(h_mid, v_mid)
    print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4

def part_one(_input):
    width, height = 101, 103
    robots = parse_robots(_input)

    for i in range(100):
        robots = move_robots(robots, width, height)

    return safety_factor(robots, width, height)

def is_tree(robots):
    return False

def print_state(grid, robots):
    for r in robots:
        grid[*r[0]] = '*'
    tmp = np.swapaxes(grid, 0, 1)
    should_print = False
    buffer = ""
    for line in tmp:
        buffer += ''.join(map(str, line)) + '\n'

    if "*******************************" in buffer:
        print(buffer)
        print()
        return True
    for r in robots:
        grid[*r[0]] = '.'
    return False

def part_two(_input):
    #width, height = 11, 7
    width, height = 101, 103
    robots = parse_robots(_input)
    grid = np.full((width, height), '.')

    for i in range(10000):
        robots = move_robots(robots, width, height)
        if print_state(grid, robots):
            return i + 1

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day14/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
