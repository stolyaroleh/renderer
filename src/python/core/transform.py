import numpy as np
from math import radians, sin, cos


def normalized(vec):
    norm = np.linalg.norm(vec)
    if norm == 0.0:
        return vec
    return vec / norm


def scale(x, y, z):
    return np.array([[x, 0, 0, 0],
                     [0, y, 0, 0],
                     [0, 0, z, 0],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


def uniform_scale(s):
    return scale(s, s, s)


def rotateX(deg):
    a = radians(deg)
    cos_a = cos(a)
    sin_a = sin(a)
    return np.array([[1, 0, 0, 0],
                     [0, cos_a, -sin_a, 0],
                     [0, sin_a,  cos_a, 0],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


def rotateY(deg):
    a = radians(deg)
    cos_a = cos(a)
    sin_a = sin(a)
    return np.array([[cos_a, 0, sin_a, 0],
                     [0, 1, 0, 0],
                     [-sin_a, 0, cos_a, 0],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


def rotateZ(deg):
    a = radians(deg)
    cos_a = cos(a)
    sin_a = sin(a)
    return np.array([[cos_a, -sin_a, 0, 0],
                     [sin_a, cos_a, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


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
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


def translate(dx, dy, dz):
    return np.array([[1, 0, 0, dx],
                     [0, 1, 0, dy],
                     [0, 0, 1, dz],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


def look_at(ex, ey, ez, tx, ty, tz, ux, uy, uz):
    eye = np.array([ex, ey, ez])
    target = np.array([tx, ty, tz])
    up = np.array([ux, uy, uz])

    f = normalized(target - eye)
    s = normalized(np.cross(f, up))
    u = normalized(np.cross(s, f))

    return np.array([[s[0], s[1], s[2], -np.dot(s, eye)],
                     [u[0], u[1], u[2], -np.dot(u, eye)],
                     [-f[0], -f[1], -f[2], np.dot(f, eye)],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


class Transform:
    def __init__(self):
        self.matrix = np.identity(4, 'f')

        self.tx = 0.0
        self.ty = 0.0
        self.tz = 0.0
        self.rx = 0.0
        self.ry = 0.0
        self.rz = 0.0

    def update(self, tx, ty, tz, rx, ry, rz):
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.rx = rx
        self.ry = ry
        self.rz = rz

    def get_matrix(self):
        self.matrix = translate(self.tx, self.ty, self.tz) * \
                      rotateZ(self.rz) * \
                      rotateY(self.ry) * \
                      rotateX(self.rx)
