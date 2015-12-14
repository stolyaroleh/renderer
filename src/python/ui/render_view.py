from ui_generated.render_view_ui import Ui_RenderViewWidget
from PyQt5.QtGui import QPixmap


class RenderViewWidget(Ui_RenderViewWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def show(self, filename):
        self.parent.show()
        self.image.setPixmap(QPixmap(filename))