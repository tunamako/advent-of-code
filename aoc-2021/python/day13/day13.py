from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np

YEAR = 2021
DAY = 13


def parse_input(_input):
    split = _input.index('')
    dots = []
    for line in _input[:split]:
        x, y = line.split(',')
        dots.append({'x': int(x), 'y': int(y)})

    folds = []
    for line in _input[split+1:]:
        f = line.split(' ')[-1].split('=')
        f = (f[0], int(f[1]))
        folds.append(f)

    return dots, folds


def prune_dupes(dots):
    unique = set()
    for d in dots:
        unique.add((d['x'], d['y']))

    return [{'x': int(d[0]), 'y': int(d[1])} for d in unique]


def part_one(_input):
    dots, folds = parse_input(_input)
    f = folds[0]
    for dot in filter(lambda d: d[f[0]] > f[1], dots):
        delta = dot[f[0]] - f[1]
        dot[f[0]] -= 2 * delta

    dots = prune_dupes(dots)
    return len(dots)


def print_paper(dots):
    max_x = max([d['x'] for d in dots])
    max_y = max([d['y'] for d in dots])

    paper = np.full((max_x + 1, max_y + 1), ' ', )
    for d in dots:
        paper[d['x']][d['y']] = '#'

    paper = np.swapaxes(paper, 0, 1)
    for line in paper:
        print(''.join(line))


def part_two(_input):
    dots, folds = parse_input(_input)

    for f in folds:
        for dot in filter(lambda d: d[f[0]] > f[1], dots):
            delta = dot[f[0]] - f[1]
            dot[f[0]] -= 2 * delta

        dots = prune_dupes(dots)

    print_paper(dots)


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    part_two(_input)

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
