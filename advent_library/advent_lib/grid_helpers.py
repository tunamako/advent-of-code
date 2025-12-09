
from collections import namedtuple, defaultdict
import os

import numpy as np
from scipy.spatial.distance import cdist
import math
from functools import cache
BasePoint = namedtuple("Point", ['x', 'y']) 
BasePoint3D = namedtuple("Point", ['x', 'y', 'z']) 

class Point(BasePoint):

    def __add__(self, p: Point) -> Point:
        if not isinstance(p, Point):
            raise ValueError(f"Expected righthand operand of type 'Point', got '{type(p)}'")

        return Point(self.x + p.x, self.y + p.y)

    def isin(self, grid: np.ndarray) -> bool:
        return 0 <= self.x < len(grid) and 0 <= self.y < len(grid[0])

class Point3D(BasePoint3D):

    def __add__(self, p: Point3D) -> Point3D:
        if not isinstance(p, Point3D):
            raise ValueError(f"Expected righthand operand of type 'Point3D', got '{type(p)}'")

        return Point3D(self.x + p.x, self.y + p.y, self.z + p.z)

    def isin(self, grid: np.ndarray) -> bool:
        return 0 <= self.x < len(grid) and 0 <= self.y < len(grid[0]) and 0 <= self.z < len(grid[0][0]) 

    @cache
    def distance(self, p):
        xpart = math.pow(abs(self.x - p.x), 2)
        ypart = math.pow(abs(self.y - p.y), 2)
        zpart = math.pow(abs(self.z - p.z), 2)

        return math.sqrt(xpart + ypart + zpart)


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