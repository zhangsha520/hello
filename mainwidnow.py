from PyQt5 import QtCore, QtWidgets, QtGui, QtSql


class test(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(test, self).__init__(parent)
        self.resize(600, 250)
        toolbar = self.addToolBar("aa")
        hbox = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QWidget()
        box = QtWidgets.QCheckBox()
        box.setChecked(True)
        button = QtWidgets.QPushButton("test")
        hbox.addWidget(box)
        hbox.addWidget(button)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setAlignment(QtCore.Qt.AlignCenter)
        widget.setLayout(hbox)
        act = toolbar.addWidget(widget)
        act.setVisible(True)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aa = test()
    aa.show()
    app.exit(app.exec_())