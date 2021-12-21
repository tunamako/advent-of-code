from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain, cycle, product
import re
import math
from pprint import *
from copy import deepcopy

YEAR = 2021
DAY = 21


def part_one(_input):
    players = [int(line.split(': ')[-1]) for line in _input]
    scores = [0, 0]
    die = cycle([i for i in range(1, 101)])

    cur = None
    rollcount = 0
    while max(scores) < 1000:
        cur = 1 if cur == 0 else 0
        res = next(die) + next(die) + next(die)
        rollcount += 3
        players[cur] += res
        players[cur] = ((players[cur] - 1) % 10) + 1
        scores[cur] += players[cur]


    return rollcount * min(scores)

dice_outcomes = [*product([1, 2, 3], repeat = 3)]



def play_game(players, scores=[0,0], cur=None, seen_states=dict()):
    if max(scores) >= 21:
        winner = max(scores)
        if winner == scores[0]:
            return [1, 0]
        else:
            return [0, 1]

    sub_wins = [0, 0]
    cur = 1 if cur == 0 else 0

    state = (players[0], players[1], scores[0], scores[1], cur)
    if state in seen_states:
        return seen_states[state]

    for roll in dice_outcomes:
        # cache game state
        res = sum(roll)
        sub_players = deepcopy(players)
        sub_scores = deepcopy(scores)

        sub_players[cur] += res
        sub_players[cur] = ((sub_players[cur] - 1) % 10) + 1
        sub_scores[cur] += sub_players[cur]

        outcomes = play_game(sub_players, sub_scores, cur, seen_states)
        sub_wins[0] += outcomes[0]
        sub_wins[1] += outcomes[1]

    seen_states[state] = sub_wins
    return sub_wins


def part_two(_input):
    players = [int(line.split(': ')[-1]) for line in _input]
    return max(play_game(players))

if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')
    #_input = [line[:-1] for line in open('input').readlines()]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
