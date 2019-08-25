#!/bin/bash/python

import xlsxwriter


def writeExcel(fileName, heading, result):
    work = xlsxwriter.Workbook(fileName)
    worksheet = work.add_worksheet("sheet1")
    worksheet.write_row('A1', heading)
    for index in range(len(result)):
        worksheet.write_row('A'+str(index+2),result[index])
    work.close()
