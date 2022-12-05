#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
Результат вычисления должен отображаться в метке.
"""
import sys
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(400, 400, 20, 280)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(55, 1, 450, 25))
        self.label.setText("Цвет")

        self.textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox.move(25, 30)
        self.textbox.resize(100, 20)

        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setStyleSheet("background: red;")
        self.btn_1.resize(100, 25)
        self.btn_1.move(25, 60)

        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setStyleSheet("background: orange;")
        self.btn_2.resize(100, 25)
        self.btn_2.move(25, 90)

        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setStyleSheet("background: yellow;")
        self.btn_3.resize(100, 25)
        self.btn_3.move(25, 120)

        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setStyleSheet("background: green;")
        self.btn_4.resize(100, 25)
        self.btn_4.move(25, 150)

        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setStyleSheet("background: skyblue;")
        self.btn_5.resize(100, 25)
        self.btn_5.move(25, 180)

        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setStyleSheet("background: blue;")
        self.btn_6.resize(100, 25)
        self.btn_6.move(25, 210)

        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setStyleSheet("background: purple;")
        self.btn_7.resize(100, 25)
        self.btn_7.move(25, 240)

        MainWindow.setCentralWidget(self.centralwidget)
        self.btn_1.clicked.connect(lambda: self.change("Красный", "#ff0000"))
        self.btn_2.clicked.connect(lambda: self.change("Оранжевый", "#ff7d00"))
        self.btn_3.clicked.connect(lambda: self.change("Жёлтый", "#ffff00"))
        self.btn_4.clicked.connect(lambda: self.change("Зелёный", "#00ff00"))
        self.btn_5.clicked.connect(lambda: self.change("Голубой", "#007dff"))
        self.btn_6.clicked.connect(lambda: self.change("Синий", "#0000ff"))
        self.btn_7.clicked.connect(lambda: self.change("Фиолетовый", "#7d00ff"))

    def change(self, color, code):
        self.label.setText(color)
        self.textbox.setText(code)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
