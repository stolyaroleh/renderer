import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    main_ui = MainWindow(window)
    main_ui.setupUi(window)
    main_ui.initialize()
    window.show()

    sys.exit(app.exec_())
