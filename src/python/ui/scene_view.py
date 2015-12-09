from ui.gl_widget import GLWidget
from ui_generated.scene_view_ui import Ui_SceneViewWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class SceneViewWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.ui = Ui_SceneViewWidget()
        self.ui.setupUi(self)

        self.gl_widget = GLWidget(self)
        self.ui.groupBoxLayout.addWidget(self.gl_widget)

    def makeObject(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = SceneViewWidget(None)
    widget.show()
    sys.exit(app.exec_())
