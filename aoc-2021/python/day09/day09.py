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
    low_points = []
    for pos in zip(*np.where(heatmap != "9")):
        height = heatmap[pos[0]][pos[1]]

        is_low = True
        for d in directions:
            try:
                if heatmap[pos[0] + d[0]][pos[1] + d[1]] <= height:
                    is_low = False
            except:
                pass

        if is_low:
            low_points.append(Point(*pos))

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
