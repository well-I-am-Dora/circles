import io

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
import sys
from random import randint

YELLOW = QColor(255, 255, 0)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circ(qp)
            qp.end()

    def draw(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_circ(self, qp):
        qp.setBrush(YELLOW)
        radius = randint(0, min(self.width(), self.height())//2)
        x, y = randint(1, self.width() - radius), randint(1, self.height() - radius)
        qp.drawEllipse(x, y, radius * 2, radius * 2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
