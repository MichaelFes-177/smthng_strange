import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for _ in range(10):
            diameter = random.randint(10, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
