from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *

YEAR = 2021
DAY = 12


def parse_caves(cave_list):
    caves = defaultdict(set)

    for line in cave_list:
        lhs, rhs = line.split('-')
        if rhs != "start": caves[lhs].add(rhs)
        if lhs != "start": caves[rhs].add(lhs)

    return caves


def gen_paths(caves, cur="start", cur_path="start"):
    if cur == "end":
        return 1

    cur_path += cur
    paths = 0

    for adj in caves[cur]:
        if (adj.islower() and adj in cur_path):
            continue
        paths += gen_paths(caves, adj, cur_path)

    return paths


def part_one(_input):
    caves = parse_caves(_input)
    return gen_paths(caves, "start")


def gen_paths2(caves, cur, cur_path=defaultdict(int), used_second=False):
    if cur == "end":
        return 1

    cur_path[cur] += 1
    paths = 0

    for adj in caves[cur]:
        if adj.islower() and cur_path[adj]:
            if used_second:
                continue
            else:
                paths += gen_paths2(caves, adj, cur_path, True)
        else:
            paths += gen_paths2(caves, adj, cur_path, used_second)

    cur_path[cur] -= 1
    return paths


def part_two(_input):
    caves = parse_caves(_input)
    return gen_paths2(caves, "start")


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for 1line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('part_one(_input)')
    #cProfile.run('part_two(_input)')
