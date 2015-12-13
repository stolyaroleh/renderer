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
from math import acos, cos, sin, tan, radians, sqrt
from core.coordinates import from_spherical_deg
from core.shapes import CUBE, SUZANNE
from core.transform import *
from core.shaders import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtGui import QColor


def mmul(*args):
    return reduce(np.dot, args, np.identity(4, 'f'))


class GLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.bg_color = QColor(121, 121, 140)

        # self.orthographic = True
        self.orthographic = False

        self.model = np.identity(4, 'f')
        self.view = np.identity(4, 'f')
        self.projection = np.identity(4, 'f')

        self.cam_rotate = np.identity(4, 'f')

        self.r = 10
        self.fov = 80

    def set_perspective_fov(self, fov, width, height, near, far):
        h = tan(radians(fov) / 2) * near
        w = h * height / width

        self.projection = np.array([w, 0, 0, 0,
                                    0, h, 0, 0,
                                    0, 0, (near + far)/(near - far), 2*far*near/(near - far),
                                    0, 0, -1, 0], 'f').reshape(4, 4).transpose()

    def set_ortho(self, width, height, back, front):
        r = width / 2
        t = height / 2

        self.projection = np.array([1 / r, 0, 0, 0,
                                    0, 1 / t, 0, 0,
                                    0, 0, -2 * (front - back), -(front + back) / (front - back),
                                    0, 0, 0, 1], 'f').reshape(4, 4)

    def initializeGL(self):
        self.shape = SUZANNE
        self.coords = vbo.VBO(self.shape.coords, usage=GL_STATIC_DRAW, target=GL_ARRAY_BUFFER)
        self.indices = vbo.VBO(self.shape.indices, usage=GL_STATIC_DRAW, target=GL_ELEMENT_ARRAY_BUFFER)
        self.zoom_camera(0)

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
        light_pos_world_space_UID = glGetUniformLocation(program, 'light_pos_world_space')

        # glEnable(GL_CULL_FACE)
        # glEnable(GL_DEPTH_TEST)
        # glDepthFunc(GL_LESS)
        glClearColor(self.bg_color.redF(), self.bg_color.greenF(), self.bg_color.blueF(), self.bg_color.alphaF())
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        try:
            glUseProgram(program)
            MVP = mmul(self.projection, self.view, self.model).astype('f')
            glUniformMatrix4fv(MVP_UID, 1, GL_FALSE, MVP)
            glUniformMatrix4fv(M_UID, 1, GL_FALSE, self.model.astype('f'))
            glUniformMatrix4fv(V_UID, 1, GL_FALSE, self.view.astype('f'))
            glUniform3f(color_UID, *np.array([0.4, 0.4, 0.8], 'f'))
            glUniform3f(light_pos_world_space_UID, *np.array([5, 5, 5], 'f'))
            self.coords.bind()
            self.indices.bind()
            try:
                glEnableVertexAttribArray(vertex_pos_model_space_ID)
                glVertexAttribPointer(vertex_pos_model_space_ID, 3, GL_FLOAT, GL_FALSE, 0, self.coords)
                glEnableVertexAttribArray(vertex_normal_model_space_ID)
                glVertexAttribPointer(vertex_normal_model_space_ID, 3, GL_FLOAT, GL_FALSE, 0, self.coords + self.shape.normal_index_offset)
                glDrawElements(GL_TRIANGLES, len(self.indices),
                               GL_UNSIGNED_SHORT, self.indices)
            finally:
                self.indices.unbind()
                self.coords.unbind()
                glDisableVertexAttribArray(vertex_pos_model_space_ID)
                glDisableVertexAttribArray(vertex_normal_model_space_ID)
        finally:
            glUseProgram(0)

    def resizeGL(self, width, height):
        self.width, self.height = width, height
        glViewport(0, 0, width, height)
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

        angle = -acos(min(1, np.dot(a, b)))
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

        self.set_perspective_fov(np.clip(self.fov, 1, 179), self.width, self.height, 0.1, 100)
        self.update()
        print(mmul(self.projection, self.view, np.array([0, 0, 0, 1])))

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = GLWidget(None)
    widget.show()
    sys.exit(app.exec_())
