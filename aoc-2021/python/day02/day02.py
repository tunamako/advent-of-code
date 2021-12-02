from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 2


def part_one(_input):
    xpos, ypos = 0, 0

    for line in _input:
        cmd, count = line.split(' ')

        if cmd == "forward":
            xpos += int(count)
        elif cmd == "up":
            ypos -= int(count)
        elif cmd == "down":
            ypos += int(count)

    return xpos * ypos

def part_two(_input):
    xpos, ypos, aim = 0, 0, 0

    for line in _input:
        cmd, count = line.split(' ')

        if cmd == "forward":
            xpos += int(count)
            ypos += int(count) * aim
        elif cmd == "up":
            aim -= int(count)
        elif cmd == "down":
            aim += int(count)

    return xpos * ypos


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = open('bigboy').readlines()

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
