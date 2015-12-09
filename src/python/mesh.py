from transform import Transform


class Mesh:
    def __init__(self, name, vertex_buffer, index_buffer, transform=None):
        self.name = name
        # we have triangle mesh
        assert len(index_buffer) // 3 == 0
        self.vertex_buffer = vertex_buffer
        self.index_buffer = index_buffer

        self.transform = transform or Transform()
