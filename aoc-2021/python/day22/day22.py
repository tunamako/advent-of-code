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

Point = namedtuple("Point", ['x', 'y', 'z']) 

YEAR = 2021
DAY = 22

class Cuboid(object):

    def __init__(self, state, coords, _id):
        self._id = _id
        self.state = state
        self.x = tuple(map(int, coords[0][2:].split('..')))
        self.y = tuple(map(int, coords[1][2:].split('..')))
        self.z = tuple(map(int, coords[2][2:].split('..')))

        self.cubecount = abs(self.x[0] - self.x[1]) + 1
        self.cubecount *= abs(self.y[0] - self.y[1]) + 1
        self.cubecount *= abs(self.z[0] - self.z[1]) + 1

        self.cubeson = 0

        self.neighbors = dict()

    def check_overlap(self, cuboid):
        if self in cuboid.neighbors:
            return

        x_overlap = min(self.x[1], cuboid.x[1]) - max(self.x[0], cuboid.x[0])
        y_overlap = min(self.y[1], cuboid.y[1]) - max(self.y[0], cuboid.y[0])
        z_overlap = min(self.z[1], cuboid.z[1]) - max(self.z[0], cuboid.z[0])
        amount = 0

        if x_overlap >= 0 and y_overlap >= 0 and z_overlap >= 0:
            amount = (x_overlap + 1) * (y_overlap + 1) * (z_overlap + 1)
            self.neighbors[cuboid._id] = [cuboid, amount]
            cuboid.neighbors[self._id] = [self, amount]

    def apply_state(self):
        if self.state:
            self.cubeson = self.cubecount
            for cuboid, amount in self.neighbors.values():
                pass
        else:
            self.cubeson = 0


def part_one(_input):
    print(_input)
    cuboids = []

    for i, line in enumerate(_input):
        state, coords = line.split(' ')
        state = 1 if state == "on" else 0
        coords = coords.split(',')

        cuboids.append(Cuboid(state, coords, i))

    for c1 in cuboids:
        for c2 in cuboids:
            if c1 is c2:
                continue
            c1.check_overlap(c2)

    print(cuboids[0].neighbors)

    for c in cuboids:
        c.apply_state()

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
