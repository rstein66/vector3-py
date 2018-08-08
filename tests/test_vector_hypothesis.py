"""
test_vector_hypothesis.py

Use Hypothesis to generate test cases for Vector3 class.
"""
# TODO test
# unit_vector

from hypothesis import given
from hypothesis.strategies import integers as ints
import numpy as np

from tests import *


ADD_LIMIT = NP_LIMITS["ADD"]
MUL_LIMIT = NP_LIMITS["MUL"]
DOT_LIMIT = NP_LIMITS["DOT"]
CRS_LIMIT = NP_LIMITS["CRS"]
MAG_LIMIT = NP_LIMITS["MAG"]


@given(x=ints(-ADD_LIMIT, ADD_LIMIT), y=ints(-ADD_LIMIT, ADD_LIMIT),
       z=ints(-ADD_LIMIT, ADD_LIMIT), a=ints(-ADD_LIMIT, ADD_LIMIT),
       b=ints(-ADD_LIMIT, ADD_LIMIT), c=ints(-ADD_LIMIT, ADD_LIMIT))
def test_add(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector3(x, y, z), Vector3(a, b, c)
    np_result = list(arr1 + arr2)
    my_result_forward = _listify_vector(vec1 + vec2)
    my_result_reverse = _listify_vector(vec2 + vec1)
    assert np_result == my_result_forward == my_result_reverse


@given(x=ints(-ADD_LIMIT, ADD_LIMIT), y=ints(-ADD_LIMIT, ADD_LIMIT),
       z=ints(-ADD_LIMIT, ADD_LIMIT), a=ints(-ADD_LIMIT, ADD_LIMIT),
       b=ints(-ADD_LIMIT, ADD_LIMIT), c=ints(-ADD_LIMIT, ADD_LIMIT))
def test_sub(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector3(x, y, z), Vector3(a, b, c)
    assert list(arr1 - arr2) == _listify_vector(vec1 - vec2)


@given(x=ints(-MUL_LIMIT, MUL_LIMIT), y=ints(-MUL_LIMIT, MUL_LIMIT),
       z=ints(-MUL_LIMIT, MUL_LIMIT), a=ints(-MUL_LIMIT, MUL_LIMIT),
       b=ints(-MUL_LIMIT, MUL_LIMIT), c=ints(-MUL_LIMIT, MUL_LIMIT))
def test_mul(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector3(x, y, z), Vector3(a, b, c)
    np_result = list(arr1 * arr2)
    my_result_forward = _listify_vector(vec1 * vec2)
    my_result_reverse = _listify_vector(vec2 * vec1)
    assert np_result == my_result_forward == my_result_reverse


@given(x=ints(-MUL_LIMIT, MUL_LIMIT), y=ints(-MUL_LIMIT, MUL_LIMIT),
       z=ints(-MUL_LIMIT, MUL_LIMIT), a=ints(-MUL_LIMIT, MUL_LIMIT),
       b=ints(-MUL_LIMIT, MUL_LIMIT), c=ints(-MUL_LIMIT, MUL_LIMIT))
def test_div(x, y, z, a, b, c):
    try:
        my_result = Vector3(x, y, z) / Vector3(a, b, c)
        np_result = np.array([x, y, z]) / np.array([a, b, c])
        assert list(np_result) == _listify_vector(my_result)
    except ZeroDivisionError:
        pass


@given(x=ints(-DOT_LIMIT, DOT_LIMIT), y=ints(-DOT_LIMIT, DOT_LIMIT),
       z=ints(-DOT_LIMIT, DOT_LIMIT), a=ints(-DOT_LIMIT, DOT_LIMIT),
       b=ints(-DOT_LIMIT, DOT_LIMIT), c=ints(-DOT_LIMIT, DOT_LIMIT))
def test_dot(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector3(x, y, z), Vector3(a, b, c)
    assert arr1.dot(arr2) == vec1.dot(vec2)


@given(x=ints(-CRS_LIMIT, CRS_LIMIT), y=ints(-CRS_LIMIT, CRS_LIMIT),
       z=ints(-CRS_LIMIT, CRS_LIMIT), a=ints(-CRS_LIMIT, CRS_LIMIT),
       b=ints(-CRS_LIMIT, CRS_LIMIT), c=ints(-CRS_LIMIT, CRS_LIMIT))
def test_cross(x, y, z, a, b, c):
    arr1, arr2 = np.array([x, y, z]), np.array([a, b, c])
    vec1, vec2 = Vector3(x, y, z), Vector3(a, b, c)
    np_result = list(np.cross(arr1, arr2))
    my_result = _listify_vector(vec1.cross(vec2))
    assert np_result == my_result


@given(x=ints(-MAG_LIMIT, MAG_LIMIT),
       y=ints(-MAG_LIMIT, MAG_LIMIT),
       z=ints(-MAG_LIMIT, MAG_LIMIT))
def test_magnitude(x, y, z):
    arr = np.array([x, y, z])
    vec = Vector3(x, y, z)
    np_result = np.linalg.norm(arr)
    my_result = vec.magnitude()
    result_avg = (np_result + my_result) / 2
    result_diff = abs(np_result - my_result)
    assert (np_result == my_result) or (result_diff / result_avg <= 0.00001)
