import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QPoint
from random import randint


class Example(QMainWindow):
    def __init__(self):
        self.r = True
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setWindowTitle('Рисование кругов')

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.r:
            return
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(0, 155)
        qp.drawEllipse(QPoint(155, 207), r, r)

    def paint(self):
        self.r = False
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())