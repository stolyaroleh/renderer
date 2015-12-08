from ui_generated.main_window_ui import Ui_MainWindow
from ui.console_widget import ConsoleWidget


class MainWindow(Ui_MainWindow):
    def __init__(self, parent, out_pipe):
        self.parent = parent
        self.console = ConsoleWidget(out_pipe)

    def initialize(self):
        self.console.setupUi(self.console_dock_contents)
        self.console.initialize()

        self.action_console.triggered.connect(self.toggle_log)
        self.action_render_view.triggered.connect(self.toggle_render_view)
        self.action_scene_view.triggered.connect(self.toggle_scene_view)
        self.action_quit.triggered.connect(self.close)

    def toggle_log(self):
        self.console_dock.setVisible(self.action_console.isChecked())

    def toggle_render_view(self):
        self.render_view.setVisible(self.action_render_view.isChecked())

    def toggle_scene_view(self):
        self.scene_view.setVisible(self.action_scene_view.isChecked())

    def close(self):
        self.parent.close()
