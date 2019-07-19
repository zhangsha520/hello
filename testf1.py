import sys
import PyQt5
from PyQt5 import QtWidgets


class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QtWidgets.QAction("关闭软件", self, triggered=self.trigg)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.trigg)
        self.menubar = QtWidgets.QMenu()
        self.menubar.addMenu('关闭软件')
        self.menubar.addAction(exitAction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

    def trigg(self):
        print("\ntigger")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()