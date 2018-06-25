"""
test_vector.py

WIP
"""

import pytest
# import hypothesis
# import numpy as np

from tracer.vector import Vector


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 3), 0, Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(0, 0, 0), Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(1, 2, 3), Vector(2, 4, 6)),
    (Vector(1, 2, 3), Vector(-1, -2, -3), Vector(0, 0, 0)),
    (Vector(1, 2, 3), 7, Vector(8, 9, 10)),
    (7, Vector(1, 2, 3), Vector(8, 9, 10)),
    (-4, Vector(1, 2, 3), Vector(-3, -2, -1))
])
def test_add(a, b, c):
    """Test __eq__, __add__, and __radd__."""
    assert c == a + b


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 3), 0, Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(0, 0, 0), Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(-1, -2, -3), Vector(2, 4, 6)),
    (Vector(1, 2, 3), Vector(1, 2, 3), Vector(0, 0, 0))
])
def test_sub(a, b, c):
    assert c == a - b

# def test_rsub(a, b, c):

# def test_mul(a, b, c):
#    """Test __mul__ and __rmul__."""

# __truediv__
# __rtruediv__
# magnitude
# dot
# cross
# unit_vector
