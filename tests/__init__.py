from tracer.vector import Vector3


NP_LIMITS = {  # https://github.com/numpy/numpy/issues/5745
    "ADD": 4611686018427387903,
    "MUL": 3037000499,
    "DOT": 1753413056,
    "CRS": 2147483647,  # cross
    "MAG": 9223372036854775808  # magnitude
}


def _listify_vector(vector):
    if isinstance(vector, Vector3):
        return [vector.x, vector.y, vector.z]


__all__ = ["Vector3", "_listify_vector", "NP_LIMITS"]
