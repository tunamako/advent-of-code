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
import networkx as nx

YEAR = 2024
DAY = 23

def generate_graph(_input):
    graph = nx.Graph()

    for line in _input:
        a, b = line.split('-')
        graph.add_edge(a, b)

    return graph

def part_one(_input):
    graph = generate_graph(_input)
    cycles = {tuple(sorted(c)) for c in nx.simple_cycles(graph, 3)}

    return sum(1 for cyc in cycles if any(comp.startswith('t') for comp in cyc))

def part_two(_input):
    graph = generate_graph(_input)
    cliques = [c for c in nx.find_cliques(graph)]
    biggest = sorted(cliques, key=lambda c: len(c))[-1]

    return ','.join(sorted(biggest))

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day23/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
