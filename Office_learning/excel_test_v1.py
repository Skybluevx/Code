import xlrd as xl
import xlwt
import openpyxl
import pandas as pd


# 打开文件
# data = openpyxl.load_workbook("E:\\ab我的很多东西\能动1601班\尺寸表.xlsx")
data2 = pd.read_
# 获取表名
# sheet_name = data.sheetnames
# 打开表格
sheet = data2["Sheet1"]

# 获取excel正在value显示的表
activesheet = data2.active

for row_cell in sheet["A3":"F3"]:
    for cell in row_cell:
        print(cell.value)
