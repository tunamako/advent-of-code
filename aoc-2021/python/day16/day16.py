from aocd.models import Puzzle

import cProfile
from collections import defaultdict, namedtuple, Counter, deque
from itertools import permutations, combinations, chain
import re
import math


YEAR = 2021
DAY = 16


class Packet(object):

    def __init__(self, bits):
        self.version = int(bits[:3], 2)
        self.type_id = int(bits[3:6], 2)
        self.packet_data = bits[6:]

    def version_sum(self):
        raise NotImplementedError()

    def evaluate(self):
        raise NotImplementedError()

class LiteralPacket(Packet):
    
    def __init__(self, bits):
        super().__init__(bits)
        number = ""
        i = 0
        while True:
            number += self.packet_data[i+1:i+5]
            if self.packet_data[i] == "0":
                break

            i += 5

        self.size = 6 + i + 5
        self.value = int(number, 2)

    def version_sum(self):
        return self.version

    def evaluate(self):
        return self.value

class OperatorPacket(Packet):

    def __init__(self, bits):
        super().__init__(bits)
        self.sub_packets = []

        length_id = self.packet_data[0]

        if length_id == '0':
            # Type 0
            length = int(self.packet_data[1:16], 2)
            self.size = 22 + length

            i = 16
            while i < length + 16:
                sub_packet = PacketFactory(self.packet_data[i:])
                self.sub_packets.append(sub_packet)
                i += sub_packet.size
        else:
            # Type 1
            packet_count = int(self.packet_data[1:12], 2)
            i = 12
            for p in range(packet_count):
                sub_packet = PacketFactory(self.packet_data[i:])
                self.sub_packets.append(sub_packet)
                i += sub_packet.size

            self.size = 18 + sum([p.size for p in self.sub_packets])

    def version_sum(self):
        return self.version + sum([p.version_sum() for p in self.sub_packets])

class SumPacket(OperatorPacket):

    def evaluate(self):
        return sum([p.evaluate() for p in self.sub_packets])

class ProductPacket(OperatorPacket):

    def evaluate(self):
        return math.prod([p.evaluate() for p in self.sub_packets])

class MinPacket(OperatorPacket):

    def evaluate(self):
        return min([p.evaluate() for p in self.sub_packets])

class MaxPacket(OperatorPacket):

    def evaluate(self):
        return max([p.evaluate() for p in self.sub_packets])

class GreaterThanPacket(OperatorPacket):

    def evaluate(self):
        return int(self.sub_packets[0].evaluate() > self.sub_packets[1].evaluate())

class LessThanPacket(OperatorPacket):

    def evaluate(self):
        return int(self.sub_packets[0].evaluate() < self.sub_packets[1].evaluate())

class EqualToPacket(OperatorPacket):

    def evaluate(self):
        return int(self.sub_packets[0].evaluate() == self.sub_packets[1].evaluate())


def PacketFactory(packet):
    type_id = int(packet[3:6], 2)

    packet_types = [
        SumPacket,
        ProductPacket,
        MinPacket,
        MaxPacket,
        LiteralPacket,
        GreaterThanPacket,
        LessThanPacket,
        EqualToPacket
    ]
    return packet_types[type_id](packet)

def part_one(_input):
    size = len(_input) * 4
    _input = bin(int(_input, 16))[2:].zfill(size)

    return PacketFactory(_input).version_sum()

def part_two(_input):
    size = len(_input) * 4
    _input = bin(int(_input, 16))[2:].zfill(size)

    return PacketFactory(_input).evaluate() 


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    _input = puzzle.input_data.split('\n')[0]
    #_input = open('input').readlines()[0]

    print(part_one(_input))
    print(part_two(_input))

    #cProfile.run('print(part_one(_input))')
    #cProfile.run('print(part_two(_input))')
