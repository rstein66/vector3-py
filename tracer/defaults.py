"""
defaults.py
"""

from tracer.vector import Vector3


DEFAULT_HORIZONTAL = Vector3(4.0, 0.0, 0.0)
DEFAULT_LOWER_LEFT = Vector3(-2.0, -1.0, -1.0)
DEFAULT_ORIGIN = Vector3(0.0, 0.0, 0.0)
DEFAULT_VERTICAL = Vector3(0.0, 2.0, 0.0)


__all__ = ["DEFAULT_HORIZONTAL", "DEFAULT_LOWER_LEFT", "DEFAULT_ORIGIN",
           "DEFAULT_VERTICAL"]
