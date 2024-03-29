"""code editor"""

import sys

from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QTextEdit, QApplication
from PyQt5.QtGui import QFont, QColor, QTextFormat, QPainter
from PyQt5.QtCore import QRect, Qt


class QCodeEditor(QPlainTextEdit):

    class NumberBar(QWidget):
        def __init__(self, editor):
            QWidget.__init__(self, editor)

            self.editor = editor
            self.editor.blockCountChanged.connect(self.updateWidth)
            self.editor.updateRequest.connect(self.updateContents)
            self.font = QFont()
            self.numberBarColor = QColor("#e8e8e8")

        def paintEvent(self, event):

            painter = QPainter(self)
            painter.fillRect(event.rect(), self.numberBarColor)

            block = self.editor.firstVisibleBlock()
        
            while block.isValid():
                blockNumber = block.blockNumber()
                block_top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()
                if blockNumber == self.editor.textCursor().blockNumber():
                    self.font.setBold(True)
                    painter.setPen(QColor("#000000"))
                else:
                    self.font.setBold(False)
                    painter.setPen(QColor("#717171"))

                paint_rect = QRect(0, block_top, self.width(), self.editor.fontMetrics().height())
                painter.drawText(paint_rect, Qt.AlignCenter, str(blockNumber+1))

                block = block.next()
                
        def getWidth(self):  
            count = self.editor.blockCount()
            if 0 <= count < 99999:
                width = self.fontMetrics().width('99999') 
            else:
                width = self.fontMetrics().width(str(count))
            return width      

        def updateWidth(self):
            width = self.getWidth()
            self.editor.setViewportMargins(width, 0, 0, 0)
        
        def updateContents(self, rect, dy):
            if dy:
                self.scroll(0, dy)
            else:
                self.update(0, rect.y(), self.width(), rect.height())
            if rect.contains(self.editor.viewport().rect()):   
                fontSize = self.editor.currentCharFormat().font().pointSize()
                self.font.setPointSize(fontSize)
                self.font.setStyle(QFont.StyleNormal)
                self.updateWidth()

    def __init__(self):
        super(QCodeEditor, self).__init__()
        self.setWindowTitle('微信公众号：学点编程吧--带行号和颜色的文本框')

        self.setFont(QFont("Ubuntu Mono", 12))
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.number_bar = self.NumberBar(self)
        self.currentLineNumber = None
        self.cursorPositionChanged.connect(self.highligtCurrentLine)    
        self.setViewportMargins(40, 0, 0, 0)
        self.highligtCurrentLine()
        self.show()

    def resizeEvent(self, *e):
        cr = self.contentsRect()
        rec = QRect(cr.left(), cr.top(), self.number_bar.getWidth(), cr.height())
        self.number_bar.setGeometry(rec)

    def highligtCurrentLine(self):
        newCurrentLineNumber = self.textCursor().blockNumber()
        if newCurrentLineNumber != self.currentLineNumber:
            lineColor = QColor(Qt.yellow).lighter(160)
            self.currentLineNumber = newCurrentLineNumber
            hi_selection = QTextEdit.ExtraSelection() 
            hi_selection.format.setBackground(lineColor)
            hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            hi_selection.cursor = self.textCursor()
            hi_selection.cursor.clearSelection() 
            self.setExtraSelections([hi_selection])


# class Editor(QWidget):
#     """line edit"""
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setGeometry(300, 300, 330, 300)
#         self.editor = QCodeEditor()
#         self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QCodeEditor()
    sys.exit(app.exec_())