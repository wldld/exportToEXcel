#!/bin/bash/python

import mysql.connector
from PyQt5.QtWidgets import QMainWindow
from mainWindow import *
from functools import partial


class MainWindowEdit(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        sql = self.text_Input.toPlainText()
        print(sql)
        self.btn_queary.clicked.connect(self.print_message)

    def testPrint(self):
        print("get 到了")

    def print_message(self):
        heading, result = queary(self.sql)
        message = "".join(result)
        self.text_message_print.setText(message)


def queary(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="test"
    )
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchall()
    headList = mycursor.description
    for index in range(len(headList)):
        if index == 0:
            heading = [headList[index][0], ]
        else:
            heading.append(headList[index][0])
    return heading, result


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowEdit()
    window.show()
    sys.exit(app.exec_())
    # sql = "select * from student"
    # heading, result = queary(sql)
    # print(result)
