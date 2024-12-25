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

YEAR = 2024
DAY = 24

NODES = {}

class Node:

    def __init__(self, _id, lhs_id, rhs_id):
        self._id = _id
        self.lhs_id = lhs_id
        self.rhs_id = rhs_id

class RootNode(Node):

    def __init__(self, _id, state):
        self.state = state

    def evaluate(self):
        return self.state

class OrNode(Node):

    def evaluate(self):
        return NODES[self.lhs_id].evaluate() | NODES[self.rhs_id].evaluate()

class AndNode(Node):

    def evaluate(self):
        return NODES[self.lhs_id].evaluate() & NODES[self.rhs_id].evaluate()

class XORNode(Node):

    def evaluate(self):
        return NODES[self.lhs_id].evaluate() ^ NODES[self.rhs_id].evaluate()


def parse_nodes(_input):
    split = _input.index('')

    for wire in _input[:split]:
        wire, state = wire.split(': ')
        NODES[wire] = RootNode(wire, int(state))
    counters = {'AND': 0, 'OR': 0, 'XOR': 0}
    for gate in sorted(_input[split+1:]):
        print(gate)
        lhs_id, _type, rhs_id, _, _id = gate.split(' ')
        print(lhs_id, "->", f"{_type}{counters[_type]}")
        print(rhs_id, "->", f"{_type}{counters[_type]}")
        print(f"{_type}{counters[_type]}", "->", _id)
        counters[_type] += 1

        if _type == "AND":
            NODES[_id] = AndNode(_id, lhs_id, rhs_id)
        elif _type == "OR":
            NODES[_id] = OrNode(_id, lhs_id, rhs_id)
        elif _type == "XOR":
            NODES[_id] = XORNode(_id, lhs_id, rhs_id)

def part_one(_input):
    parse_nodes(_input)

    leafnodes = sorted([_id for _id in NODES if _id.startswith('z')], reverse=True)
    ret = ''
    for _id in leafnodes:
        print(_id, NODES[_id].evaluate())
        ret += str(NODES[_id].evaluate()) 

    return int(ret, base=2)

def test_add(x, y):
    x_nodes = sorted([_id for _id in NODES if _id.startswith('x')])
    y_nodes = sorted([_id for _id in NODES if _id.startswith('y')])
    z_nodes = sorted([_id for _id in NODES if _id.startswith('z')])

    z = x + y
    x = "{0:b}".format(x).zfill(len(x_nodes))
    y = "{0:b}".format(y).zfill(len(y_nodes))
    z = "{0:b}".format(z).zfill(len(z_nodes))

    for i, state in enumerate(x):
        NODES[x_nodes[i]].state = int(state)

    for i, state in enumerate(y):
        NODES[y_nodes[i]].state = int(state)

    z_actual = []
    for _id in z_nodes:
        z_actual.insert(0, NODES[_id].evaluate())
    z_actual = ''.join(map(str, z_actual))
    print(z)
    print(z_actual)
    print()



def part_two(_input):
    parse_nodes(_input)
    #exit()
    swaps = [
        "z09", "cwt",
        "z05", "gdd",
        "css", "jmv",
        "z37", "pqt",
    ]

    #for i in range(44):
    #    tmp = int(math.pow(2, i))
    #    test_add(i, i+1)

    return ','.join(sorted(swaps))


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    _input = [line[:-1] for line in open('aoc-2024/day24/input.txt').readlines()]

    #print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')


