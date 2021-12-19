from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 17


class Probe(object):

    def __init__(self, target):
        _, _, tar_x, tar_y = target.split(' ')
        self.tar_x = tuple(map(int, tar_x[2:-1].split('..')))
        self.tar_y = tuple(map(int, tar_y[2:].split('..')))

        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0
        self.max_height = float('-inf')

    def step(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1

        self.y_vel -= 1

    def reached_target(self):
        return (self.tar_x[0] <= self.x <= self.tar_x[1]) \
                and (self.tar_y[0] <= self.y <= self.tar_y[1])

    def launch(self, x_vel, y_vel):
        self.reset()
        self.x_vel, self.y_vel = x_vel, y_vel
        x_passed, y_passed = False, False

        while True:
            if self.reached_target():
                return True

            prev_x, prev_y = self.x, self.y
            self.step()
            self.max_height = max(self.y, self.max_height)

            if self.x_vel == 0 and self.y < self.tar_y[0]:
                # Freefalling
                return False

            if self.x > self.tar_x[1]:
                x_passed = True
            if self.y < self.tar_y[0]:
                y_passed = True

            if x_passed and y_passed:
                return False


def part_one(_input):
    probe = Probe(_input)

    max_vel = probe.tar_x[1] + 1
    max_height = float("-inf")
    for x in range(max_vel):
        for y in range(max_vel):
            if probe.launch(x, y):
                if probe.max_height > max_height:
                    max_height = max(max_height, probe.max_height)

    return max_height


def part_two(_input):
    probe = Probe(_input)

    min_vel = probe.tar_y[0] - 1
    max_vel = probe.tar_x[1] + 1

    count = 0
    for x in range(min_vel, max_vel):
        for y in range(min_vel, max_vel):
            if probe.launch(x, y):
                count += 1

    return count


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')[0]
    #_input = open('input').readlines()[0]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
