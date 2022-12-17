from aocd.models import Puzzle

import cProfile
import functools
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *
import numpy as np
import sys
from copy import deepcopy

YEAR = 2022
DAY = 13


def correct_order(a, b):
    if type(a) is type(b) is int:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

    elif type(a) is type(b) is list:
        for i in range(max(len(a), len(b))):
            if i == len(b):
                return -1
            elif i == len(a):
                return 1

            res = correct_order(a[i], b[i])
            if res != 0:
                return res

        return 0

    elif type(a) is int:
        a = [a]
    elif type(b) is int:
        b = [b]

    return correct_order(a, b)

def part_one(_input):
    pairs = []
    for i in range(0, len(_input), 3):
        pairs.append([eval(_input[i]), eval(_input[i+1])])

    ret = 0
    for i in range(len(pairs)):
        if correct_order(*pairs[i]) > -1:
            ret += i + 1

    return ret

def part_two(_input):
    packets = [[[2]], [[6]]]
    for i in range(0, len(_input), 3):
        packets += [eval(_input[i]), eval(_input[i+1])]

    packets.sort(reverse=True, key=functools.cmp_to_key(correct_order))

    ret = 1
    for i in range(len(packets)):
        if packets[i] == [[2]]:
            ret *= i + 1
        elif packets[i] == [[6]]:
            ret *= i + 1

    return ret

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
