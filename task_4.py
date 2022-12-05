#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QTextEdit,
)
from PySide2.QtCore import QByteArray


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.label = QTextEdit(self)
        self.button1 = QPushButton("Открыть файл", self)
        self.button2 = QPushButton("Сохранить файл", self)
        self.initialize()

    def initialize(self):
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 550, 500)
        self.label.move(0, 100)
        self.label.resize(550, 450)
        self.line_edit.move(230, 10)
        self.button1.move(250, 35)
        self.button1.clicked.connect(self.opening)
        self.button2.move(250, 65)
        self.button2.clicked.connect(self.save)

    def opening(self):
        if self.line_edit.text() == "":
            name = QFileDialog.getOpenFileName(self)
            with open(name[0], "r", encoding="utf-8") as f:
                data = f.read()
            self.label.setText(data)
        else:
            try:
                name = self.line_edit.text()
                with open(name, "r", encoding="utf-8") as f:
                    data = f.read()
                self.label.setText(data)
            except Exception as e:
                self.label.setText(f"Файл не найден {e}")

    def save(self):
        data = self.label.toPlainText()
        data = bytes(data, encoding="utf-8")
        data = QByteArray(data)
        name = self.line_edit.text()
        if name == "":
            QFileDialog.saveFileContent(data)
        else:
            QFileDialog.saveFileContent(data, name)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
