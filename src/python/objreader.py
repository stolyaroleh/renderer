import os
from core.mesh import Mesh
from itertools import islice


def read_obj(filename):
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
            i = [int(x) or None for x in a.split('/')]
            indices.append(i[0])
            if len(i) == 2 and i[1]:
                uv_indices.append(i)
            if len(i) == 3 and i[2]:
                normal_indices.append(i[2])

    actions = {'v': v,
               'vt': vt,
               'vn': vn,
               'vp': lambda x: None,
               'f': f,
               '#': lambda x: None
               }

    with open(filename) as file:
        for tokens in map(lambda x: x.strip().split(' ', 1), file):
            if len(tokens) < 2:
                continue
            action, args = tokens[0], tokens[1]
            if action in actions:
                actions[action](args)

    if vertices and indices:
        return Mesh(filename, vertices, indices,
                    normals or None,
                    normal_indices or None)

    return None
