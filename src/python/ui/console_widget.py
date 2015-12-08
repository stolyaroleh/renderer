import os

from PyQt5.QtGui import QTextCursor, QColor
from ui_generated.console_widget_ui import Ui_ConsoleWidget

from threading import Thread
from time import sleep


class LoggingThread(Thread):
    def __init__(self, pipe, write):
        super().__init__()
        self.daemon = True
        self.pipe = pipe
        self.write = write

    def run(self):
        while True:
            self.write(self.drain_pipe())
            sleep(0.1)

    def drain_pipe(self):
        return os.read(self.pipe, 1024).decode()


class ConsoleWidget(Ui_ConsoleWidget):
    def __init__(self, out_pipe, normal_color, warning_color, error_color):
        self.normal_color = normal_color
        self.warning_color = warning_color
        self.error_color = error_color

        self.out_pipe = out_pipe

    def initialize(self):
        self.stdout_logger = LoggingThread(self.out_pipe, self.write)
        self.stdout_logger.start()

        self.clear_btn.clicked.connect(self.flush)

    def write(self, message):
        self.text_edit.setTextColor(self.normal_color)
        self.text_edit.insertPlainText(message)
        self.text_edit.moveCursor(QTextCursor.End)

    def warning(self, message):
        self.text_edit.setTextColor(self.warning_color)
        self.text_edit.insertPlainText(message)
        self.text_edit.moveCursor(QTextCursor.End)

    def error(self, message):
        self.text_edit.setTextColor(self.error_color)
        self.text_edit.insertPlainText(message)
        self.text_edit.moveCursor(QTextCursor.End)

    def flush(self):
        self.text_edit.clear()
