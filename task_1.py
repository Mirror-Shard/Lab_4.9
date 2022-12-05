#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
Результат вычисления должен отображаться в метке.
"""
import sys
from PySide2 import QtCore, QtGui, QtWidgets


def add(label, a, b):
    a, b = float(a), float(b)
    label.setText(str(a + b))


def sub(label, a, b):
    a, b = float(a), float(b)
    label.setText(str(a - b))


def mul(label, a, b):
    a, b = float(a), float(b)
    label.setText(str(a * b))


def div(label, a, b):
    a, b = float(a), float(b)
    label.setText(str(a / b))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(400, 400, 20, 220)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.atextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.atextbox.move(25, 5)
        self.atextbox.resize(100, 20)

        self.btextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.btextbox.move(25, 30)
        self.btextbox.resize(100, 20)

        self.abutton = QtWidgets.QPushButton(self.centralwidget)
        self.abutton.setText("+")
        self.abutton.move(28, 60)

        self.sbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sbutton.setText("-")
        self.sbutton.move(28, 90)

        self.mbutton = QtWidgets.QPushButton(self.centralwidget)
        self.mbutton.setText("*")
        self.mbutton.move(28, 120)

        self.dbutton = QtWidgets.QPushButton(self.centralwidget)
        self.dbutton.setText("/")
        self.dbutton.move(28, 150)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(55, 1, 450, 390))
        self.label.setText("Ответ")

        MainWindow.setCentralWidget(self.centralwidget)
        self.abutton.clicked.connect(lambda: add(self.label, self.atextbox.text(), self.btextbox.text()))
        self.sbutton.clicked.connect(lambda: sub(self.label, self.atextbox.text(), self.btextbox.text()))
        self.mbutton.clicked.connect(lambda: mul(self.label, self.atextbox.text(), self.btextbox.text()))
        self.dbutton.clicked.connect(lambda: div(self.label, self.atextbox.text(), self.btextbox.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
