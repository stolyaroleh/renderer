from ui_generated.main_window_ui import Ui_MainWindow
from ui.console_widget import ConsoleWidget
from ui.render_view import RenderViewWidget
from ui.scene_view import SceneViewWidget
from core.scene import SceneDescription

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog, QWidget


class MainWindow(Ui_MainWindow):
    def __init__(self, parent, out_pipe, dark=False):
        self.parent = parent
        if dark:
            self.console = ConsoleWidget(out_pipe,
                                         QColor(220, 220, 220),
                                         QColor(255, 220, 50),
                                         QColor(255, 50, 50))
        else:
            self.console = ConsoleWidget(out_pipe,
                                         QColor(0, 0, 0),
                                         QColor(255, 220, 30),
                                         QColor(255, 0, 0))

        self.scene = SceneDescription()
        self.scene_view = SceneViewWidget(self.parent, self, self.scene)
        self.render_view_widget = QWidget()
        self.render_view = RenderViewWidget(self.render_view_widget)

    def initialize(self):
        self.gridLayout.addWidget(self.scene_view)
        self.gridLayout.addWidget(self.render_view_widget, 0, 1)

        self.render_view.setupUi(self.render_view_widget)

        self.console.setupUi(self.console_dock_contents)
        self.console.initialize()

        self.action_console.triggered.connect(self.toggle_log)
        self.action_render_view.triggered.connect(self.toggle_render_view)
        self.action_scene_view.triggered.connect(self.toggle_scene_view)
        self.action_toggle_fullscreen.triggered.connect(self.toggle_fullscreen)
        self.action_quit.triggered.connect(self.close)

        self.action_obj.triggered.connect(self.import_obj)

        self.centralwidget.addAction(self.action_console)
        self.centralwidget.addAction(self.action_render_view)
        self.centralwidget.addAction(self.action_scene_view)
        self.centralwidget.addAction(self.action_toggle_fullscreen)
        self.centralwidget.addAction(self.action_quit)
        self.centralwidget.addAction(self.action_obj)

        self.action_render_view.setChecked(False)
        self.toggle_render_view()

    def toggle_log(self):
        self.console_dock.setVisible(self.action_console.isChecked())

    def toggle_render_view(self):
        self.render_view_widget.setVisible(self.action_render_view.isChecked())
        pass

    def toggle_scene_view(self):
        self.scene_view.setVisible(self.action_scene_view.isChecked())

    def toggle_fullscreen(self):
        if self.action_toggle_fullscreen.isChecked():
            self.parent.showFullScreen()
            self.parent.menuBar().hide()
        else:
            self.parent.showNormal()
            self.parent.menuBar().show()

    def import_obj(self):
        filename, _ = QFileDialog.getOpenFileName(self.parent, 'Import .obj', r'w:\Renderer\obj', '.obj (*.obj)')
        if not filename:
            return

        print('Loading...  {0}'.format(filename))
        self.scene.import_mesh(filename)
        self.scene_view.update_list()
        self.scene_view.refresh()

    def load_png(self, filename):
        self.action_scene_view.setChecked(False)
        self.toggle_scene_view()
        self.render_view.show(filename)

    def close(self):
        self.parent.close()
