# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\renderer\qt\console_widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConsoleWidget(object):
    def setupUi(self, ConsoleWidget):
        ConsoleWidget.setObjectName("ConsoleWidget")
        ConsoleWidget.resize(554, 300)
        self.gridLayout = QtWidgets.QGridLayout(ConsoleWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.text_edit = QtWidgets.QTextEdit(ConsoleWidget)
        self.text_edit.setReadOnly(True)
        self.text_edit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 0, 0, 1, 1)
        self._formLayout = QtWidgets.QFormLayout()
        self._formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self._formLayout.setObjectName("_formLayout")
        self.clear_btn = QtWidgets.QPushButton(ConsoleWidget)
        self.clear_btn.setObjectName("clear_btn")
        self._formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.clear_btn)
        self.gridLayout.addLayout(self._formLayout, 0, 1, 1, 1)

        self.retranslateUi(ConsoleWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleWidget)

    def retranslateUi(self, ConsoleWidget):
        _translate = QtCore.QCoreApplication.translate
        ConsoleWidget.setWindowTitle(_translate("ConsoleWidget", "Form"))
        self.clear_btn.setText(_translate("ConsoleWidget", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsoleWidget = QtWidgets.QWidget()
    ui = Ui_ConsoleWidget()
    ui.setupUi(ConsoleWidget)
    ConsoleWidget.show()
    sys.exit(app.exec_())

