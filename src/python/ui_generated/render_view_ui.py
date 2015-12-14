# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\renderer\qt\render_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RenderViewWidget(object):
    def setupUi(self, RenderViewWidget):
        RenderViewWidget.setObjectName("RenderViewWidget")
        RenderViewWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(RenderViewWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(RenderViewWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image = QtWidgets.QLabel(self.groupBox)
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(RenderViewWidget)
        QtCore.QMetaObject.connectSlotsByName(RenderViewWidget)

    def retranslateUi(self, RenderViewWidget):
        _translate = QtCore.QCoreApplication.translate
        RenderViewWidget.setWindowTitle(_translate("RenderViewWidget", "Form"))
        self.groupBox.setTitle(_translate("RenderViewWidget", "Render View"))
        self.image.setText(_translate("RenderViewWidget", "Image not loaded"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RenderViewWidget = QtWidgets.QWidget()
    ui = Ui_RenderViewWidget()
    ui.setupUi(RenderViewWidget)
    RenderViewWidget.show()
    sys.exit(app.exec_())

