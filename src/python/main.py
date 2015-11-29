import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qdarkstyle import load_stylesheet_pyqt5
from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    if '--dark' in sys.argv:
        stylesheet = load_stylesheet_pyqt5()
        window.setStyleSheet(stylesheet)

    main_ui = MainWindow(window)
    main_ui.setupUi(window)
    main_ui.initialize()

    window.show()
    sys.exit(app.exec_())
