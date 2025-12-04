import numpy as np
import pytest

from advent_lib.grid_helpers import get_neighbors, parse_text_to_ndarray, Point

def test_get_neighbors_all_directions():
    grid = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])
    p = Point(1, 1)
    neighbors = get_neighbors(grid, p)
    expected_points = [
        Point(1, 0), Point(2, 1), Point(1, 2), Point(0, 1),
        Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)
    ]
    assert set(neighbors) == set(expected_points)

def test_get_neighbors_cardinal_only():
    grid = np.zeros((3, 3), dtype=int)
    p = Point(1, 1)
    neighbors = get_neighbors(grid, p, cardinal_only=True)
    expected_points = [Point(1, 0), Point(2, 1), Point(1, 2), Point(0, 1)]
    assert set(neighbors) == set(expected_points)

def test_get_neighbors_with_value():
    grid = np.array([
        [0, 2, 0],
        [2, 1, 2],
        [0, 2, 0]
    ])
    p = Point(1, 1)
    neighbors = get_neighbors(grid, p, value=2)
    expected_points = [
        Point(2, 1), Point(1, 0), Point(1, 2), Point(0, 1),
        Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)
    ]
    # Only points where grid[n] == 2
    expected_points = [pt for pt in expected_points if grid[pt.x, pt.y] == 2]
    assert set(neighbors) == set(expected_points)

def test_get_neighbors_with_value_cardinal_only():
    grid = np.array([
        [0, 2, 0],
        [2, 1, 2],
        [0, 2, 0]
    ])
    p = Point(1, 1)
    neighbors = get_neighbors(grid, p, value=2, cardinal_only=True)
    expected_points = [Point(2, 1), Point(1, 0), Point(1, 2), Point(0, 1)]
    expected_points = [pt for pt in expected_points if grid[pt.x, pt.y] == 2]
    assert set(neighbors) == set(expected_points)

def test_get_neighbors_edge_point():
    grid = np.zeros((3, 3), dtype=int)
    p = Point(0, 0)
    neighbors = get_neighbors(grid, p)
    expected_points = [Point(1, 0), Point(0, 1), Point(1, 1)]
    assert set(neighbors) == set(expected_points)

def test_get_neighbors_out_of_bounds():
    grid = np.zeros((3, 3), dtype=int)
    p = Point(-1, -1)
    neighbors = get_neighbors(grid, p)
    assert neighbors == []

def test_get_neighbors_value_none_behavior():
    grid = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    p = Point(1, 1)
    # value=None, so all neighbors should be included
    neighbors = get_neighbors(grid, p, value=None)
    expected_points = [
        Point(1, 0), Point(2, 1), Point(1, 2), Point(0, 1),
        Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)
    ]
    assert set(neighbors) == set(expected_points)