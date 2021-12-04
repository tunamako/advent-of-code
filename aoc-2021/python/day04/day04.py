from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np


YEAR = 2021
DAY = 4


class BingoBoard(object):

    def __init__(self, board_data):
        board_data = [[int(x) for x in row.strip().split(' ') if x != ''] for row in board_data]
        self.board = np.array(board_data, dtype=object)
        self.numbers = dict()

        for i in range(5):
            for j in range(5):
                self.numbers[self.board[i][j]] = [i, j, False]

    def calc_score(self, ball):
        score = sum(cell for cell, data in self.numbers.items() if not data[2])
        return score * ball

    def check_winning(self):
        for i in range(5):
            if all([self.numbers[cell][2] for cell in self.board[i]]):
                return True

        for j in range(5):
            col = [row[j] for row in self.board]

            if all([self.numbers[cell][2] for cell in col]):
                return True

        return False

    def call_number(self, ball):
        if ball in self.numbers:
            self.numbers[ball][2] = True

            if self.check_winning():
                return self.calc_score(ball)

        return None

def part_one(_input):
    raffle = list(map(int, _input[0].split(',')))
    boards = set()

    for i in range(1, len(_input), 6):
        boards.add(BingoBoard(_input[i+1:i+6]))

    for ball in raffle:
        for board in boards:
            score = board.call_number(ball)
            if score:
                return score

def part_two(_input):
    raffle = list(map(int, _input[0].split(',')))
    boards = []

    for i in range(1, len(_input), 6):
        boards.append([BingoBoard(_input[i+1:i+6]), False])

    for ball in raffle:
        for board in boards:
            score = board[0].call_number(ball)
            if score:
                board[1] = True
            if all([b[1] for b in boards]):
                return score


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line.strip() for line in open('input').readlines()]
    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
