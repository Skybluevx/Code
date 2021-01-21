"""
    xlwings 的简单使用
"""
import xlwings as xw

app = xw.App(visible=True, add_book=False)
app.display_alerts = False
app.screen_updating = False

path = r"能动1601班就业情况汇总表.xlsx"
path2 = r"./text.xlsx"

wb = app.books.open(path)
wb.save()
wb.close()
app.quit()
