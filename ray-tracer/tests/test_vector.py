"""
test_vector.py

Test Vector class with a few simple test cases.
"""
# TODO test:
# __rsub__
# __truediv__
# __rtruediv__
# magnitude
# cross
# unit_vector

import pytest

from tests import Vector


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 3), 0, Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(0, 0, 0), Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(1, 2, 3), Vector(2, 4, 6)),
    (Vector(1, 2, 3), Vector(-1, -2, -3), Vector(0, 0, 0)),
    (Vector(1, 2, 3), 7, Vector(8, 9, 10)),
    (-4, Vector(1, 2, 3), Vector(-3, -2, -1))
])
def test_add(a, b, c):
    """Test __eq__, __add__, and __radd__."""
    assert a + b == c == b + a


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 3), 0, Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(0, 0, 0), Vector(1, 2, 3)),
    (Vector(1, 2, 3), Vector(-1, -2, -3), Vector(2, 4, 6)),
    (Vector(1, 2, 3), Vector(1, 2, 3), Vector(0, 0, 0))
])
def test_sub(a, b, c):
    assert a - b == c


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 3), 0, Vector(0, 0, 0)),
    (Vector(1, 2, 3), Vector(0, 0, 0), Vector(0, 0, 0)),
    (Vector(1, 2, 3), Vector(1, 2, 3), Vector(1, 4, 9)),
    (Vector(1, -2, -3), Vector(-1, -2, -3), Vector(-1, 4, 9)),
    (7, Vector(1, 2, 3), Vector(7, 14, 21)),
    (-4, Vector(1, 2, 3), Vector(-4, -8, -12))
])
def test_mul(a, b, c):
    """Test __mul__ and __rmul__."""
    assert a * b == c == b * a


@pytest.mark.parametrize("a,b", [
    (Vector(11, 2, 3), Vector(0, 22, 33)),
    (Vector(1, 0, 3), Vector(1, 0, 3)),
    (Vector(1, 2, 3), Vector(0, 0, 0))])
def test_div_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        a / b


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 3), Vector(1, 2, 3), 14),
    (Vector(1, 2, 3), Vector(0, 0, 0), 0),
    (Vector(1, 2, 3), Vector(2, 4, 1), 13)
])
def test_dot(a, b, c):
    assert a.dot(b) == c == b.dot(a)


@pytest.mark.parametrize("a,b,c", [
    (Vector(1, 2, 0), Vector(4, 5, 6), Vector(12, -6, -3)),
    (Vector(1, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1)),
    (Vector(0, 1, 0), Vector(1, 0, 0), Vector(0, 0, -1)),
    (Vector(1, -7, 1), Vector(5, 2, 4), Vector(-30, 1, 37))
])
def test_cross(a, b, c):
    assert a.cross(b) == c
