"""文件系统"""
import sys
from PyQt5 import QtWidgets

class App():
    """app"""
    def __init__(self):
        self.my_model = QtWidgets.QFileSystemModel()
        self.my_model.setRootPath("/")
        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.my_model)
        self.tree.setSortingEnabled(True)
        self.tree.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tree.resize(640, 480)

    def show(self):
        self.tree.show()

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    app = App()  # create an application object.
    app.show()
    sys.exit(application.exec_())