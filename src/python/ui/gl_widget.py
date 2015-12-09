from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QOpenGLVersionProfile


class GLWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.bg_color = QColor(121, 121, 140)

    def initializeGL(self):
        version = QOpenGLVersionProfile()
        version.setVersion(2, 0)
        self.gl = self.context().versionFunctions(version)
        self.gl.initializeOpenGLFunctions()

        self.set_clear_color(self.bg_color)
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_CULL_FACE)

    def paintGL(self):
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        self.gl.glViewport((width - side) // 2,
                           (height - side) // 2,
                           side, side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def set_clear_color(self, c):
        self.gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = GLWidget(None)
    widget.show()
    sys.exit(app.exec_())
