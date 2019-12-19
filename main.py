from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import Qt, QPen
from random import randint, randrange


class Circle(object):
    def __init__(self, color, coords, size):
        self.color = color
        self.coords = coords
        self.size = size

    def draw(self, qp):
        qp.setBrush(Qt.NoBrush)
        qp.setPen(QPen(self.color, 3, Qt.SolidLine))
        qp.drawEllipse(*self.coords, self.size, self.size)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUi()

    def initUi(self):
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        size = randint(1, 100)
        self.circles.append(Circle(QColor(255, 255, 0),
                                   (randrange(0, width - size), randrange(0, height - size)),
                                   size))

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        for circle in self.circles:
            circle.draw(self.qp)
        self.qp.end()
        self.update()


def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
