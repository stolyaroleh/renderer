import os
from core.mesh import Mesh
from itertools import islice

from timeit import default_timer


def read_obj(filename):
    start = default_timer()

    if not os.path.isfile(filename):
        print('File does not exist: {0}'.format(filename))
        return None

    vertices = []
    indices = []
    uvs = []
    uv_indices = []
    normals = []
    normal_indices = []

    def v(args):
        vertices.extend(islice(map(float, args.split()), 0, 3))

    def vt(args):
        uvs.extend(islice(map(float, args.split()), 0, 2))

    def vn(args):
        normals.extend(islice(map(float, args.split()), 0, 2))

    def f(args):
        for a in args.split():
            i = list(map(int, [x or 0 for x in a.split('/')] + [0, 0]))
            indices.append(i[0] - 1)
            uv_indices.append(i[1] - 1)
            normal_indices.append(i[2] - 1)

    actions = {'v': v,
               'vt': vt,
               'vn': vn,
               'f': f}

    with open(filename) as file:
        for tokens in map(lambda x: x.strip().split(' ', 1), file):
            if len(tokens) < 2:
                continue
            action, args = tokens[0], tokens[1]
            actions.get(action, lambda x: None)(args)

    end = default_timer()

    if vertices and indices:
        print('Mesh loaded successfully. Triangle count: {0} \nTime: {1:.2} s'.format(len(vertices) // 3, end - start))
        return Mesh(filename, vertices, indices,
                    normals, normal_indices)

    return None