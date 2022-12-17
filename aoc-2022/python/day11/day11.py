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
DAY = 11

divisors = [23, 19, 13, 17]


class Monkey:

    def initialize(self, init_strings, monkeys):
        self.inspect_count = 0

        self.id = int(init_strings[0][-2])
        self.items = list(map(int, init_strings[1].split(': ')[-1].split(', ')))

        self.op = init_strings[2].split(': ')[-1]
        if self.op[-3:] == "old":
            self.op = lambda x: x * x
        else:
            value = int(self.op.split(' ')[-1])
            if '*' in self.op:
                self.op = lambda x: x * value
            else:
                self.op = lambda x: x + value

        self.divisor = int(init_strings[3].split(' ')[-1])
        self.test = lambda x: x % self.divisor == 0

        self.true_throw = monkeys[int(init_strings[4].split(' ')[-1])]
        self.false_throw = monkeys[int(init_strings[5].split(' ')[-1])]

    def take_turn(self, p2=False, lcm=None):
        for i in range(len(self.items)):
            self.inspect_count += 1
            self.items[i] = self.op(self.items[i])
            if not p2: self.items[i] //= 3
            if lcm: self.items[i] %= lcm

            throw = self.true_throw if self.test(self.items[i]) else self.false_throw
            throw.items.append(self.items[i])

        self.items = []

def part_one(_input):
    monkeys = [Monkey() for i in range(0, len(_input), 7)]

    for i in range(0, len(_input), 7):
        monkeys[i // 7].initialize(_input[i:i+6], monkeys)

    for i in range(20):
        for mank in monkeys:
            mank.take_turn()

    monkeys.sort(reverse=True, key=lambda m: m.inspect_count)
    return monkeys[0].inspect_count * monkeys[1].inspect_count

def part_two(_input):
    monkeys = [Monkey() for i in range(0, len(_input), 7)]
    for i in range(0, len(_input), 7):
        monkeys[i // 7].initialize(_input[i:i+6], monkeys)

    lcm = math.lcm(*[m.divisor for m in monkeys])

    for i in range(10000):
        for mank in monkeys:
            mank.take_turn(p2=True, lcm=lcm)

    monkeys.sort(reverse=True, key=lambda m: m.inspect_count)
    return monkeys[0].inspect_count * monkeys[1].inspect_count

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
