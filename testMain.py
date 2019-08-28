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
        self.str_input = ""
        self.btn_queary.clicked.connect(self.print_message)

    def testPrint(self):
        print("get 到了")

    def print_message(self):
        self.text_message_print.setPlainText("")
        try:
            self.str_input = self.text_Input.toPlainText().strip()
            if self.str_input == '':
                self.text_message_print.setPlainText("请输入sql")
            else:
                result = queary_sql(self.str_input)
                self.text_message_print.setPlainText(str(result))
                # self.text_message_print.setPlainText("queary OK")
        except mysql.connector.errors.InterfaceError:
            print("sql queary faild")
            self.text_message_print.setPlainText("sql queary faild")
        except mysql.connector.errors.ProgrammingError:
            print("sql queary faild")
            self.text_message_print.setPlainText("sql queary faild")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


def queary_sql(sql_str):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="test"
    )
    mycursor = mydb.cursor()
    mycursor.execute(sql_str)
    result = mycursor.fetchall()
    # headList = mycursor.description
    # for index in range(len(headList)):
    #     if index == 0:
    #         heading = [headList[index][0], ]
    #     else:
    #         heading.append(headList[index][0])
    # return heading, result
    return result


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowEdit()
    window.show()
    sys.exit(app.exec_())

    # result = queary_sql("select * from user")
    # print(str(result))
