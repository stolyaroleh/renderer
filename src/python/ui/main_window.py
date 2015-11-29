from ui_generated.main_window_ui import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, parent):
        self.parent = parent

    def initialize(self):
        self.actionQuit.triggered.connect(self.close)

    def close(self):
        self.parent.close()