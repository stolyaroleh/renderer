import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo as glvbo
from OpenGL.GL.shaders import compileProgram, compileShader

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtGui import QColor, QOpenGLVersionProfile


OpenGL.FULL_LOGGING = True
OpenGL.ARRAY_SIZE_CHECKING = True

vertex_shader = \
    '''
    attribute vec3 vertexPosition_modelspace;

    uniform mat4 MVP;

    void main(){
        // Output position of the vertex, in clip space : MVP * position
        gl_Position =  MVP * vec4(vertexPosition_modelspace, 1);
    }
    '''

fragment_shader = \
    '''
    void main(void)
    {
      gl_FragColor = vec4(0.5, 0.5, 0.5, 1.0);
    }
    '''


data = np.array([-1.0, -1.0, -1.0,
                 -1.0, -1.0, 1.0,
                 -1.0, 1.0, 1.0,
                 1.0, 1.0, -1.0,
                 -1.0, -1.0, -1.0,
                 -1.0, 1.0, -1.0,
                 1.0, -1.0, 1.0,
                 -1.0, -1.0, -1.0,
                 1.0, -1.0, -1.0,
                 1.0, 1.0, -1.0,
                 1.0, -1.0, -1.0,
                 -1.0, -1.0, -1.0,
                 -1.0, -1.0, -1.0,
                 -1.0, 1.0, 1.0,
                 -1.0, 1.0, -1.0,
                 1.0, -1.0, 1.0,
                 -1.0, -1.0, 1.0,
                 -1.0, -1.0, -1.0,
                 -1.0, 1.0, 1.0,
                 -1.0, -1.0, 1.0,
                 1.0, -1.0, 1.0,
                 1.0, 1.0, 1.0,
                 1.0, -1.0, -1.0,
                 1.0, 1.0, -1.0,
                 1.0, -1.0, -1.0,
                 1.0, 1.0, 1.0,
                 1.0, -1.0, 1.0,
                 1.0, 1.0, 1.0,
                 1.0, 1.0, -1.0,
                 -1.0, 1.0, -1.0,
                 1.0, 1.0, 1.0,
                 -1.0, 1.0, -1.0,
                 -1.0, 1.0, 1.0,
                 1.0, 1.0, 1.0,
                 -1.0, 1.0, 1.0,
                 1.0, -1.0, 1.0
                 ], dtype=np.single) * 20


class GLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.bg_color = QColor(121, 121, 140)

        self.set_model_matrix(np.identity(4))
        self.set_view_matrix(np.identity(4))
        self.set_projection_matrix(np.identity(4))

    def set_projection_matrix(self, matrix):
        assert matrix.shape == (4, 4)
        self.projection = matrix

    def set_view_matrix(self, matrix):
        assert matrix.shape == (4, 4)
        self.view = matrix

    def set_model_matrix(self, matrix):
        assert matrix.shape == (4, 4)
        self.model = matrix

    def initializeGL(self):
        self.vbo = glvbo.VBO(data)


    def paintGL(self):
        self.program = compileProgram(compileShader(vertex_shader, GL_VERTEX_SHADER),
                                      compileShader(fragment_shader, GL_FRAGMENT_SHADER))
        glLinkProgram(self.program)
        glUseProgram(self.program)

        glClearColor(self.bg_color.redF(), self.bg_color.greenF(), self.bg_color.blueF(), self.bg_color.alphaF())
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        gluLookAt(5, 5, 5,
                  0, 0, 0,
                  0, 1, 0)


        self.vbo.bind()

        glColor(0.7, 0.6, 0.8)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.vbo)
        glDrawArrays(GL_TRIANGLES, 0, len(data))

    def resizeGL(self, width, height):
        self.width, self.height = width, height
        aspect_ratio = width / height
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)

        glFrustum(-100 * aspect_ratio,
                  100 * aspect_ratio,
                  -100,
                  100,
                  10, 100)


    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.mouse_move(dx, dy)

        self.lastPos = event.pos()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouse_move(self, dx, dy):
        self.dx = dx
        self.dy = dy


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = GLWidget(None)
    widget.set_projection_matrix(np.identity(4))
    # widget.show()
    sys.exit(app.exec_())