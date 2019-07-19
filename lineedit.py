"""lineedit"""

import sys

from PyQt5 import QtWidgets, QtGui, QtCore


class Lineedit(QtWidgets.QWidget):
    """line edit"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 330, 300)
        self.line_edit = QtWidgets.QLineEdit("", self)
        self.m_model = QtGui.QStandardItemModel(0, 1, self)
        self.m_completer = QtWidgets.QCompleter(self.m_model, self)
        self.line_edit.setCompleter(self.m_completer)
        self.line_edit.textChanged.connect(self.on_line_edit_textChanged)
        self.m_completer.activated[str].connect(self.onEmailChoosed)
        self.show()

    def onEmailChoosed(self, text):
        self.line_edit.setText(text)

    def on_line_edit_textChanged(self, text):
        print(" in on_line_edit_textChanged")
        if '@' in self.line_edit.text():
            return

        emaillist = ["@163.com", "@qq.com", "@gmail.com", "@live.com", "@126.com", "@139.com"]
        self.m_model.removeRows(0, self.m_model.rowCount())
        for i in range(0, len(emaillist)):
            self.m_model.insertRow(0)
            self.m_model.setData(self.m_model.index(0, 0), text + emaillist[i])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Lineedit()
    sys.exit(app.exec_())
