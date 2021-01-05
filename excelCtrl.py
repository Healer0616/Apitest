# -*- coding: utf-8 -*- 
# @Time    : 2021/1/5 2:12 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : excelCtrl.py
# @Software: PyCharm

import xlrd
import json
from xlutils.copy import copy
from get_token import get_token

excelDir = "/Users/healer/Desktop/apicase.xls"
# 打开Excel文件    formatting_info 保持原样式
workBook = xlrd.open_workbook(excelDir, formatting_info=True)
sheets = workBook.sheet_names()
# print(sheets)
workSheet = workBook.sheet_by_name("Sheet1")

# 取数据 获取1行6列params
cellData = workSheet.cell_value(2, 6)
# print(cellData)
res = get_token(cellData)
print(res)

# 断言 if  assert
if res["status"] == 1:
    info = "pass"
else:
    info = "fail"

# 结果写入
# 文件不存在  创建Excel 写 -- xlwt
# 文件存在   另存写 新Excel -- xlutils
# 拷贝Excel对象
newWorkBook = copy(workBook)
# 拷贝Excel的sheet -- 下标
newSheet = newWorkBook.get_sheet(0)
# 写入数据info
newSheet.write(2, 9, info)
newSheet.write(2, 8, json.dumps(res))
# 保存Excel对象
newWorkBook.save("/Users/healer/Desktop/Code/Apitest/newExcel/saveapicase.xls")
