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
DAY = 7


class Directory():

    def __init__(self, parent, name):

        self.parent = parent
        self.name = name
        self.children = dict()

    def calc_sizes(self):
        self.size = sum([child.calc_sizes() for child in self.children.values()])
        return self.size

    def add_child(self, size, name):
        self.children[name] = Directory(self, name) if size == 'dir' else File(self, name, int(size))

class File():
    def __init__(self, parent, name, size):

        self.parent = parent
        self.name = name
        self.size = size

    def calc_sizes(self):
        return self.size

def construct_directories(_input):
    pwd = Directory(None, '/')
    root = pwd
    flat_dirs = {root}

    line = 1
    while line < len(_input):
        if 'cd' in _input[line]:
            next_dir = _input[line].split(' ')[-1]
            if next_dir == '..':
                pwd = pwd.parent
            else:
                pwd = pwd.children[next_dir]
                flat_dirs.add(pwd)
            line += 1
        elif 'ls' in _input[line]:
            line += 1
            while line < len(_input) and _input[line][0] != '$':
                pwd.add_child(*_input[line].split(' '))
                line += 1

    root.calc_sizes()
    return root, flat_dirs

def part_one(_input):
    root, flat_dirs = construct_directories(_input)

    return sum(_dir.size for _dir in flat_dirs if _dir.size <= 100000)

def part_two(_input):
    root, flat_dirs = construct_directories(_input)

    delta = 30000000 - (70000000 - root.size)

    return min(_dir.size for _dir in flat_dirs if _dir.size >= delta)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
