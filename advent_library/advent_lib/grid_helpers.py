
from collections import namedtuple, defaultdict
import os

import numpy as np

BasePoint = namedtuple("Point", ['x', 'y']) 

class Point(BasePoint):

    def __add__(self, p: Point) -> Point:
        if not isinstance(p, Point):
            raise ValueError(f"Expected righthand operand of type 'Point', got '{type(p)}'")

        return Point(self.x + p.x, self.y + p.y)

    def isin(self, grid: np.ndarray) -> bool:
        return 0 <= self.x < len(grid) and 0 <= self.y < len(grid[0])

DIRECTIONS = [
    Point(0, -1), # N
    Point(1, 0),  # E
    Point(0, 1),  # S
    Point(-1, 0), # W
    Point(-1,-1), # NW
    Point(1, -1), # NE
    Point(1, 1),  # SE
    Point(-1, 1), # SW
]

CARDINAL_DIRECTIONS = DIRECTIONS[:4]

def get_neighbors(grid: np.ndarray, p: Point, value=None, cardinal_only=False) -> list[Point]:
    neighbors = list()
    directions = CARDINAL_DIRECTIONS if cardinal_only else DIRECTIONS

    if not p.isin(grid):
        return []

    for d in directions:
        n = p + d
        if n.isin(grid):
            if (value is None) ^ (grid[n] == value):
                neighbors.append(n)

    return neighbors

def parse_text_to_ndarray(_input: list) -> np.ndarray:
    grid = np.array([list(line) for line in _input])
    grid = np.swapaxes(grid, 0, 1)

    return grid

def print_grid(grid: np.ndarray, preclear=False) -> None:
    if preclear:
        os.system('cls' if os.name == 'nt' else 'clear')
    out = ""
    for x in np.swapaxes(grid, 0, 1):
        out += ''.join(x) + "\n"

    print(out)