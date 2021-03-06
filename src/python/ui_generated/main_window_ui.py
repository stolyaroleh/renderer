# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\renderer\qt\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.console_dock = QtWidgets.QDockWidget(MainWindow)
        self.console_dock.setMinimumSize(QtCore.QSize(600, 200))
        self.console_dock.setFloating(False)
        self.console_dock.setObjectName("console_dock")
        self.console_dock_contents = QtWidgets.QWidget()
        self.console_dock_contents.setObjectName("console_dock_contents")
        self.console_dock.setWidget(self.console_dock_contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console_dock)
        self.action_console = QtWidgets.QAction(MainWindow)
        self.action_console.setCheckable(True)
        self.action_console.setChecked(True)
        self.action_console.setObjectName("action_console")
        self.action_scene_view = QtWidgets.QAction(MainWindow)
        self.action_scene_view.setCheckable(True)
        self.action_scene_view.setChecked(True)
        self.action_scene_view.setObjectName("action_scene_view")
        self.action_render_view = QtWidgets.QAction(MainWindow)
        self.action_render_view.setCheckable(True)
        self.action_render_view.setChecked(True)
        self.action_render_view.setObjectName("action_render_view")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_obj = QtWidgets.QAction(MainWindow)
        self.action_obj.setObjectName("action_obj")
        self.action_toggle_fullscreen = QtWidgets.QAction(MainWindow)
        self.action_toggle_fullscreen.setCheckable(True)
        self.action_toggle_fullscreen.setObjectName("action_toggle_fullscreen")
        self.menuView.addAction(self.action_console)
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_scene_view)
        self.menuView.addAction(self.action_render_view)
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_toggle_fullscreen)
        self.menuImport.addAction(self.action_obj)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.console_dock.setWindowTitle(_translate("MainWindow", "Console"))
        self.action_console.setText(_translate("MainWindow", "Console"))
        self.action_console.setShortcut(_translate("MainWindow", "C"))
        self.action_scene_view.setText(_translate("MainWindow", "Scene View"))
        self.action_scene_view.setShortcut(_translate("MainWindow", "2"))
        self.action_render_view.setText(_translate("MainWindow", "Render View"))
        self.action_render_view.setShortcut(_translate("MainWindow", "1"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.action_quit.setShortcut(_translate("MainWindow", "Esc"))
        self.action_obj.setText(_translate("MainWindow", "Wavefront .obj"))
        self.action_obj.setToolTip(_translate("MainWindow", ".obj"))
        self.action_obj.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.action_toggle_fullscreen.setText(_translate("MainWindow", "Toggle Fullscreen"))
        self.action_toggle_fullscreen.setShortcut(_translate("MainWindow", "Alt+Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

