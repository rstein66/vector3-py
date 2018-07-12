"""
vector.py

3-D vector implementation.

Note: First iteration. Inefficient implementation.
"""
import math


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):  # for debugging
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):  # for printing
        return f"{self.x}, {self.y}, {self.z}"

    def __eq__(self, other):
        """Overload equality operator."""
        if not isinstance(other, Vector):
            return False
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __add__(self, other):
        """Overload addition operator."""
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
        else:
            x = self.x + other
            y = self.y + other
            z = self.z + other
        return Vector(x, y, z)

    # Support "reverse[d]" addition.
    # Aliasing (w/c?) works because addition is commutative.
    # i.e., a + b == b + a
    __radd__ = __add__

    def __sub__(self, other):
        """Overload subtraction operator."""
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
        else:
            x = self.x - other
            y = self.y - other
            z = self.z - other
        return Vector(x, y, z)

    def __rsub__(self, other):
        """Reversed subtraction. Subtraction is noncommutative."""
        if isinstance(other, Vector):
            x = other.x - self.x
            y = other.y - self.y
            z = other.z - self.z
        else:
            x = other - self.x
            y = other - self.y
            z = other - self.z
        return Vector(x, y, z)

    def __mul__(self, other):
        """Overload multiplication operator."""
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
        else:
            x = self.x * other
            y = self.y * other
            z = self.z * other
        return Vector(x, y, z)

    __rmul__ = __mul__  # "Reverse[d]" multiplication

    def __truediv__(self, other):
        """Overload divison operator."""
        if isinstance(other, Vector):
            x = self.x / other.x
            y = self.y / other.y
            z = self.z / other.z
        else:
            x = self.x / other
            y = self.y / other
            z = self.z / other
        return Vector(x, y, z)

    def __rtruediv__(self, other):
        """Reversed divison. Divison is noncommutative."""
        if isinstance(other, Vector):
            x = other.x / self.x
            y = other.y / self.y
            z = other.z / self.z
        else:
            x = other / self.x
            y = other / self.y
            z = other / self.z
        return Vector(x, y, z)

    def magnitude(self):
        """Compute magnitude (length)."""
        x = self.x**2
        y = self.y**2
        z = self.z**2
        return math.sqrt(x + y + z)

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
        return Vector(x, y, z)

    def unit_vector(self):
        """Create vector whose magnitude is 1 (but retains self's direction)."""
        return self / self.magnitude()
