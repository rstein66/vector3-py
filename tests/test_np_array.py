"""
test_np_array.py

Ensure min & max values used by hypothesis.strategies.integers
in test_vector_hypothesis.py works for instances of numpy.array

Reference: https://github.com/numpy/numpy/issues/5745
"""

import numpy as np
import pytest

from tests import *


ADD_LIMIT = NP_LIMITS["ADD"]
MUL_LIMIT = NP_LIMITS["MUL"]
DOT_LIMIT = NP_LIMITS["DOT"]
CRS_LIMIT = NP_LIMITS["CRS"]
MAG_LIMIT = NP_LIMITS["MAG"]


def test_add_limit_pass():
    for v in [-ADD_LIMIT, ADD_LIMIT]:
        my_result = _listify_vector(Vector3(v, v, v) + Vector3(v, v, v))
        np_result = list(np.array([v, v, v]) + np.array([v, v, v]))
        assert my_result == np_result


def test_add_limit_fail():
    for v in [-ADD_LIMIT - 2, ADD_LIMIT + 1]:
        my_result = _listify_vector(Vector3(v, v, v) + Vector3(v, v, v))
        np_result = list(np.array([v, v, v]) + np.array([v, v, v]))
        assert my_result != np_result


def test_mul_limit_pass():
    for v in [-MUL_LIMIT, MUL_LIMIT]:
        my_result = _listify_vector(Vector3(v, v, v) * (Vector3(v, v, v)))
        np_result = list(np.array([v, v, v]) * np.array([v, v, v]))
        assert my_result == np_result


def test_mul_limit_fail():
    for v in [-MUL_LIMIT - 1, MUL_LIMIT + 1]:
        my_result = _listify_vector(Vector3(v, v, v) * (Vector3(v, v, v)))
        np_result = list(np.array([v, v, v]) * np.array([v, v, v]))
        assert my_result != np_result


def test_dot_limit_pass():
    for v in [-DOT_LIMIT, DOT_LIMIT]:
        my_result = Vector3(v, v, v).dot(Vector3(v, v, v))
        np_result = (np.array([v, v, v])).dot(np.array([v, v, v]))
        assert my_result == np_result


def test_dot_limit_fail():
    for v in [-DOT_LIMIT - 1, DOT_LIMIT + 1]:
        my_result = Vector3(v, v, v).dot(Vector3(v, v, v))
        np_result = (np.array([v, v, v])).dot(np.array([v, v, v]))
        assert my_result != np_result


def test_crs_limit_pass():
    n = CRS_LIMIT
    vec1, vec2 = Vector3(0, n, -n), Vector3(0, n, n)
    arr1, arr2 = np.array([0, n, -n]), np.array([0, n, n])
    my_result = _listify_vector(vec1.cross(vec2))
    np_result = list(np.cross(arr1, arr2))
    assert my_result == np_result


def test_crs_limit_fail():
    n = CRS_LIMIT + 1
    vec1, vec2 = Vector3(0, n, -n), Vector3(0, n, n)
    arr1, arr2 = np.array([0, n, -n]), np.array([0, n, n])
    my_result = _listify_vector(vec1.cross(vec2))
    np_result = list(np.cross(arr1, arr2))
    assert my_result != np_result


def test_mag_limit_pass():
    for n in [-MAG_LIMIT, MAG_LIMIT]:
        arr = np.array([0, 0, n])
        vec = Vector3(0, 0, n)
        np_result = np.linalg.norm(arr)
        my_result = vec.magnitude()
        result_avg = (np_result + my_result) / 2
        result_diff = abs(np_result - my_result)
        assert (np_result == my_result) or (result_diff / result_avg <= 0.00001)


def test_mag_limit_fail():
    with pytest.raises(AttributeError) as excinfo:
        for n in [-MAG_LIMIT - 1, MAG_LIMIT + 1]:
            arr = np.array([0, 0, n])
            _ = np.linalg.norm(arr)
    assert "'int' object has no attribute 'sqrt'" in str(excinfo.value)
