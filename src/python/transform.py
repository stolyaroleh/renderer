import numpy as np
from math import radians, sin, cos


def normalized(vec):
    norm = np.linalg.norm(vec)
    if norm == 0.0:
        return vec
    return vec / norm


class Transform:
    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = np.identity(4, 'f')
        else:
            self.matrix = matrix

    def uniform_scale(self, s):
        self.scale(s, s, s)

    def scale(self, x, y, z):
        self.matrix = np.matrix([[x, 0, 0, 0],
                                 [0, y, 0, 0],
                                 [0, 0, z, 0],
                                 [0, 0, 0, 1]]) * self.matrix

    def rotateX(self, deg):
        a = radians(deg)
        cos_a = cos(a)
        sin_a = sin(a)
        self.matrix = np.matrix([[1, 0, 0, 0],
                                 [0, cos_a, -sin_a, 0],
                                 [0, sin_a,  cos_a, 0],
                                 [0, 0, 0, 1]]) * self.matrix

    def rotateY(self, deg):
        a = radians(deg)
        cos_a = cos(a)
        sin_a = sin(a)
        self.matrix = np.matrix([[cos_a, 0, sin_a, 0],
                                 [0, 1, 0, 0],
                                 [-sin_a, 0, cos_a, 0],
                                 [0, 0, 0, 1]]) * self.matrix

    def rotateZ(self, deg):
        a = radians(deg)
        cos_a = cos(a)
        sin_a = sin(a)
        self.matrix = np.matrix([[cos_a, -sin_a, 0, 0],
                                 [sin_a, cos_a, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]]) * self.matrix

    def rotate_axis(self, deg, axis_x, axis_y, axis_z):
        v = np.array([axis_x, axis_y, axis_z])
        ax = normalized(v)
        a = radians(deg)
        sin_a = sin(a)
        cos_a = cos(a)

        rot_matrix = np.matrix([[ax[0] * ax[0] + (1 - ax[0] * ax[0]) * cos_a,
                                 ax[0] * ax[1] * (1 - cos_a) - ax[2] * sin_a,
                                 ax[0] * ax[2] * (1 - cos_a) + ax[1] * sin_a,
                                 0],
                                [ax[0] * ax[1] * (1 - cos_a) + ax[2] * sin_a,
                                 ax[1] * ax[1] + (1 - ax[1] * ax[1]) * cos_a,
                                 ax[1] * ax[2] * (1 - cos_a) - ax[0] * sin_a,
                                 0],
                                [ax[0] * ax[2] * (1 - cos_a) - ax[1] * sin_a,
                                 ax[1] * ax[2] * (1 - cos_a) + ax[0] * sin_a,
                                 ax[2] * ax[2] + (1 - ax[2] * ax[2]) * cos_a,
                                 0],
                                [0, 0, 0, 1]])
        self.matrix = rot_matrix * self.matrix

    def translate(self, dx, dy, dz):
        self.matrix = np.matrix([[1, 0, 0, dx],
                                 [0, 1, 0, dy],
                                 [0, 0, 1, dz],
                                 [0, 0, 0, 1]]) * self.matrix

    def get_matrix(self):
        return self.matrix

    def to_array(self):
        return self.matrix.flatten()

if __name__ == '__main__':
    t = Transform()

    def show_transform(x=0, y=0, z=0):
        print(np.round(t.get_matrix() * np.matrix([[x],
                                                   [y],
                                                   [z],
                                                   [1]])))

    t.translate(10, 0, 0)
    t.rotate_axis(180, 0, 1, 0)
    show_transform()
