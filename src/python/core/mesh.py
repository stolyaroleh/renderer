import numpy as np
from core.transform import Transform


class Mesh:
    def __init__(self, name, vertices, vertex_indices, normals, normal_indices, transform=None):
        self.name = name

        # we have triangle mesh
        assert len(vertex_indices) % 3 == 0
        assert len(normal_indices) == len(vertex_indices)

        self.v = np.array(vertices, dtype=np.single)
        self.n = np.array(normals, dtype=np.single)
        self.vi = np.array(vertex_indices, dtype=np.uint32)
        self.ni = np.array(normal_indices, dtype=np.uint32) + len(vertices)
        self.coords = np.concatenate((self.v, self.n))
        self.indices = np.concatenate((self.vi, self.ni))
        self.normal_index_offset = len(vertex_indices)

        self.transform = transform or Transform()
