from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 24

def run_program(program, model_number):
    reg = {"w": 0, "x": 0, "y": 0, "z": 0}
    input_idx = 0

    for line in program:
        op = line[0]
        args = line[1:]
        if len(args) == 2 and args[1] in reg:
            args[1] = reg[args[1]]

        if op == "inp":
            reg[args[0]] = int(model_number[input_idx])
            input_idx += 1
        elif op == "add":
            reg[args[0]] = reg[args[0]] + int(args[1])
        elif op == "mul":
            reg[args[0]] = reg[args[0]] * int(args[1])
        elif op == "div":
            reg[args[0]] = int(reg[args[0]] // int(args[1]))
        elif op == "mod":
            reg[args[0]] = reg[args[0]] % int(args[1])
        elif op == "eql":
            reg[args[0]] = int(reg[args[0]] == int(args[1]))

    return int(reg['z'])

def part_one(_input):
    program = [line.split(' ') for line in _input]
    run_program(program, "11111111111111")

    for i in range(11111111111111, 99999999999999 + 1):
        result = run_program(program, str(i))
        print(i, result)
        if result == 0:
            return i

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
