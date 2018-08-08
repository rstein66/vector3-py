"""
camera.py


TODO Rename & add comments for clarity
"""
from tracer.vector import Vector3
from tracer.defaults import *


class Ray(object):

    def __init__(self, origin: Vector3, direction: Vector3):
        self.origin = origin
        self.direction = direction

    def point_at_parameter(self, t: float) -> Vector3:
        return self.origin + t * self.direction


class Camera(object):

    def __init__(self, horizontal=None, lower_left=None, origin=None, vertical=None):
        self.horizontal = horizontal or DEFAULT_HORIZONTAL
        self.lower_left = lower_left or DEFAULT_LOWER_LEFT
        self.origin = origin or DEFAULT_ORIGIN
        self.vertical = vertical or DEFAULT_VERTICAL

    def get_ray(self, u, v):
        direction = self.lower_left - self.origin
        direction += (u * self.horizontal) + (v * self.vertical)

        return Ray(self.origin, direction)
