from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import Qt, QPen
from random import randint, randrange


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(321, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и жёлтые окружности"))
        self.pushButton.setText(_translate("MainWindow", "Click"))


class Circle(object):
    def __init__(self, color, coords, size):
        self.color = color
        self.coords = coords
        self.size = size

    def draw(self, qp):
        qp.setBrush(Qt.NoBrush)
        qp.setPen(QPen(self.color, 3, Qt.SolidLine))
        qp.drawEllipse(*self.coords, self.size, self.size)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        size = randint(1, 100)
        red, green, blue = randint(0, 255), randint(0, 255), randint(0, 255)
        self.circles.append(Circle(QColor(red, green, blue),
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
