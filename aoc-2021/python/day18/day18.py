from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import ast
from copy import deepcopy

YEAR = 2021
DAY = 18


class Pair(object):

    def __init__(self, pair_list=None, parent=None):
        self.parent = parent
        self.is_number = False
        if pair_list is None:
            return

        if isinstance(pair_list[0], list):
            self.lhs = Pair(pair_list[0], self)
        else:
            self.lhs = Number(pair_list[0], self)

        if isinstance(pair_list[1], list):
            self.rhs = Pair(pair_list[1], self)
        else:
            self.rhs = Number(pair_list[1], self)

    def __repr__(self):
        return "[{},{}]".format(self.lhs, self.rhs)

    def __add__(self, other):
        tmp = Pair()
        tmp.lhs = self.lhs
        tmp.rhs = self.rhs
        tmp.lhs.parent = tmp
        tmp.rhs.parent = tmp
        tmp.parent = self
        self.lhs = tmp
        self.rhs = other
        other.parent = self

        return self

    def depth(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.depth() + 1

    def explode(self):
        if self.depth() < 4:
            retl = self.lhs.explode()
            retr = self.rhs.explode()
            return bool(retl) or bool(retr)

        elif self.lhs.is_number and self.rhs.is_number:
            # Need to esplod self
            pair = self
            while pair.parent:
                if pair.parent.lhs is not pair:
                    pair = pair.parent.lhs
                    while not pair.is_number:
                        pair = pair.rhs
                    pair.value += self.lhs.value
                    break

                pair = pair.parent

            pair = self
            while pair.parent:
                if pair.parent.rhs is not pair:
                    pair = pair.parent.rhs
                    while not pair.is_number:
                        pair = pair.lhs
                    pair.value += self.rhs.value
                    break

                pair = pair.parent

            if self.parent.lhs is self:
                self.parent.lhs = Number(0, self.parent)
            elif self.parent.rhs is self:
                self.parent.rhs = Number(0, self.parent)

            return 1
        return 0

    def reduce(self):
        while True:
            exploded = self.explode()
            splitted = self.split()
            if not exploded and not splitted:
                break

    def split(self):
        if self.lhs.split():
            return 1
        if self.rhs.split():
            return 1

        return 0

    def magnitude(self):
        return (3 * self.lhs.magnitude()) + (2 * self.rhs.magnitude())

class Number(Pair):

    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.is_number = True

    def __repr__(self):
        return str(self.value)

    def explode(self):
        pass

    def split(self):
        if self.value >= 10:
            new_lhs = self.value // 2
            new_rhs = math.ceil(self.value / 2)

            pair = Pair([new_lhs, new_rhs], self.parent)

            if self.parent.lhs is self:
                self.parent.lhs = pair
            elif self.parent.rhs is self:
                self.parent.rhs = pair
            return 1
        else:
            return 0

    def magnitude(self):
        return self.value


def part_one(_input):
    pair_list = [ast.literal_eval(pair) for pair in _input]

    pair = Pair(pair_list[0])
    for next_pair in pair_list[1:]:
        pair += Pair(next_pair)
        pair.reduce()

    return pair.magnitude()

def part_two(_input):
    pair_list = [ast.literal_eval(pair) for pair in _input]

    max_mag = float("-inf")
    for perm in permutations(pair_list, 2):
        pair_1, pair_2 = Pair(deepcopy(perm[0])), Pair(deepcopy(perm[1]))
        pair_1 += pair_2
        pair_1.reduce()
        max_mag = max(max_mag, pair_1.magnitude())

    return max_mag

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    cProfile.run('print(part_two(_input))')
