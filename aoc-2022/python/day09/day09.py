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

YEAR = 2022
DAY = 9

Point = namedtuple("Point", ['x', 'y']) 

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

def are_close(head, tail):
    return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1

def close_gap(head, tail):
    delta = [0, 0]
    if tail.x != head.x:
        delta[0] = 1 if head.x > tail.x else -1
    if tail.y != head.y:
        delta[1] = 1 if head.y > tail.y else -1

    return Point(tail.x + delta[0], tail.y + delta[1])

def solve(_input):
    moves = [move.split() for move in _input]
    rope = [Point(0, 0) for i in range(10)]
    visited_p1, visited_p2 = set([Point(0, 0)]), set([Point(0, 0)])

    for move in moves:
        delta, dist = directions[move[0]], int(move[1])

        for i in range(dist):
            rope[0] = Point(rope[0].x + delta[0], rope[0].y + delta[1])

            for j in range(1, 10):
                if not are_close(rope[j], rope[j - 1]):
                    rope[j] = close_gap(rope[j - 1], rope[j])

            visited_p1.add(rope[1])
            visited_p2.add(rope[-1])

    return len(visited_p1), len(visited_p2)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(solve(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
