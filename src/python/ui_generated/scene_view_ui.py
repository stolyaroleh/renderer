# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\renderer\qt\scene_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SceneViewWidget(object):
    def setupUi(self, SceneViewWidget):
        SceneViewWidget.setObjectName("SceneViewWidget")
        SceneViewWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(SceneViewWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(SceneViewWidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBoxLayout = QtWidgets.QGridLayout(self.groupBox)
        self.groupBoxLayout.setObjectName("groupBoxLayout")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(SceneViewWidget)
        QtCore.QMetaObject.connectSlotsByName(SceneViewWidget)

    def retranslateUi(self, SceneViewWidget):
        _translate = QtCore.QCoreApplication.translate
        SceneViewWidget.setWindowTitle(_translate("SceneViewWidget", "Form"))
        self.groupBox.setTitle(_translate("SceneViewWidget", "Scene View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SceneViewWidget = QtWidgets.QWidget()
    ui = Ui_SceneViewWidget()
    ui.setupUi(SceneViewWidget)
    SceneViewWidget.show()
    sys.exit(app.exec_())

