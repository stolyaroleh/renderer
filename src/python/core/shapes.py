from core.mesh import Mesh
from objreader import read_obj

vertices = [1.000000, -1.000000, -1.000000,
            1.000000, -1.000000, 1.000000,
            -1.000000, -1.000000, 1.000000,
            -1.000000, -1.000000, -1.000000,
            1.000000, 1.000000, -0.999999,
            0.999999, 1.000000, 1.000001,
            -1.000000, 1.000000, 1.000000,
            -1.000000, 1.000000, -1.000000]

indices = [i - 1 for i in [2, 3, 4,
                           8, 7, 6,
                           5, 6, 2,
                           6, 7, 3,
                           3, 7, 8,
                           1, 4, 8,
                           1, 2, 4,
                           5, 8, 6,
                           1, 5, 2,
                           2, 6, 3,
                           4, 3, 8,
                           5, 1, 8]]

CUBE = Mesh("Cube", vertices, indices)

triangle_vertices = [-1, -1, 0,
                     0, 1, 0,
                     1, -1, 0]

triangle_indices = [0, 1, 2]

TRIANGLE = Mesh("Triangle", triangle_vertices, triangle_indices)

SUZANNE = read_obj(r'W:\renderer\obj\suzanne.obj')