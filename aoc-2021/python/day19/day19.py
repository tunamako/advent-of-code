from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *
import numpy as np

Point = namedtuple("Point", ['x', 'y', 'z']) 

YEAR = 2021
DAY = 19

orientations = [
    lambda p: Point( p.x,  p.y,  p.z),
    lambda p: Point( p.x, -p.y, -p.z),
    lambda p: Point( p.x, p.z,  -p.y),
    lambda p: Point( p.x, -p.z,  p.y),
    lambda p: Point( p.y,  p.x, -p.z),
    lambda p: Point( p.y, -p.x,  p.z),
    lambda p: Point( p.y,  p.z,  p.x),
    lambda p: Point( p.y, -p.z, -p.x),
    lambda p: Point( p.z,  p.x,  p.y),
    lambda p: Point( p.z, -p.x, -p.y),
    lambda p: Point( p.z,  p.y, -p.x),
    lambda p: Point( p.z, -p.y,  p.x),
    lambda p: Point(-p.x,  p.y, -p.z),
    lambda p: Point(-p.x, -p.y,  p.z),
    lambda p: Point(-p.x,  p.z,  p.y),
    lambda p: Point(-p.x,  -p.z,  -p.y),
    lambda p: Point(-p.y,  p.x,  p.z),
    lambda p: Point(-p.y, -p.x, -p.z),
    lambda p: Point(-p.y,  p.z, -p.x),
    lambda p: Point(-p.y, -p.z,  p.x),
    lambda p: Point(-p.z,  p.x,  -p.y),
    lambda p: Point(-p.z, -p.x,  p.y),
    lambda p: Point(-p.z,  p.y,  p.x),
    lambda p: Point(-p.z, -p.y, -p.x),
    lambda p: Point(-p.z, -p.x, -p.y),
    lambda p: Point( p.z,  p.x, -p.y),
]


def shift_reference(root, target, beacons):
    delta = Point(*[root[i] - target[i] for i in range(len(root))])

    return [Point(b.x + delta.x, b.y + delta.y, b.z + delta.z) for b in beacons], delta


def check_beacons_adjacent(beaconsA, beaconsB):
    for b_A in beaconsA:
        for b_B in beaconsB:
            shifted, delta = shift_reference(b_A, b_B, beaconsB)
            if len(set(shifted).intersection(set(beaconsA))) >= 12:
                return shifted, delta

    return False


def check_scanners_adjacent(scannerA, scannerB):
    for beaconsB in scannerB["orientations"]:
        if shifted := check_beacons_adjacent(scannerA["actual"], beaconsB):
            scannerB["actual"] = shifted[0]
            scannerB["orientations"] = [shifted[0]]
            scannerB["loc"] = shifted[1]
            return True

    return False


def align_scanners(_input):
    scanners = []
    breaks = [0] + [pos + 1 for pos, val in enumerate(_input) if val == ''] + [len(_input) + 1]

    for i, j in zip(breaks, breaks[1:]):
        idx = int(_input[i].split(' ')[-2])
        beacons = [Point(*map(int, b.split(','))) for b in _input[i+1:j-1]]
        scanners.append({
            "loc": Point(0,0,0),
            "actual": beacons,
            "adjacents": set(),
            "orientations": [beacons] if idx == 0 else  [[orientations[k](b) for b in beacons] for k in range(24)]})

        print(idx, len(beacons))


    queue = deque([0])
    while queue:
        cur = queue.pop()

        for i in range(len(scanners)):
            if i == cur or i in scanners[cur]["adjacents"]:
                continue

            print(cur, i)
            if check_scanners_adjacent(scanners[cur], scanners[i]):
                print("wah")
                queue.appendleft(i)
                scanners[cur]["adjacents"].add(i)
                scanners[i]["adjacents"].add(cur)

    return scanners

def part_one(_input):
    scanners = align_scanners(_input)
    return len(set.union(*[set(s["actual"]) for s in scanners]))

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def part_two(_input):
    scanners = align_scanners(_input)
    max_dist = float("-inf")

    for s1 in scanners:
        for s2 in scanners:
            max_dist = max(max_dist, manhattan(s1["loc"], s2["loc"]))

    return max_dist

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
