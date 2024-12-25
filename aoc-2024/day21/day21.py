from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, pairwise, product
import re
import math
from pprint import pprint
import numpy as np
import pandas as pd
import sys
from copy import deepcopy
import networkx as nx

YEAR = 2024
DAY = 21
Point = namedtuple("Point", ['x', 'y'])

class Robot:

    MOVES = {
        Point(0, 1): '^',
        Point(1, 0): '>',
        Point(0, -1): 'v',
        Point(-1, 0): '<',
    }

    def __init__(self, pad_count, depth=0):
        self.depth = depth

        if depth < pad_count:
            self.presser = DirPad(pad_count, depth+1)
        else:
            self.presser = NullPad(pad_count, depth)

        self.cache = {}

    @classmethod
    def generate_paths(cls):
        if cls.SHORTEST_PATHS is not None:
            return

        graph = nx.DiGraph()

        for pos, b in cls.BUTTON_POSITIONS.items():
            for m, m_str in cls.MOVES.items():
                m_pos = Point(pos.x + m.x, pos.y + m.y)
                if m_pos in cls.BUTTON_POSITIONS:
                    graph.add_edge(b, cls.BUTTON_POSITIONS[m_pos], move=m_str)

        shortest_paths = defaultdict(list)

        for start, end in permutations(cls.BUTTON_POSITIONS.values(), 2):
            if start == end:
                continue

            for path in nx.all_shortest_paths(graph, start, end):
                xpath = ""

                for pair in pairwise(path):
                    xpath = xpath + graph.get_edge_data(pair[0], pair[1])["move"]
                shortest_paths[(start, end)].append(xpath)

        cls.SHORTEST_PATHS = shortest_paths

    def input_code(self, code):
        ret = 0
        for state in pairwise('A' + code):
            if state[0] == state[1]:
                ret += 1 
                continue

            if state not in self.cache:
                wah = [self.presser.input_code(translated + 'A') for translated in self.SHORTEST_PATHS[state]]
                self.cache[state] = min(wah)
            ret += self.cache[state]

        return ret

class NullPad(Robot):

    def __init__(self, pad_count, depth=0):
        pass

    def input_code(self, code):
        return len(code)

class KeyPad(Robot):

    BUTTON_POSITIONS = {
        Point(2, 0): 'A',
        Point(1, 0): '0',
        Point(0, 1): '1',
        Point(1, 1): '2',
        Point(2, 1): '3',
        Point(0, 2): '4',
        Point(1, 2): '5',
        Point(2, 2): '6',
        Point(0, 3): '7',
        Point(1, 3): '8',
        Point(2, 3): '9',
    }
    SHORTEST_PATHS = None

class DirPad(Robot):

    BUTTON_POSITIONS = {
        Point(0, 0): '<',
        Point(1, 0): 'v',
        Point(2, 0): '>',
        Point(1, 1): '^',
        Point(2, 1): 'A',
    }
    SHORTEST_PATHS = None


def part_one(_input):
    KeyPad.generate_paths()
    DirPad.generate_paths()
    keypad = KeyPad(2)

    return sum(int(code[:-1]) * keypad.input_code(code) for code in _input)

def part_two(_input):
    KeyPad.generate_paths()
    DirPad.generate_paths()
    keypad = KeyPad(25)

    return sum(int(code[:-1]) * keypad.input_code(code) for code in _input)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day21/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
