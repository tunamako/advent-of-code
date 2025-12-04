from collections import namedtuple
import pytest

from advent_lib.advent_machine import AdventMachine, Paintbot

Point = namedtuple("Point", ['x', 'y'])

@pytest.fixture
def test_machine():
    return AdventMachine(return_output=True)

def _test_data_helper(test_machine, tape, data):
    for _input, expected in data:
        test_machine.reinit(tape, _input)
        assert test_machine.execute() == expected

def test_PosEq(test_machine):
    tape = [3,9,8,9,10,9,4,9,99,-1,8]
    data = [(8, [1]), (9, [0]), (7, [0])]
    _test_data_helper(test_machine, tape, data)

def test_PosLess(test_machine):
    tape = [3,9,7,9,10,9,4,9,99,-1,8]
    data = [(2, [1]), (10, [0]), (8, [0])]
    _test_data_helper(test_machine, tape, data)

def test_ImEq(test_machine):
    tape = [3,3,1108,-1,8,3,4,3,99]
    data = [(8, [1]), (9, [0]), (7, [0])]
    _test_data_helper(test_machine, tape, data)

def test_ImLess(test_machine):
    tape = [3,3,1107,-1,8,3,4,3,99]
    data = [(7, [1]), (8, [0]), (9, [0])]
    _test_data_helper(test_machine, tape, data)

def test_JMP(test_machine):
    tape = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    data = [(0, [0]), (1, [1]), (2, [1])]
    _test_data_helper(test_machine, tape, data)

    tape = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    data = [(0, [0]), (1, [1]), (2, [1])]
    _test_data_helper(test_machine, tape, data)

def test_All(test_machine):
    tape = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    data = [(7, [999]), (8, [1000]), (9, [1001])]
    _test_data_helper(test_machine, tape, data)

def test_Quine(test_machine):
    tape = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    test_machine.reinit(tape, 1)
    output = test_machine.execute()
    assert output == tape

def test_BigMul(test_machine):
    tape = [1102,34915192,34915192,7,4,7,99,0]
    test_machine.reinit(tape, 0)
    output = test_machine.execute()[0]
    assert len(str(output)) == 16

def test_BigOut(test_machine):
    tape = [104,1125899906842624,99]
    test_machine.reinit(tape, 0)
    output = test_machine.execute()[0]
    assert output == 1125899906842624

@pytest.fixture
def bot():
    return Paintbot([99])

def test_Construction(bot):
    assert bot.pos == Point(0,0)
    assert bot.pos.y == 0
    assert bot.facing == 'N'
    assert bot.panel == 0
    assert len(bot.grid) == 0

def test_Paint(bot):
    assert len(bot.grid) == 0

    bot.paint(1)
    assert len(bot.grid) == 1
    assert bot.pos == Point(0,0)
    assert bot.grid[Point(0,0)] == 1
    assert bot.panel == 1

    bot.pos = Point(1,1)
    bot.paint(0)
    assert len(bot.grid) == 2
    assert bot.pos == Point(1,1)
    assert bot.grid[Point(1,1)] == 0
    assert bot.panel == 0

    bot.pos = Point(0,0)
    bot.paint(0)
    assert len(bot.grid) == 2
    assert bot.pos == Point(0,0)
    assert bot.grid[Point(0,0)] == 0
    assert bot.panel == 0

def test_Step(bot):
    bot.facing = 'N'
    bot.step()
    assert bot.pos == Point(0,1)
    bot.step(4)
    assert bot.pos == Point(0,5)

    bot.facing = 'S'
    bot.step()
    assert bot.pos == Point(0,4)
    bot.step(2)
    assert bot.pos == Point(0,2)

    bot.facing = 'E'
    bot.step()
    assert bot.pos == Point(1,2)
    bot.step(2)
    assert bot.pos == Point(3,2)

    bot.facing = 'W'
    bot.step()
    assert bot.pos == Point(2,2)
    bot.step(4)
    assert bot.pos == Point(-2,2)

def test_Turn(bot):
    bot.facing = 'N'
    bot.turn(0)
    assert bot.facing == 'W'
    bot.turn(0)
    assert bot.facing == 'S'
    bot.turn(0)
    assert bot.facing == 'E'
    bot.turn(0)
    assert bot.facing == 'N'

    bot.facing = 'N'
    bot.turn(1)
    assert bot.facing == 'E'
    bot.turn(1)
    assert bot.facing == 'S'
    bot.turn(1)
    assert bot.facing == 'W'
    bot.turn(1)
    assert bot.facing == 'N'

    bot.facing = 'S'
    bot.turn(1)
    assert bot.facing == 'W'
    bot.turn(0)
    assert bot.facing == 'S'
    bot.turn(1)
    assert bot.facing == 'W'
    bot.turn(0)
    assert bot.facing == 'S'
