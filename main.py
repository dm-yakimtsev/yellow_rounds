import sys
from random import randint
from ui import Ui_Form
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class YellowRounds(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.make_draw = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.make_draw:
            qp = QPainter()
            qp.begin(self)
            x, y = [randint(10, 200) for i in range(2)]
            diam = randint(10, 200)
            w, h = [diam for i in range(2)]
            pen = QPen()
            pen.setWidth(5)
            pen.setColor(QColor(*[randint(0, 255) for _ in range(3)]))
            qp.setPen(pen)
            qp.drawEllipse(x, y, w, h)
            qp.end()
            self.make_draw = False

    def draw(self):
        self.make_draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowRounds()
    ex.show()
    sys.exit(app.exec())
