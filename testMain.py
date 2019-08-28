#!/bin/bash/python

from PyQt5.QtWidgets import QMainWindow
from mainWindow import *


class MainWindowEdit(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowEdit()
    window.show()
    sys.exit(app.exec_())
