#!/bin/bash/python

from PyQt5 import QtWidgets, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()


def title_changed(title):
    window.windowTitleChanged.disconnect()
    window.setWindowTitle("僚机-" + title)
    window.windowTitleChanged.connect(title_changed)


window.windowTitleChanged.connect(title_changed)
window.setWindowTitle("Hello xy")
window.resize(500, 400)
window.move(500, 400)
btn = QtWidgets.QPushButton(window)
btn.setText("click")


def btn_click():
    if window.windowTitle() == "僚机-Hello xy":
        window.setWindowTitle("Hello world")
    else:
        window.setWindowTitle("Hello xy")


btn.move(50, 60)
btn.clicked.connect(btn_click)
window.show()

sys.exit(app.exec_())
