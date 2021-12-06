from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 6


def part_one(_input):
    fishes = list(map(int, _input.split(',')))
    print(_input)

    for i in range(80):
        print(i)
        to_add = []
        for j in range(len(fishes)):
            if fishes[j] == 0:
                to_add.append(8)
                fishes[j] = 6
            else:
                fishes[j] -= 1
        fishes += to_add
    return len(fishes)

def part_two(_input):
    fishes = list(map(int, _input.split(',')))

    for i in range(80):
        #print(fishes)
        to_add = []
        for j in range(len(fishes)):
            if fishes[j] == 0:
                to_add.append(8)
                fishes[j] = 6
            else:
                fishes[j] -= 1

        fishes += to_add
    return len(fishes)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')[0]
    #_input = open('input').readlines()[0]

    #print(part_one(_input))
    #print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    cProfile.run('print(part_two(_input))')
