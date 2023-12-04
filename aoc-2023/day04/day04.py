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
DAY = 4


class Card():

    def __init__(self, initstring):
        self.id = int(initstring.split(': ')[0].split(' ')[-1])
        initstring = initstring.split(':')[1].replace('  ', ' 0')[1:]

        self.numbers = list(map(int, initstring.split(' | ')[1].split(' ')))
        self.winning_numbers = set(map(int, initstring.split(' | ')[0].split(' ')))
        self.matches = len([n for n in self.numbers if n in self.winning_numbers])
        self.copies = 0

    def calc_points(self):
        return int(pow(2, self.matches - 1))

    def calc_copies(self, cards):
        if not self.copies:
            if self.matches:
                self.copies = 1 + sum(cards[self.id+i].calc_copies(cards) for i in range(1, self.matches+1))
            else:
                self.copies = 1

        return self.copies

def part_one(_input):
    return sum(Card(line).calc_points() for line in _input)

def part_two(_input):
    cards = dict()
    for line in _input:
        card = Card(line)
        cards[card.id] = card

    return sum(card.calc_copies(cards ) for card in cards.values())

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
