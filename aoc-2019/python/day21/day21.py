from aocd.models import Puzzle
import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math

from advent_machine import AdventMachine, Paintbot


def part_one(_input):
    pass


def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=2019, day=21)
    _input = puzzle.input_data.split('\n')
    print(_input)
    #_input = open('bigboy').readlines()

    print(part_one(_input))
    #print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
