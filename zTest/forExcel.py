# -*- coding: utf-8 -*- 
# @Time    : 2021/1/6 11:46 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : forExcel.py
# @Software: PyCharm


import xlrd
import re
import json
from xlutils.copy import copy
from zTest.get_token import get_token

excelPwd = "/Users/healer/Desktop/apicase.xls"

workBook = xlrd.open_workbook(excelPwd, formatting_info=True)
sheets = workBook.sheet_names()
# print(sheets)
workSheet = workBook.sheet_by_name("Sheet1")
row = workSheet.nrows  # 获取表总行数
col = workSheet.ncols  # 获取表列数


def get_actual_value():
    paramsList = []
    for r in range(2, row):
        for c in range(6, col - 3):
            # print(workSheet.cell_value(r, c))
            cellData = workSheet.cell_value(r, c)
            res = get_token(cellData)
            paramsList.append(res)
        # print(res)
    return paramsList


# print(get_actual_value())
# get_actual_value()

# 结果写入
# 文件不存在  创建Excel 写 -- xlwt
# 文件存在   另存写 新Excel -- xlutils
# 拷贝Excel对象
newWorkBook = copy(workBook)
# 拷贝Excel sheet 下标
newSheet = newWorkBook.get_sheet(0)
# 写入info数据
for i in range(2, row):
    for j in range(8, col - 1):
        # print(json.dumps(get_actual_value()))
        newSheet.write(i, j, json.dumps(get_actual_value()[i - 2], ensure_ascii=False))
        if re.search("TK", str(get_actual_value()[i - 2])):
            info = "pass"
        else:
            info = "fail"
        newSheet.write(i, j + 1, info)

# for i, item in enumerate(paramsList):
#     for j, val in enumerate(item):
#         newSheet.write()

# 保存Excel对象
newWorkBook.save("/Users/healer/Desktop/Code/Apitest/zTest/newExcel/forWrite.xls")
print("执行成功")
