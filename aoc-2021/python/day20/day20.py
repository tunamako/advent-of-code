from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np

YEAR = 2021
DAY = 20

directions = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def next_generation(image, algo, step):
    ret = np.copy(image)

    for x in range(len(image)):
        for y in range(len(image[0])):
            binary = ''
            for d in directions:
                dx, dy = x+d[0], y+d[1]
                if (0 <= dx < len(image)) and (0 <= dy < len(image[0])):
                    binary += str(image[dx][dy])
                elif algo[0] == '#':
                    binary += str(step % 2)
                else:
                    binary += '0'

            ret[x][y] = 1 if algo[int(binary, 2)] == '#' else 0

    return ret

def expand_image(image, value=0):
    return np.pad(image, pad_width=50, mode='constant', constant_values=value)

def print_image(image):
    for line in np.swapaxes(image, 0, 1):
        print(''.join([str(c) for c in line]))

def part_one(_input):
    algo = _input[0]
    image = np.array([list(line) for line in _input[2:]])
    image = np.swapaxes(image, 0, 1)
    image = np.where(image == '#', 1, 0)
    image = expand_image(image)

    for i in range(50):
        print(i)
        image = next_generation(image, algo, i)

    return np.count_nonzero(image == 1)

def part_two(_input):
    pass


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
