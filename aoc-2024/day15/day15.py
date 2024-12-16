from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, cycle
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy

np.set_printoptions(threshold=sys.maxsize)

YEAR = 2024
DAY = 15

Point = namedtuple("Point", ['x', 'y']) 
moves = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1),
}

def try_simple_shift(x, y, move, grid):
    next_x, next_y = x + moves[move][0], y + moves[move][1]
    item = grid[x][y]

    if grid[next_x][next_y] == '#':
        return False
    elif grid[next_x][next_y] == '.' or try_simple_shift(next_x, next_y, move, grid):
        grid[next_x][next_y] = item
        grid[x][y] = '.'
        return True

def print_state(grid):
    tmp = np.swapaxes(grid, 0, 1)
    for line in tmp:
        print(''.join(line))
    print()

def part_one(_input):
    split = _input.index('')
    grid = np.array([list(line) for line in _input[:split]])
    grid = np.swapaxes(grid, 0, 1)

    tape = ''.join(_input[split:])

    start_pos = np.where(grid == '@')
    x, y = int(start_pos[0][0]), int(start_pos[1][0])
    print_state(grid)

    for move in tape:
        if try_simple_shift(x, y, move, grid):
            x, y = x + moves[move][0], y + moves[move][1]

    print_state(grid)
    
    ret = 0
    for x, y in  zip(*np.where(grid == 'O')):
        ret += 100 * y + x
    
    return ret

def can_be_moved(pos, move, grid):
    item = grid[pos]

    if item == '[':
        l = Point(pos.x, pos.y)
        r = Point(pos.x + 1, pos.y)
    elif item == ']':
        l = Point(pos.x - 1, pos.y)
        r = Point(pos.x, pos.y)
    elif item in ".@":
        return True
    elif item == '#':
        return False

    next_l = Point(l.x + moves[move][0], l.y + moves[move][1])
    next_r = Point(r.x + moves[move][0], r.y + moves[move][1])

    if grid[next_l] == '#' or grid[next_r] == '#':
        return False
    elif (grid[next_l] == '.' and grid[next_r] == '.'):
        return True
    elif (can_be_moved(next_l, move, grid) and can_be_moved(next_r, move, grid)):
        return True

    return False

def try_vertical_shift(pos, move, grid):
    item = grid[pos]

    if item == '@':
        next_pos = Point(pos.x + moves[move][0], pos.y + moves[move][1])
        if grid[next_pos] == '#':
            return False
        elif grid[next_pos] == '.' or try_vertical_shift(next_pos, move, grid):
            grid[next_pos] = item
            grid[pos] = '.'
            return True
    elif item in "[]":
        if item == '[':
            l = Point(pos.x, pos.y)
            r = Point(pos.x + 1, pos.y)
        elif item == ']':
            l = Point(pos.x - 1, pos.y)
            r = Point(pos.x, pos.y)

        next_l = Point(l.x + moves[move][0], l.y + moves[move][1])
        next_r = Point(r.x + moves[move][0], r.y + moves[move][1])

        if grid[next_l] == '#' or grid[next_r] == '#':
            return False
        elif (grid[next_l] == '.' and grid[next_r] == '.'):
            grid[next_l] = '['
            grid[next_r] = ']'
            grid[l] = '.'
            grid[r] = '.'
            return True
        elif can_be_moved(next_l, move, grid) and can_be_moved(next_r, move, grid):
            try_vertical_shift(next_l, move, grid)
            try_vertical_shift(next_r, move, grid)
            grid[next_l] = '['
            grid[next_r] = ']'
            grid[l] = '.'
            grid[r] = '.'
            return True

    return False

def expand_grid(grid):
    xlate = {
        '[': ']',
        '@': '.',
        '#': '#',
        '.': '.',
    }
    grid[grid == 'O'] = '['
    ret = []
    for x in range(len(grid)):
        ret.append(grid[x])
        new_col = []
        for cell in grid[x]:
            new_col.append(xlate[cell])
        ret.append(new_col)

    return np.array(ret)

def part_two(_input):
    split = _input.index('')
    grid = np.array([list(line) for line in _input[:split]])
    grid = np.swapaxes(grid, 0, 1)
    grid = expand_grid(grid)

    tape = ''.join(_input[split:])

    start_pos = np.where(grid == '@')
    x, y = int(start_pos[0][0]), int(start_pos[1][0])
    print_state(grid)

    for move in tape:
        if move in "<>" and try_simple_shift(x, y, move, grid):
            x, y = x + moves[move][0], y + moves[move][1]
        elif move in '^v' and try_vertical_shift(Point(x, y), move, grid):
            x, y = x + moves[move][0], y + moves[move][1]

    ret = 0
    for x, y in  zip(*np.where(grid == '[')):
        ret += 100 * y + x
    
    return ret

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day15/input.txt').readlines()]

    ##print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
