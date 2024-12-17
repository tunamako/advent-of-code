from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math
from pprint import pprint
import numpy as np
import sys
from copy import deepcopy
from difflib import SequenceMatcher
YEAR = 2024
DAY = 17

class Computah:

    def __init__(self, start_state):
        self.initial_state = {
            "A": int(start_state[0].split(": ")[1]),
            "B": int(start_state[1].split(": ")[1]),
            "C": int(start_state[2].split(": ")[1]),
        }
        self.pgm = list(map(int, start_state[4].split(": ")[1].split(',')))
        self.reset()

    def reset(self):
        self.A = self.initial_state["A"]
        self.B = self.initial_state["B"]
        self.C = self.initial_state["C"]

        self.ip = 0
        self.output = []

    def run_program(self):

        while self.ip < len(self.pgm) :
            op = self.pgm[self.ip]
            operand = self.pgm[self.ip+1]

            if op == 0:
                print(self.ip, self.A, self.B, self.C, "adv " + str(self.get_combo(operand)))
                self.adv(operand)
            elif op == 1:
                print(self.ip, self.A, self.B, self.C, "bxl " + str(operand))
                self.bxl(operand)                
            elif op == 2:
                print(self.ip, self.A, self.B, self.C, "bst " + str(self.get_combo(operand)))
                self.bst(operand)                
            elif op == 3:
                print(self.ip, self.A, self.B, self.C, "jnz " + str(operand))
                self.jnz(operand)                
            elif op == 4:
                print(self.ip, self.A, self.B, self.C, "bxc " + str(operand))
                self.bxc(operand)                
            elif op == 5:
                print(self.ip, self.A, self.B, self.C, "out " + str(self.get_combo(operand)))
                self.out(operand)                
            elif op == 6:
                print(self.ip, self.A, self.B, self.C, "bdv " + str(self.get_combo(operand)))
                self.bdv(operand)                
            elif op == 7:
                print(self.ip, self.A, self.B, self.C, "cdv " + str(self.get_combo(operand)))
                self.cdv(operand)                

    def get_combo(self, value):
        if value <= 3:
            return value
        elif value == 4:
            return self.A
        elif value == 5:
            return self.B
        elif value == 6:
            return self.C
        elif value == 7:
            pass

    def adv(self, operand):
        self.A = int(self.A // math.pow(2, self.get_combo(operand)))
        self.ip += 2

    def bxl(self, operand):
        self.B = self.B ^ operand
        self.ip += 2

    def bst(self, operand):
        self.B = self.get_combo(operand) % 8
        self.ip += 2

    def jnz(self, operand):
        if self.A != 0:
            self.ip = operand
        else:
            self.ip += 2

    def bxc(self, operand):
        self.B = self.B ^ self.C
        self.ip += 2

    def out(self, operand):
        out = int(self.get_combo(operand) % 8)
        #print("Out: " + out)

        self.output.append(out)
        self.ip += 2

    def bdv(self, operand):
        self.B = int(self.A // math.pow(2, self.get_combo(operand)))
        self.ip += 2

    def cdv(self, operand):
        self.C = int(self.A // math.pow(2, self.get_combo(operand)))
        self.ip += 2


def calc_out(A):
    return ((((A % 8) ^ 5) ^ (int(A // math.pow(2, ((A % 8) ^ 5))))) ^ 6) % 8

def part_one(_input):
    A = int(_input[0].split(": ")[1])
    ret = []
    while A > 0:
        out = calc_out(A)
        ret.append(str(out))
        A = A // 8

    return ','.join(ret)

def check_item(pgm, A):
    if len(pgm) == 0:
        return A

    for i in range(A * 8, (A + 1) * 8):
        if calc_out(i) == pgm[-1]:
            if ret := check_item(pgm[:-1], i):
                return ret

def part_two(_input):
    pgm = list(map(int, _input[4].split(": ")[1].split(',')))
    return check_item(pgm, 0)



if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day17/input.txt').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
