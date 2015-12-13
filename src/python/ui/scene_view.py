from ui.gl_widget import GLWidget
from ui_generated.scene_view_ui import Ui_SceneViewWidget
from PyQt5 import QtWidgets


class SceneViewWidget(QtWidgets.QWidget):
    def __init__(self, parent, scene):
        super().__init__(parent)
        self.parent = parent

        self.ui = Ui_SceneViewWidget()
        self.ui.setupUi(self)
        self.gl_widget = GLWidget(self)
        self.ui.gl_layout.addWidget(self.gl_widget)

        self.scene = scene
        self.initialize()

    def initialize(self):
        self.ui.tx.valueChanged.connect(self.update_transform)
        self.ui.ty.valueChanged.connect(self.update_transform)
        self.ui.tz.valueChanged.connect(self.update_transform)
        self.ui.rx.valueChanged.connect(self.update_transform)
        self.ui.ry.valueChanged.connect(self.update_transform)
        self.ui.rz.valueChanged.connect(self.update_transform)

        self.ui.lposx.valueChanged.connect(self.update_light)
        self.ui.lposy.valueChanged.connect(self.update_light)
        self.ui.lposz.valueChanged.connect(self.update_light)
        self.ui.intensity.valueChanged.connect(self.update_light)

        self.ui.meshes_list.itemClicked.connect(self.update_transform_fields)
        self.ui.delete_btn.clicked.connect(self.delete_mesh)

        self.update_light()

    def update_transform_fields(self):
        mesh = self.get_selected_mesh()
        if not mesh:
            return

        self.ui.tx.setValue(mesh.transform.tx)
        self.ui.ty.setValue(mesh.transform.ty)
        self.ui.tz.setValue(mesh.transform.tz)
        self.ui.rx.setValue(mesh.transform.rx)
        self.ui.ry.setValue(mesh.transform.ry)
        self.ui.rz.setValue(mesh.transform.rz)

    def update_transform(self):
        mesh = self.get_selected_mesh()
        if not mesh:
            return

        mesh.transform.tx = self.ui.tx.value()
        mesh.transform.ty = self.ui.ty.value()
        mesh.transform.tz = self.ui.tz.value()
        mesh.transform.rx = self.ui.rx.value()
        mesh.transform.ry = self.ui.ry.value()
        mesh.transform.rz = self.ui.rz.value()

        self.gl_widget.update()

    def update_list(self):
        self.ui.meshes_list.clear()
        for mesh_name in self.scene.meshes.keys():
            self.ui.meshes_list.addItem(mesh_name)

    def get_selected_mesh(self):
        selection = self.ui.meshes_list.selectedItems()
        if not selection:
            return None

        return self.scene.meshes[selection[0].text()]

    def delete_mesh(self):
        selection = self.ui.meshes_list.selectedItems()
        if not selection:
            return

        del self.scene.meshes[selection[0].text()]
        self.refresh()

    def update_light(self):
        self.gl_widget.light_pos = (self.ui.lposx.value(),
                                    self.ui.lposy.value(),
                                    self.ui.lposz.value())
        self.gl_widget.light_intensity = self.ui.intensity.value()
        self.gl_widget.update()

    def refresh(self):
        self.gl_widget.schedule_buffer_update(self.scene.meshes.values())
        self.update_light()
        self.update_list()
        self.gl_widget.update()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = SceneViewWidget(None)
    widget.show()
    sys.exit(app.exec_())
