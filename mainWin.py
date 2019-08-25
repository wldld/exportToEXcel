#!/bin/bash/python

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("hello")
window.resize(500,500)
window.move(500,500)
label = QLabel(window)
label.setText("handsome boy is here")
label.setWindowTitle("world")
label.move(100, 50)
window.show()
sys.exit(app.exec_())
