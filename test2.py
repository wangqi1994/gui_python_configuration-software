import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Foo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Foo, self).__init__(parent)
        self.setGeometry(QtCore.QRect(200, 100, 700, 600))
        self.paint = Paint()
        self.sizeHint()
        self.lay = QtWidgets.QVBoxLayout()
        self.lay.addWidget(self.paint)
        self.setLayout(self.lay)

class Paint(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Paint, self).__init__(parent)
        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setAutoFillBackground(True)
        self.r = QtCore.QRect(QtCore.QPoint(), QtCore.QSize(200, 300))
        self._factor = 1.0

    def paintEvent(self, event):
        self.r.moveCenter(self.rect().center())
        pen = QtGui.QPen()
        brush = QtGui.QBrush( QtCore.Qt.darkCyan, QtCore.Qt.Dense5Pattern)
        painter = QtGui.QPainter(self)
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        painter.translate(self.rect().center())
        painter.scale(self._factor, self._factor)
        painter.translate(-self.rect().center())

        painter.drawRect(self.r)

    def wheelEvent(self, event):
        self._factor *= 1.01**(event.angleDelta().y()/15.0)
        self.update()
        super(Paint, self).wheelEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Foo()
    w.show()
    sys.exit(app.exec_())