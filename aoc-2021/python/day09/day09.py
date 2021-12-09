from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
import numpy as np

YEAR = 2021
DAY = 9

Point = namedtuple("Point", ['x', 'y']) 
directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}


def get_low_points(heatmap):
    dimx = len(heatmap)
    dimy = len(heatmap[0])

    low_points = []
    for x in range(dimx):
        for y in range(dimy):
            is_low = True
            for d in directions:
                i, j = x + d[0], y + d[1]
                if (dimx > i >= 0 and dimy > j >= 0):
                    if heatmap[i][j] <= heatmap[x][y]:
                        is_low = False

            if is_low:
                low_points.append(Point(x, y))

    return low_points


def part_one(_input):
    heatmap = np.swapaxes(np.array(_input), 0, 1)
    low_points = get_low_points(heatmap)

    return sum([1 + int(heatmap[p.x][p.y]) for p in low_points])


def get_basin(heatmap, sink):
    seen = set()
    queue = {sink}

    while queue:
        cur = queue.pop()
        seen.add(cur)
        for d in directions:
            t = Point(cur.x + d[0], cur.y + d[1])
            if (len(heatmap) > t.x >= 0 and len(heatmap[0]) > t.y >= 0 \
                and t not in seen \
                and '9' > heatmap[t.x][t.y] > heatmap[cur.x][cur.y]):

                queue.add(t)

    return len(seen)


def part_two(_input):
    heatmap = np.swapaxes(np.array(_input), 0, 1)
    basins = sorted([get_basin(heatmap, p) for p in get_low_points(heatmap)], reverse=True)

    return math.prod(basins[:3])


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = [list(line) for line in puzzle.input_data.split('\n')]
    #_input = [list(line[:-1]) for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
