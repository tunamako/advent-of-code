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

YEAR = 2024
DAY = 22

def mix(n, value):
    return n ^ value

def prune(n):
    return n % 16777216

memo = dict()

def generate_secret_number(secret):
    if secret in memo:
        return memo[secret]
    n = prune(mix(secret, secret * 64))
    n = prune(mix(n, n // 32))
    n = prune(mix(n, n * 2048))

    memo[secret] = n
    return n

def part_one(_input):
    ret = 0
    for secret in _input:
        secret = int(secret)
        for i in range(2000):
            secret = generate_secret_number(secret)
        
        ret += secret

    return ret

def get_price(n):
    return int(str(n)[-1])

def get_sequence_value(seq, all_sequences):
    ret = 0
    for sequences in all_sequences:
        if seq in sequences:
            ret += sequences[seq]

    return ret

def part_two(_input):
    all_sequences = []
    all_sequences_for_real = set()
    for buyer in _input:
        secret = int(buyer)
        price_list = [(secret, get_price(secret), None)]
        window = []
        sequences = dict()

        for i in range(2000):
            secret = generate_secret_number(secret)
            price = get_price(secret)
            price_change = price - price_list[-1][1]
            price_list.append((secret, price, price_change))

            window.append(price_change)
            
            if len(window) == 4:
                if tuple(window) not in sequences:
                    sequences[tuple(window)] = price
                all_sequences_for_real.add(tuple(window))
                del window[0]


        all_sequences.append(sequences)

    max_bananas = 0
    for seq in all_sequences_for_real:
        max_bananas = max(max_bananas, get_sequence_value(seq, all_sequences))

    return max_bananas



if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('aoc-2024/day22/input.txt').readlines()]
    #print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
