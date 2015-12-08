import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qdarkstyle import load_stylesheet_pyqt5
from ui.main_window import MainWindow


class FDWrapper:
    def __init__(self, fd):
        self.fd = fd

    def write(self, message):
        os.write(self.fd, message.encode())

    def flush(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    if '--dark' in sys.argv:
        stylesheet = load_stylesheet_pyqt5()
        window.setStyleSheet(stylesheet)

    # capture file descriptors, responsible for stderr and stdout and pass them to console for logging
    stdout_descriptor = sys.stdout.fileno()
    new_stdout, in_write = os.pipe()
    os.dup2(in_write, stdout_descriptor)
    sys.stdout = FDWrapper(in_write)

    main_ui = MainWindow(window, new_stdout)
    main_ui.setupUi(window)
    main_ui.initialize()

    print('Initializing...')

    window.show()
    sys.exit(app.exec_())
