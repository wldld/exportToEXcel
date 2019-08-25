#!/bin/bash/python

import mysql.connector
import writerToExcel


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


def selectSql(sql):
    pass


if __name__ == "__main__":
    sql = "select * from store"
    heading, result = queary(sql)
    writerToExcel.writeExcel('G:\\temp\\store1.xlsx', heading, result)
