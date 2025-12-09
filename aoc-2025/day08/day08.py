from aocd.models import Puzzle
from advent_lib.grid_helpers import parse_text_to_ndarray, get_neighbors, Point3D, DIRECTIONS

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
from functools import reduce
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
import os
import networkx as nx
import heapq
from heapdict import heapdict
YEAR = 2025
DAY = 8


def generate_points(_input):
    points = {Point3D(*map(int, line.split(','))) for line in _input}
    point_pairs = [(p, q) for p, q in combinations(points, 2)]
    point_pairs = sorted(point_pairs, key=lambda pair: pair[0].distance(pair[1]), reverse=True)
    return points, point_pairs

def part_one(_input):
    _, point_pairs = generate_points(_input)
    graph = nx.Graph()

    for i in range(1000):
        closest_pair = point_pairs.pop()
        graph.add_edge(*closest_pair)

    cliques = [c for c in nx.connected_components(graph)]
    cliques = sorted([len(c) for c in cliques], reverse=True)

    return cliques[0] * cliques[1] * cliques[2]

def part_two(_input):
    points, point_pairs = generate_points(_input)
    graph = nx.Graph()

    while True:
        closest_pair = point_pairs.pop()
        graph.add_edge(*closest_pair)
        components = [c for c in nx.connected_components(graph)]
        if len(components) == 1 and len(components[0]) == len(points):
            return closest_pair[0].x * closest_pair[1].x


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #_input = [line[:-1] for line in open(os.path.join(dir_path, 'bigboy.txt')).readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
