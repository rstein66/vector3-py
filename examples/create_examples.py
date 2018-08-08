"""
Create example graphics.
method_name creates $PWD/method_name.ppm

TODO Add additional examples
TODO Clean up
"""

import random

# from tracer.defaults import *
from tracer.camera import Ray, Camera
from tracer.vector import Vector3


def blue_white():
    def get_color(ray: Ray) -> Vector3:
        unit_direction = ray.direction.unit_vector()
        t = 0.5 * unit_direction.y + 1.0
        return (1.0 - t) * Vector3(1.0, 1.0, 1.0) + t * Vector3(0.5, 0.7, 1.0)

    nx = 200
    ny = 100

    with open("blue_white.ppm", "w") as outfile:
        outfile.write(f"P3\n{nx} {ny}\n255\n")
        camera = Camera()
        for j in range(ny - 1, -1, -1):
            for i in range(0, nx):
                u = float(i + random.random()) / float(nx)
                v = float(j + random.random()) / float(ny)
                ray = camera.get_ray(u, v)
                color = get_color(ray)
                ir = int(255.99 * color.r)
                ig = int(255.99 * color.g)
                ib = int(255.99 * color.b)
                outfile.write(f"{ir} {ig} {ib}\n")


if __name__ == '__main__':
    blue_white()
