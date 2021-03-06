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
        SceneViewWidget.resize(741, 463)
        self.gridLayout = QtWidgets.QGridLayout(SceneViewWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(SceneViewWidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBoxLayout = QtWidgets.QGridLayout(self.groupBox)
        self.groupBoxLayout.setObjectName("groupBoxLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.groupBox_2)
        self.toolBox.setObjectName("toolBox")
        self.Meshes = QtWidgets.QWidget()
        self.Meshes.setGeometry(QtCore.QRect(0, 0, 380, 343))
        self.Meshes.setObjectName("Meshes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Meshes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Meshes)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rx = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.rx.setMinimum(-360.0)
        self.rx.setMaximum(360.0)
        self.rx.setObjectName("rx")
        self.gridLayout_4.addWidget(self.rx, 0, 1, 1, 1)
        self._rlbl = QtWidgets.QLabel(self.groupBox_3)
        self._rlbl.setObjectName("_rlbl")
        self.gridLayout_4.addWidget(self._rlbl, 0, 0, 1, 1)
        self._tlbl = QtWidgets.QLabel(self.groupBox_3)
        self._tlbl.setObjectName("_tlbl")
        self.gridLayout_4.addWidget(self._tlbl, 2, 0, 1, 1)
        self.rz = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.rz.setMinimum(-360.0)
        self.rz.setMaximum(360.0)
        self.rz.setObjectName("rz")
        self.gridLayout_4.addWidget(self.rz, 0, 3, 1, 1)
        self.ry = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.ry.setMinimum(-360.0)
        self.ry.setMaximum(360.0)
        self.ry.setObjectName("ry")
        self.gridLayout_4.addWidget(self.ry, 0, 2, 1, 1)
        self.ty = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.ty.setMinimum(-500.0)
        self.ty.setMaximum(500.0)
        self.ty.setObjectName("ty")
        self.gridLayout_4.addWidget(self.ty, 2, 2, 1, 1)
        self.tz = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.tz.setMinimum(-500.0)
        self.tz.setMaximum(500.0)
        self.tz.setObjectName("tz")
        self.gridLayout_4.addWidget(self.tz, 2, 3, 1, 1)
        self.tx = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.tx.setMinimum(-500.0)
        self.tx.setMaximum(500.0)
        self.tx.setObjectName("tx")
        self.gridLayout_4.addWidget(self.tx, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.meshes_list = QtWidgets.QListWidget(self.Meshes)
        self.meshes_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.meshes_list.setObjectName("meshes_list")
        self.gridLayout_3.addWidget(self.meshes_list, 1, 0, 1, 2)
        self.delete_btn = QtWidgets.QPushButton(self.Meshes)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout_3.addWidget(self.delete_btn, 2, 1, 1, 1)
        self.toolBox.addItem(self.Meshes, "")
        self.Light = QtWidgets.QWidget()
        self.Light.setGeometry(QtCore.QRect(0, 0, 380, 343))
        self.Light.setObjectName("Light")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Light)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self._llbl = QtWidgets.QLabel(self.Light)
        self._llbl.setObjectName("_llbl")
        self.gridLayout_5.addWidget(self._llbl, 0, 0, 1, 1)
        self.lposx = QtWidgets.QDoubleSpinBox(self.Light)
        self.lposx.setMinimum(-500.0)
        self.lposx.setMaximum(500.0)
        self.lposx.setProperty("value", -10.0)
        self.lposx.setObjectName("lposx")
        self.gridLayout_5.addWidget(self.lposx, 0, 1, 1, 1)
        self.lposy = QtWidgets.QDoubleSpinBox(self.Light)
        self.lposy.setMinimum(-500.0)
        self.lposy.setMaximum(500.0)
        self.lposy.setProperty("value", 10.0)
        self.lposy.setObjectName("lposy")
        self.gridLayout_5.addWidget(self.lposy, 0, 2, 1, 1)
        self.lposz = QtWidgets.QDoubleSpinBox(self.Light)
        self.lposz.setMinimum(-500.0)
        self.lposz.setMaximum(500.0)
        self.lposz.setProperty("value", -10.0)
        self.lposz.setObjectName("lposz")
        self.gridLayout_5.addWidget(self.lposz, 0, 3, 1, 1)
        self._ilbl = QtWidgets.QLabel(self.Light)
        self._ilbl.setObjectName("_ilbl")
        self.gridLayout_5.addWidget(self._ilbl, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.Light)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 3, 0, 1, 1)
        self.filename = QtWidgets.QLineEdit(self.Light)
        self.filename.setObjectName("filename")
        self.gridLayout_5.addWidget(self.filename, 3, 1, 1, 3)
        self.render_btn = QtWidgets.QPushButton(self.Light)
        self.render_btn.setObjectName("render_btn")
        self.gridLayout_5.addWidget(self.render_btn, 4, 1, 1, 3)
        self.intensity = QtWidgets.QDoubleSpinBox(self.Light)
        self.intensity.setMaximum(99999.99)
        self.intensity.setProperty("value", 3.0)
        self.intensity.setObjectName("intensity")
        self.gridLayout_5.addWidget(self.intensity, 1, 1, 1, 3)
        self.toolBox.addItem(self.Light, "")
        self.gridLayout_2.addWidget(self.toolBox, 1, 0, 1, 1)
        self.groupBoxLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gl_layout = QtWidgets.QGridLayout()
        self.gl_layout.setObjectName("gl_layout")
        self.groupBoxLayout.addLayout(self.gl_layout, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(SceneViewWidget)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SceneViewWidget)

    def retranslateUi(self, SceneViewWidget):
        _translate = QtCore.QCoreApplication.translate
        SceneViewWidget.setWindowTitle(_translate("SceneViewWidget", "Form"))
        self.groupBox.setTitle(_translate("SceneViewWidget", "Scene View"))
        self.groupBox_2.setTitle(_translate("SceneViewWidget", "Scene"))
        self.groupBox_3.setTitle(_translate("SceneViewWidget", "Transform"))
        self._rlbl.setText(_translate("SceneViewWidget", "Rotation"))
        self._tlbl.setText(_translate("SceneViewWidget", "Translation"))
        self.delete_btn.setText(_translate("SceneViewWidget", "Delete"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Meshes), _translate("SceneViewWidget", "Meshes"))
        self._llbl.setText(_translate("SceneViewWidget", "Position"))
        self._ilbl.setText(_translate("SceneViewWidget", "Intensity"))
        self.label.setText(_translate("SceneViewWidget", "Output filename:"))
        self.filename.setText(_translate("SceneViewWidget", "image"))
        self.render_btn.setText(_translate("SceneViewWidget", "Render"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Light), _translate("SceneViewWidget", "Light"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SceneViewWidget = QtWidgets.QWidget()
    ui = Ui_SceneViewWidget()
    ui.setupUi(SceneViewWidget)
    SceneViewWidget.show()
    sys.exit(app.exec_())

