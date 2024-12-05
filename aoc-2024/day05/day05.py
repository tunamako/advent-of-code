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
DAY = 5


def is_ordered(rules, update):
    is_ordered = True
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue

        is_ordered &= update.index(rule[0]) < update.index(rule[1])

    return is_ordered

def order_update(rules, update):
    update_at_start = update[::]

    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        elif update.index(rule[0]) > update.index(rule[1]):
            update.insert(update.index(rule[0]), update.pop(update.index(rule[1])))

    if update == update_at_start:
        return update
    else:
        return order_update(rules, update)

def solve(_input):
    divider = _input.index("")
    updates = [list(map(int, update.split(','))) for update in _input[divider + 1:]]

    page_rules = []
    for rule in _input[:divider]:
        page_rules.append(tuple(map(int, rule.split('|'))))

    ret_p1 = 0
    ret_p2 = 0
    for update in updates:
        if is_ordered(page_rules, update):
            ret_p1 += update[int(math.ceil((len(update) - 1)/2))]
        else:
            ordered = order_update(page_rules, update)
            ret_p2 += ordered[int(math.ceil((len(ordered) - 1)/2))]

    return ret_p1, ret_p2


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day05/input.txt').readlines()]

    print(solve(_input))
    #print(part_two(_input))

    #cProfile.run('print(solve(_input))')
    #cProfile.run('print(part_two(_input))')
