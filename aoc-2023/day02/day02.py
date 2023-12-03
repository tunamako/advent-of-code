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

YEAR = 2023
DAY = 2


class Game():

    def __init__(self, initstring):
        self.id = int(initstring.split(': ')[0].split(' ')[1])
        self.batches = []

        for raw_batch in initstring.split(': ')[1].split('; '):
            batch = dict()
            colors = raw_batch.split(', ')
            for color in colors:
                num, color = color.split(' ')
                batch[color] = int(num)
            self.batches.append(batch)

    def is_possible(self, counts):
        for batch in self.batches:
            for color in counts:
                if color in batch and batch[color] > counts[color]:
                    return False
        return True

    def get_power(self):
        max_red = max([batch["red"] for batch in self.batches if "red" in batch])
        max_green = max([batch["green"] for batch in self.batches if "green" in batch])
        max_blue = max([batch["blue"] for batch in self.batches if "blue" in batch])

        return max_red * max_green * max_blue

def part_one(_input):
    games = [Game(line) for line in _input]
    ret = 0
    counts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for game in games:
        if game.is_possible(counts):
            ret += game.id

    return ret

def part_two(_input):
    return sum(Game(line).get_power() for line in _input)

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
