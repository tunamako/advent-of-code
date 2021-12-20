from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *

DIMENSIONS = 2

if DIMENSIONS == 2:
    Point = namedtuple("Point", ['x', 'y']) 
else:
    Point = namedtuple("Point", ['x', 'y', 'z']) 

YEAR = 2021
DAY = 19

pprint(len(list(combinations([i for i in range(35)], 2))))

rotations = [
    lambda p: Point(p.x, p.y),
    lambda p: Point(-p.x, p.y),
]


def rotate_point(point):
    pass


def get_rotations(beacons):
    # return all 24 orientations
    # run this once per scanner?
    ret = []
    for i in range(len(rotations)):
        for b in beacons:

        print(rotations[1](beacons.pop()))
        ret.append(rotations[i](p) for p in beacons)

    return ret

def check_adjacent(scannerA, scannerB):
    # for each orientation of scanner B:
        # assume beacon A:0 == beacon B:0
        # shift point of reference of scannerB to match scannerA
        # check if there's 12+ overlaps
            # if yes: we found the match
            # if no: move on to A:0 == B:1
    pass


def part_one(_input):
    scanners = []
    for i in range(0, len(_input), _input.index('') + 1):
        idx = int(_input[i].split(' ')[-2])
        beacons = set([Point(*map(int, b.split(','))) for b in _input[i+1:i+4]])
        scanners.append(get_rotations(beacons))
    
    pprint(scanners)

    #use adjacency matrix
    print(_input)
    # scanner 0 is "master" origin and orientation
    # find all scanners adjacent to 0
    # branch out, find scanners adjacent to those ones, etc 

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    #print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
