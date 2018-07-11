"""
test_vector_hypothesis.py

Use Hypothesis to generate test cases for Vector class.
"""
# TODO test
# magnitude
# cross
# unit_vector

from hypothesis import given
from hypothesis.strategies import integers as ints
import numpy as np

from tests import *


ADD_LIMIT = NP_LIMITS["ADD"]
MUL_LIMIT = NP_LIMITS["MUL"]
DOT_LIMIT = NP_LIMITS["DOT"]


@given(x=ints(-ADD_LIMIT, ADD_LIMIT), y=ints(-ADD_LIMIT, ADD_LIMIT),
       z=ints(-ADD_LIMIT, ADD_LIMIT), a=ints(-ADD_LIMIT, ADD_LIMIT),
       b=ints(-ADD_LIMIT, ADD_LIMIT), c=ints(-ADD_LIMIT, ADD_LIMIT))
def test_add(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector(x, y, z), Vector(a, b, c)
    np_result = list(arr1 + arr2)
    my_result_forward = _listify_vector(vec1 + vec2)
    my_result_reverse = _listify_vector(vec2 + vec1)
    assert np_result == my_result_forward == my_result_reverse


@given(x=ints(-ADD_LIMIT, ADD_LIMIT), y=ints(-ADD_LIMIT, ADD_LIMIT),
       z=ints(-ADD_LIMIT, ADD_LIMIT), a=ints(-ADD_LIMIT, ADD_LIMIT),
       b=ints(-ADD_LIMIT, ADD_LIMIT), c=ints(-ADD_LIMIT, ADD_LIMIT))
def test_sub(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector(x, y, z), Vector(a, b, c)
    assert list(arr1 - arr2) == _listify_vector(vec1 - vec2)


@given(x=ints(-MUL_LIMIT, MUL_LIMIT), y=ints(-MUL_LIMIT, MUL_LIMIT),
       z=ints(-MUL_LIMIT, MUL_LIMIT), a=ints(-MUL_LIMIT, MUL_LIMIT),
       b=ints(-MUL_LIMIT, MUL_LIMIT), c=ints(-MUL_LIMIT, MUL_LIMIT))
def test_mul(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector(x, y, z), Vector(a, b, c)
    np_result = list(arr1 * arr2)
    my_result_forward = _listify_vector(vec1 * vec2)
    my_result_reverse = _listify_vector(vec2 * vec1)
    assert np_result == my_result_forward == my_result_reverse


@given(x=ints(-MUL_LIMIT, MUL_LIMIT), y=ints(-MUL_LIMIT, MUL_LIMIT),
       z=ints(-MUL_LIMIT, MUL_LIMIT), a=ints(-MUL_LIMIT, MUL_LIMIT),
       b=ints(-MUL_LIMIT, MUL_LIMIT), c=ints(-MUL_LIMIT, MUL_LIMIT))
def test_div(x, y, z, a, b, c):
    try:
        my_result = Vector(x, y, z) / Vector(a, b, c)
        np_result = np.array([x, y, z]) / np.array([a, b, c])
        assert list(np_result) == _listify_vector(my_result)
    except ZeroDivisionError:
        pass


@given(x=ints(-DOT_LIMIT, DOT_LIMIT), y=ints(-DOT_LIMIT, DOT_LIMIT),
       z=ints(-DOT_LIMIT, DOT_LIMIT), a=ints(-DOT_LIMIT, DOT_LIMIT),
       b=ints(-DOT_LIMIT, DOT_LIMIT), c=ints(-DOT_LIMIT, DOT_LIMIT))
def test_dot(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector(x, y, z), Vector(a, b, c)
    assert arr1.dot(arr2) == vec1.dot(vec2)
