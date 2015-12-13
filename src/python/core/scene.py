from objreader import read_obj


class SceneDescription:
    def __init__(self):
        self.meshes = {}

        self.light_pos = (5, 5, 5)
        self.light_intensity = 100

    def import_mesh(self, filename):
        mesh = read_obj(filename)
        if mesh is not None:
            self.meshes[mesh.name] = mesh
