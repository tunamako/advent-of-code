from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, pairwise
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
import time
YEAR = 2024
DAY = 9

def part_one(_input):
    disk_map = _input[0]
    disk = []
    for i, block in enumerate(disk_map):
        if i % 2 == 0:
            disk += int(block) * [int(i/2)]
        else:
            disk += int(block) * ['.']

    empty_blocks = list(reversed([i for i, block in enumerate(disk) if block == '.']))
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] == '.':
            continue
        else:
            j = empty_blocks.pop()
            if j >= i:
                break
            disk[j] = disk[i]
            disk[i] = '.'

    return sum(i * disk[i] for i in range(len(disk)) if disk[i] != '.')

def part_two(_input):
    disk_map = _input[0]

    disk_size = 0
    file_blocks = []
    empty_blocks = []

    for i, block in enumerate(disk_map):
        if i % 2 == 0:
            file_blocks.append({
                "pos": disk_size,
                "id": int(i/2),
                "len": int(block)
            })
            disk_size += int(block)
        else:
            empty_blocks.append({
                "pos": disk_size,
                "len": int(block)
            })
            disk_size += int(block)

    file_blocks.sort(key=lambda block: block["id"], reverse=True)
    empty_blocks.sort(key=lambda block: block["pos"])

    for file in file_blocks:
        for block in empty_blocks:
            if block["len"] < file["len"]:
                continue
            elif block["pos"] >= file["pos"]:
                break

            file["pos"] = block["pos"]

            block["len"] -= file["len"]
            block["pos"] += file["len"]

    ret = 0
    for block in file_blocks:
        ret += sum(range(block["pos"], block["pos"] + block["len"]))  * block["id"]

    return ret


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day09/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')

