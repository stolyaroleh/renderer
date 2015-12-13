import numpy as np
from math import radians, sin, cos


def normalized(vec):
    norm = np.linalg.norm(vec)
    if norm == 0.0:
        return vec
    return vec / norm


def scale(x, y, z):
    return np.array([x, 0, 0, 0,
                     0, y, 0, 0,
                     0, 0, z, 0,
                     0, 0, 0, 1], 'f').reshape(4, 4)


def uniform_scale(s):
    return scale(s, s, s)


def rotateX(deg):
    a = radians(deg)
    cos_a = cos(a)
    sin_a = sin(a)
    return np.array([1, 0, 0, 0,
                     0, cos_a, -sin_a, 0,
                     0, sin_a,  cos_a, 0,
                     0, 0, 0, 1], 'f').reshape(4, 4)


def rotateY(deg):
    a = radians(deg)
    cos_a = cos(a)
    sin_a = sin(a)
    return np.array([cos_a, 0, sin_a, 0,
                     0, 1, 0, 0,
                     -sin_a, 0, cos_a, 0,
                     0, 0, 0, 1], 'f').reshape(4, 4)


def rotateZ(deg):
    a = radians(deg)
    cos_a = cos(a)
    sin_a = sin(a)
    return np.array([cos_a, -sin_a, 0, 0,
                     sin_a, cos_a, 0, 0,
                     0, 0, 1, 0,
                     0, 0, 0, 1], 'f').reshape(4, 4)


def rotate_axis(deg, axis_x, axis_y, axis_z):
    u, v, w = normalized(np.array([axis_x, axis_y, axis_z]))
    a = radians(deg)
    sin_a = sin(a)
    cos_a = cos(a)

    return np.array([[u*u + (v*v + w*w) * cos_a,
                      u*v * (1 - cos_a) - w * sin_a,
                      u*w * (1 - cos_a) + v * sin_a,
                      0],
                     [u*v * (1 - cos_a) + w * sin_a,
                      v*v + (u*u + w*w) * cos_a,
                      v*w * (1 - cos_a) - u * sin_a,
                      0],
                     [u*w * (1 - cos_a) - v * sin_a,
                      v*w * (1 - cos_a) + u * sin_a,
                      w*w + (u*u + v*v) * cos_a,
                      0],
                     [0, 0, 0, 1]], 'f')


def translate(dx, dy, dz):
    return np.array([[1, 0, 0, dx],
                     [0, 1, 0, dy],
                     [0, 0, 1, dz],
                     [0, 0, 0, 1]], 'f')


def look_at(ex, ey, ez, tx, ty, tz, ux, uy, uz):
    eye = np.array([ex, ey, ez])
    target = np.array([tx, ty, tz])
    up = np.array([ux, uy, uz])

    f = normalized(eye - target)
    u = normalized(up)
    s = normalized(np.cross(f, u))
    u = np.cross(s, f)

    return np.array([[s[0], u[0], -f[0], -np.dot(s, eye)],
                     [s[1], u[1], -f[1], -np.dot(u, eye)],
                     [s[2], u[2], -f[2], -np.dot(f, eye)],
                     [0, 0, 0, 1]], 'f')
