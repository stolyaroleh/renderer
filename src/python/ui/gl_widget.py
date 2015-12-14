import OpenGL

OpenGL.USE_ACCELERATE = False
OpenGL.ERROR_ON_COPY = True
OpenGL.ERROR_CHECKING = True
OpenGL.FULL_LOGGING = True
OpenGL.ARRAY_SIZE_CHECKING = True

import numpy as np
np.set_printoptions(precision=2, suppress=True)

from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.arrays import vbo

from functools import reduce
from math import acos, tan, sqrt
from random import random

from core.transform import *
from core.shaders import fragment_shaded, vertex_shaded

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget

IDENTITY = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], dtype=np.float32, order='F').reshape(4, 4)


def mmul(*args):
    return reduce(np.dot, args, IDENTITY.copy())


class GLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.orthographic = True

        self.view = IDENTITY.copy()
        self.projection = IDENTITY.copy()
        self.cam_rotate = IDENTITY.copy()

        self.r = 10
        self.fov = 80
        self.light_pos = (25, 25, 25)
        self.light_intensity = 20.0

        self.to_render = []
        self.to_update = []

    def set_perspective_fov(self, fovy, aspect, z_near, z_far):
        tan_half_fovy = tan(radians(fovy) / 2)
        self.projection = np.array([[1 / (aspect * tan_half_fovy), 0, 0, 0],
                                    [0, 1 / tan_half_fovy, 0, 0],
                                    [0, 0, -(z_far + z_near) / (z_far - z_near), -2 * z_far * z_near / (z_far - z_near)],
                                    [0, 0, -1, 0]], dtype=np.float32).reshape(4, 4)

    def set_ortho(self, width, height, z_near, z_far):
        r = width / 2
        t = height / 2

        self.projection = np.array([[1 / r, 0, 0, 0],
                                    [0, 1 / t, 0, 0],
                                    [0, 0, -2 / (z_far - z_near), -(z_far + z_near) / (z_far - z_near)],
                                    [0, 0, 0, 1]], dtype=np.float32).reshape(4, 4)

    def initializeGL(self):
        pass

    def schedule_buffer_update(self, meshes):
        self.to_update = meshes

    def update_buffers(self):
        self.to_render.clear()
        for mesh in self.to_update:
            data = vbo.VBO(mesh.coords, usage=GL_STATIC_DRAW, target=GL_ARRAY_BUFFER)
            indices = vbo.VBO(mesh.indices, usage=GL_STATIC_DRAW, target=GL_ELEMENT_ARRAY_BUFFER)
            offset = mesh.normal_index_offset
            model_view_matrix = mesh.transform.matrix
            color = np.array([random(),
                              random(),
                              random()], 'f') * 2
            self.to_render.append((data, indices, offset, model_view_matrix, color))

    def paintGL(self):
        program = compileProgram(compileShader(vertex_shaded, GL_VERTEX_SHADER),
                                 compileShader(fragment_shaded, GL_FRAGMENT_SHADER))
        glLinkProgram(program)

        vertex_pos_model_space_ID = glGetAttribLocation(program, 'vertex_pos_model_space')
        vertex_normal_model_space_ID = glGetAttribLocation(program, 'vertex_normal_model_space')
        MVP_UID = glGetUniformLocation(program, 'MVP')
        M_UID = glGetUniformLocation(program, 'M')
        V_UID = glGetUniformLocation(program, 'V')
        color_UID = glGetUniformLocation(program, 'color')
        light_intensity_UID = glGetUniformLocation(program, 'light_intensity')
        light_pos_world_space_UID = glGetUniformLocation(program, 'light_pos_world_space')

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glClearColor(0.2, 0.3, 0.35, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.to_update:
            self.update_buffers()
            self.to_update = []

        for data, indices, offset, model_matrix, color in self.to_render:
            try:
                glUseProgram(program)
                MVP = mmul(self.projection, self.view, model_matrix)
                glUniformMatrix4fv(MVP_UID, 1, GL_FALSE, MVP)
                glUniformMatrix4fv(M_UID, 1, GL_FALSE, model_matrix)
                glUniformMatrix4fv(V_UID, 1, GL_FALSE, self.view)
                glUniform1f(light_intensity_UID, np.single(10 * self.light_intensity))
                glUniform3f(color_UID, *color)
                glUniform3f(light_pos_world_space_UID, *np.array(self.light_pos, 'f'))
                data.bind()
                indices.bind()
                try:
                    glEnableVertexAttribArray(vertex_pos_model_space_ID)
                    glVertexAttribPointer(vertex_pos_model_space_ID, 3, GL_FLOAT, GL_FALSE, 12, data)
                    glEnableVertexAttribArray(vertex_normal_model_space_ID)
                    glVertexAttribPointer(vertex_normal_model_space_ID, 3, GL_FLOAT, GL_FALSE, 12, data)
                    glDrawElements(GL_TRIANGLES, len(indices),
                                   GL_UNSIGNED_INT, indices)
                finally:
                    indices.unbind()
                    data.unbind()
                    glDisableVertexAttribArray(vertex_pos_model_space_ID)
                    glDisableVertexAttribArray(vertex_normal_model_space_ID)
            finally:
                glUseProgram(0)

    def resizeGL(self, width, height):
        self.width, self.height = width, height
        self.compute_view()

    def mousePressEvent(self, event):
        self.last_pos = event.x(), event.y()

    def mouseMoveEvent(self, event):
        new_pos = event.x(), event.y()

        if event.buttons() & Qt.LeftButton:
            self.arcball_rotate(new_pos, self.last_pos)
            self.compute_view()

        if event.buttons() & Qt.RightButton:
            self.zoom_camera(new_pos[0] - self.last_pos[0])
            self.compute_view()

        if event.buttons() & Qt.MidButton:
            self.fov += new_pos[0] - self.last_pos[0]
            self.compute_view()

        self.last_pos = new_pos

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def arcball_rotate(self, p1, p2):
        a = self.get_arcball_vector(*p1)
        b = self.get_arcball_vector(*p2)

        angle = acos(min(1, np.dot(a, b)))
        axis = np.cross(a, b)
        self.cam_rotate = mmul(rotate_axis(angle * 180, *axis), self.cam_rotate)

    def zoom_camera(self, delta):
        self.r += delta
        if self.r < 1:
            self.r = 1

    def get_arcball_vector(self, x, y):
        p = np.array([(x / self.width * 2) - 1,
                      1 - (y / self.height * 2),
                      0])
        op_squared = p[0] * p[0] + p[1] * p[1]
        if op_squared <= 1:
            p[2] = sqrt(1 - op_squared)
        else:
            p = normalized(p)
        return p

    def compute_view(self):
        self.camera_pos = mmul(self.cam_rotate, np.array([0, 0, self.r / 100, 1]))

        self.view = look_at(self.camera_pos[0], self.camera_pos[1], self.camera_pos[2],
                            0, 0, 0,
                            0, 1, 0)
        if self.orthographic:
            ar = self.width / self.height
            s = self.r / 100
            self.set_ortho(ar * s, s, -100, 100)
        else:
            self.set_perspective_fov(np.clip(self.fov, 1, 179), self.width / self.height, 0.1, 100)
        self.update()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = GLWidget(None)
    widget.show()
    sys.exit(app.exec_())
