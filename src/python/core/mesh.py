import numpy as np


class Mesh:
    def __init__(self, name, vertex_buffer, index_buffer, normal_buffer=None, normal_indices=None, transform=None):
        self.name = name

        # we have triangle mesh
        assert len(index_buffer) % 3 == 0

        self.vertices = np.array(vertex_buffer, dtype=np.single)
        self.indices = np.array(index_buffer, dtype=np.uint16)
        self.normals = normal_buffer
        self.normal_indices = normal_indices
        self.transform = transform or np.identity(4)