"""
test_vector.py

Test Vector3 class with a few simple test cases.
"""
# TODO test:
# __rsub__
# __truediv__
# __rtruediv__
# unit_vector

import pytest

from tests import Vector3


@pytest.mark.parametrize("a,b,c", [
    (Vector3(1, 2, 3), 0, Vector3(1, 2, 3)),
    (Vector3(1, 2, 3), Vector3(0, 0, 0), Vector3(1, 2, 3)),
    (Vector3(1, 2, 3), Vector3(1, 2, 3), Vector3(2, 4, 6)),
    (Vector3(1, 2, 3), Vector3(-1, -2, -3), Vector3(0, 0, 0)),
    (Vector3(1, 2, 3), 7, Vector3(8, 9, 10)),
    (-4, Vector3(1, 2, 3), Vector3(-3, -2, -1))
])
def test_add(a, b, c):
    """Test __eq__, __add__, and __radd__."""
    assert a + b == c == b + a


@pytest.mark.parametrize("a,b,c", [
    (Vector3(1, 2, 3), 0, Vector3(1, 2, 3)),
    (Vector3(1, 2, 3), Vector3(0, 0, 0), Vector3(1, 2, 3)),
    (Vector3(1, 2, 3), Vector3(-1, -2, -3), Vector3(2, 4, 6)),
    (Vector3(1, 2, 3), Vector3(1, 2, 3), Vector3(0, 0, 0))
])
def test_sub(a, b, c):
    assert a - b == c


@pytest.mark.parametrize("a,b,c", [
    (Vector3(1, 2, 3), 0, Vector3(0, 0, 0)),
    (Vector3(1, 2, 3), Vector3(0, 0, 0), Vector3(0, 0, 0)),
    (Vector3(1, 2, 3), Vector3(1, 2, 3), Vector3(1, 4, 9)),
    (Vector3(1, -2, -3), Vector3(-1, -2, -3), Vector3(-1, 4, 9)),
    (7, Vector3(1, 2, 3), Vector3(7, 14, 21)),
    (-4, Vector3(1, 2, 3), Vector3(-4, -8, -12))
])
def test_mul(a, b, c):
    """Test __mul__ and __rmul__."""
    assert a * b == c == b * a


@pytest.mark.parametrize("a,b", [
    (Vector3(11, 2, 3), Vector3(0, 22, 33)),
    (Vector3(1, 0, 3), Vector3(1, 0, 3)),
    (Vector3(1, 2, 3), Vector3(0, 0, 0))])
def test_div_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        a / b


@pytest.mark.parametrize("a,b,c", [
    (Vector3(1, 2, 3), Vector3(1, 2, 3), 14),
    (Vector3(1, 2, 3), Vector3(0, 0, 0), 0),
    (Vector3(1, 2, 3), Vector3(2, 4, 1), 13)
])
def test_dot(a, b, c):
    assert a.dot(b) == c == b.dot(a)


@pytest.mark.parametrize("a,b,c", [
    (Vector3(1, 2, 0), Vector3(4, 5, 6), Vector3(12, -6, -3)),
    (Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)),
    (Vector3(0, 1, 0), Vector3(1, 0, 0), Vector3(0, 0, -1)),
    (Vector3(1, -7, 1), Vector3(5, 2, 4), Vector3(-30, 1, 37))
])
def test_cross(a, b, c):
    assert a.cross(b) == c


@pytest.mark.parametrize("a,b", [
    (Vector3(0, 3, 4), 5),
    (Vector3(0, -3, 4), 5),
    (Vector3(0, -3, -4), 5),
    (Vector3(1, 2, 3), 3.74166),
    (Vector3(2, 3, 5), 6.16441)
])
def test_magnitude(a, b):
    assert round(a.magnitude(), ndigits=5) == b
