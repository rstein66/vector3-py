# vector.py

from math import sqrt


class Vector3(object):
    """
    3-D vector implementation.
    Purpose: Provide
    * Core functionality to ray tracing implementation.
    * Examples of using special methods & overriding class attributes
    (which is why packages such as `numpy` or `attrs` are not used).
    ---
    NOTE: Implementation prioritizes readability/simplicity over efficiency.
    Strategies for incremental performance improvements include:
      *  Define the `__slots__` class attribute.
      *  Use the dot operator less frequently.
      *  Support multiprocessing.
    Dramatic performance improvement:
      *  Run using PyPy, instead of CPython (since PyPy implements Python 3.5.3,
         make minor changes like using string formatting in place of f-strings).
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):  # for debugging
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __str__(self):  # for printing
        return f"{self.x}, {self.y}, {self.z}"

    def __eq__(self, other):
        """Overload equality operator."""
        if not isinstance(other, Vector3):
            return False
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __add__(self, other):
        """Overload addition operator."""
        if isinstance(other, Vector3):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
        else:
            x = self.x + other
            y = self.y + other
            z = self.z + other
        return Vector3(x, y, z)

    # Support "reverse[d]" addition.
    # Aliasing (w/c?) works because addition is commutative.
    # i.e., a + b == b + a
    __radd__ = __add__

    def __sub__(self, other):
        """Overload subtraction operator."""
        if isinstance(other, Vector3):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
        else:
            x = self.x - other
            y = self.y - other
            z = self.z - other
        return Vector3(x, y, z)

    def __rsub__(self, other):
        """Reversed subtraction. Subtraction is noncommutative."""
        if isinstance(other, Vector3):
            x = other.x - self.x
            y = other.y - self.y
            z = other.z - self.z
        else:
            x = other - self.x
            y = other - self.y
            z = other - self.z
        return Vector3(x, y, z)

    def __mul__(self, other):
        """Overload multiplication operator."""
        if isinstance(other, Vector3):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
        else:
            x = self.x * other
            y = self.y * other
            z = self.z * other
        return Vector3(x, y, z)

    __rmul__ = __mul__  # "Reverse[d]" multiplication

    def __truediv__(self, other):
        """Overload division operator."""
        if isinstance(other, Vector3):
            x = self.x / other.x
            y = self.y / other.y
            z = self.z / other.z
        else:
            x = self.x / other
            y = self.y / other
            z = self.z / other
        return Vector3(x, y, z)

    def __rtruediv__(self, other):
        """Reversed division. Division is noncommutative."""
        if isinstance(other, Vector3):
            x = other.x / self.x
            y = other.y / self.y
            z = other.z / self.z
        else:
            x = other / self.x
            y = other / self.y
            z = other / self.z
        return Vector3(x, y, z)

    def magnitude(self):
        """Compute magnitude (length)."""
        x = self.x**2
        y = self.y**2
        z = self.z**2
        return sqrt(x + y + z)

    def dot(self, other):
        """Compute dot product."""
        a = self.x * other.x
        b = self.y * other.y
        c = self.z * other.z
        return a + b + c

    def cross(self, other):
        """Compute cross product."""
        x = (self.y * other.z) - (self.z * other.y)
        y = (self.z * other.x) - (self.x * other.z)
        z = (self.x * other.y) - (self.y * other.x)
        return Vector3(x, y, z)

    def unit_vector(self):
        """Create vector whose magnitude is 1 (but retains self's direction)."""
        return self / self.magnitude()
