from collections import defaultdict, namedtuple
import os
import sys
import unittest
import ast

from day18 import Pair, Number


class TestPair(unittest.TestCase):

    def test_Construction(self):
        pair_string = "[1,2]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

        pair_string = "[[1,2],3]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

        pair_string = "[9,[8,7]]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

        pair_string = "[[1,9],[8,5]]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

        pair_string = "[[[[1,2],[3,4]],[[5,6],[7,8]]],9]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

        pair_string = "[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

        pair_string = "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
        pair = Pair(ast.literal_eval(pair_string))
        self.assertEqual(str(pair), pair_string)

    def test_Addition(self):
        pair_1 = Pair([1,2])
        pair_2 = Pair([[3,4],5])
        pair_1 += pair_2
        self.assertEqual(str(pair_1), "[[1,2],[[3,4],5]]")

        pair_1 = Pair([[[[4,3],4],4],[7,[[8,4],9]]])
        pair_2 = Pair([1,1])
        pair_1 += pair_2
        self.assertEqual(str(pair_1), "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")

    def test_Explosion(self):

        pair = Pair([[[[[9,8],1],2],3],4])
        pair.explode()
        self.assertEqual(str(pair), "[[[[0,9],2],3],4]")

        pair = Pair([7,[6,[5,[4,[3,2]]]]])
        pair.explode()
        self.assertEqual(str(pair), "[7,[6,[5,[7,0]]]]")

        pair = Pair([[6,[5,[4,[3,2]]]],1])
        pair.explode()
        self.assertEqual(str(pair), "[[6,[5,[7,0]]],3]")

        pair = Pair([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
        pair.explode()
        self.assertEqual(str(pair), "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

    def test_Splitting(self):
        pair = Pair([[[[0,7],4],[15,[0,13]]],[1,1]])
        pair.split()
        self.assertEqual(str(pair), "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")

        pair = Pair([[[[0,7],4],[[7,8],[0,13]]],[1,1]])
        pair.split()
        self.assertEqual(str(pair), "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")

    def test_Reduction(self):
        pair = Pair([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
        pair.reduce()

        self.assertEqual(str(pair), "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

        pair_list = [
            [1,1],
            [2,2],
            [3,3],
            [4,4]
        ]
        pair = Pair(pair_list[0])
        for next_pair in pair_list[1:]:
            pair += Pair(next_pair)
            pair.reduce()
        self.assertEqual(str(pair), "[[[[1,1],[2,2]],[3,3]],[4,4]]")

        pair_list = [
            [1,1],
            [2,2],
            [3,3],
            [4,4],
            [5,5]
        ]
        pair = Pair(pair_list[0])
        for next_pair in pair_list[1:]:
            pair += Pair(next_pair)
            pair.reduce()
        self.assertEqual(str(pair), "[[[[3,0],[5,3]],[4,4]],[5,5]]")

        pair_list = [
            [1,1],
            [2,2],
            [3,3],
            [4,4],
            [5,5],
            [6,6]
        ]
        pair = Pair(pair_list[0])
        for next_pair in pair_list[1:]:
            pair += Pair(next_pair)
            pair.reduce()
        self.assertEqual(str(pair), "[[[[5,0],[7,4]],[5,5]],[6,6]]")

        pair_list = [
            [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
            [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
            [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
            [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
            [7,[5,[[3,8],[1,4]]]],
            [[2,[2,2]],[8,[8,1]]],
            [2,9],
            [1,[[[9,3],9],[[9,0],[0,7]]]],
            [[[5,[7,4]],7],1],
            [[[[4,2],2],6],[8,7]]
        ]
        pair = Pair(pair_list[0])
        for next_pair in pair_list[1:]:
            pair += Pair(next_pair)
            pair.reduce()
            print(pair)
        self.assertEqual(str(pair), "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

    def test_Magnitude(self):
        pair = Pair([9,1])
        self.assertEqual(pair.magnitude(), 29)

        pair = Pair([1, 9])
        self.assertEqual(pair.magnitude(), 21)

        pair = Pair([[9,1],[1,9]])
        self.assertEqual(pair.magnitude(), 129)

        pair = Pair([[1,2],[[3,4],5]])
        self.assertEqual(pair.magnitude(), 143)

        pair = Pair([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
        self.assertEqual(pair.magnitude(), 1384)

        pair = Pair([[[[1,1],[2,2]],[3,3]],[4,4]])
        self.assertEqual(pair.magnitude(), 445)

        pair = Pair([[[[3,0],[5,3]],[4,4]],[5,5]])
        self.assertEqual(pair.magnitude(), 791)

        pair = Pair([[[[5,0],[7,4]],[5,5]],[6,6]])
        self.assertEqual(pair.magnitude(), 1137)

        pair = Pair([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
        self.assertEqual(pair.magnitude(), 3488)


if __name__ == "__main__":
    unittest.main(buffer=True)