import numpy as np


class Mesh:
    def __init__(self, name, vertex_buffer, index_buffer, normal_buffer=[], normal_indices=[], transform=None):
        self.name = name

        # we have triangle mesh
        assert len(vertex_buffer) % 3 == 0

        self.coords = np.array(vertex_buffer, dtype=np.single)
        self.indices = np.array(index_buffer, dtype=np.uint16)
        self.normal_index_offset = len(self.indices)
        self.coords = np.append(self.coords, np.array(normal_buffer, dtype=np.single))
        self.indices = np.append(self.indices, np.array(normal_indices, dtype=np.uint16))

        self.transform = transform or np.identity(4)
