from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 3


def get_commonality(data, index):
    ones = sum([int(string[index]) for string in data])
    zeroes = len(data) - ones

    return str(int(ones >= zeroes)), str(int(ones < zeroes))


def part_one(_input):
    gamma, epsilon = "", ""

    for i in range(len(_input[0])):
        most, least = get_commonality(_input, i)
        gamma += most
        epsilon += least

    return int(gamma, 2) * int(epsilon, 2)


def reduce(data, use_most):
    for i in range(len(next(iter(data), None))):
        if len(data) == 1:
            break

        most, least = get_commonality(data, i)
        criteria = most if use_most else least

        data = {string for string in data if string[i] == criteria}

    return int(data.pop(), 2)


def part_two(_input):
    return reduce(set(_input), True) * reduce(set(_input), False)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
