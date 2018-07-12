from tracer.vector import Vector


NP_LIMITS = {  # https://github.com/numpy/numpy/issues/5745
    "ADD": 4611686018427387903,
    "MUL": 3037000499,
    "DOT": 1753413056,
    "CRS": 2147483647  # cross
}


def _listify_vector(vector):
    if isinstance(vector, Vector):
        return [vector.x, vector.y, vector.z]


__all__ = ["Vector", "_listify_vector", "NP_LIMITS"]
