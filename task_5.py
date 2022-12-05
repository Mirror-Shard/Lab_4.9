#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QRadioButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.button1 = QRadioButton("ВАСЯ", self)
        self.button2 = QRadioButton("ПЕТЯ", self)
        self.button3 = QRadioButton("МАША", self)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("My App")
        self.setGeometry(400, 400, 350, 100)
        self.label.move(175, 0)
        self.label.resize(300, 100)
        self.button1.move(10, 10)
        self.button2.move(10, 40)
        self.button3.move(10, 70)
        self.button1.clicked.connect(self.click)
        self.button2.clicked.connect(self.click)
        self.button3.clicked.connect(self.click)

    def click(self):
        if self.button1.isChecked():
            self.label.setText("+7(800)555-35-35")
        elif self.button2.isChecked():
            self.label.setText("+7(999)888-77-66")
        elif self.button3.isChecked():
            self.label.setText("+7(700)777-77-66")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
