"""Test codes"""
from src.math_operations import add, sub


def test_add():
    """Creating test for mat operation module add"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-2, 3) == 1


def test_substract():
    """Creating test for mat operation module sub"""
    assert sub(2, 3) == -1
    assert sub(-1, 1) == -2
    assert sub(-2, 3) == -5
