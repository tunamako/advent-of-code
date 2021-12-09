from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import *
from copy import deepcopy

YEAR = 2021
DAY = 8


def part_one(_input):
    unique = 0
    for entry in _input:
        output = entry.split(' | ')[1].split(' ')
        print(output)
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                print(digit)
                unique += 1

    return unique


def find_matches(num_map):
    horizontals = [char for char in num_map[2][0] if char in num_map[2][1] and char in  num_map[2][2]]
    a, d, g = "", "", ""

    for x in horizontals:
        if all([x in num_map[0][0] and x in num_map[0][1] and x in num_map[0][2]]):
            if x in num_map[7][0]:
                a = x
            else:
                g = x
        else:
            d = x

    for x in num_map[0]:
        if d not in x:
            num_map[0] = x
            num_map[6].remove(x)
            num_map[9].remove(x)
            break

    c, f = "", ""
    for x in num_map[1]:
        if x in set(num_map[6][0]).intersection(set(num_map[6][1])):
            f = x
        else:
            c = x

    tmp = num_map[6]
    num_map[6] = tmp[0] if c not in tmp[0] else tmp[1]
    num_map[9] = tmp[0] if c in tmp[0] else tmp[1]

    for x in num_map[2]:
        if c not in x:
            five = x
        elif f in x:
            three = x
        else:
            two = x
    num_map[2] = two
    num_map[3] = three
    num_map[5] = five

    return num_map


def calc_output(display):
    signals, output = [x.split(' ') for x in display.split(' | ')]
    signals = ["".join(sorted(x)) for x in signals]
    output = ["".join(sorted(x)) for x in output]
    num_map = [list() for i in range(10)]

    for s in signals:
        if len(s) == 2: # One
            num_map[1] = s
        elif len(s) == 3: # Seven
            num_map[7] = s
        elif len(s) == 4: # Four
            num_map[4] = s
        elif len(s) == 5: # Two, Three, Five
            num_map[2].append(s)
            num_map[3].append(s)
            num_map[5].append(s)
        elif len(s) == 6: # Zero, Six, Nine
            num_map[0].append(s)
            num_map[6].append(s)
            num_map[9].append(s)
        elif len(s) == 7: # Eight
            num_map[8] = s

    num_map = {signals: str(i) for i, signals in enumerate(find_matches(num_map))}

    return int(''.join([num_map[digit] for digit in output]))


def part_two(_input):
     return sum([calc_output(display) for display in _input])


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    #print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
