"""
    数据源：
    Tushare大数据社区：https://tushare.pro/
"""
import sys
import inspect
import sqlite3
import tushare
import pandas as pd


TOKEN = "59e9f1e90c209a64712527ef752795b9929028c07398611d69bf49e1"


class TakeData(object):

    def __init__(self):
        self.conn = sqlite3.connect("./database.db")
        self.cur = self.conn.cursor()
        # self.conn.execute("CREATE TABLE test(key key )")
        self.ts = tushare.pro_api(token=TOKEN)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def save2database(self, dataframe, table_name, if_exists="append"):
        dataframe.to_sql(table_name, con=self.conn, if_exists=if_exists)

    def stock_basic(self):
        """
        股票列表
        :return:
        """
        data = self.ts.stock_basic(exchange="",
                                   list_status='L',
                                   fields='ts_code,symbol,name,area,industry,list_date')
        # print(data)
        self.save2database(dataframe=data, table_name="stock_basic")

    def trade_cal(self):
        """
        交易日历
        :return:
        """
        data = self.ts.trade_cal(exchange='',
                                 start_date='20190101',
                                 end_date='20201231')
        self.save2database(dataframe=data, table_name="trade_cal")

    def namechange(self):
        """
        股票曾用名
        :return:
        """
        data = self.ts.namechange(ts_code='600848.SH', fields='ts_code,name,start_date,end_date,change_reason')
        self.save2database(dataframe=data, table_name="namechange")

    def hs_const(self):
        """
        沪深股通成分股
        :return:
        """
        data = self.ts.hs_const(hs_type="SH")
        self.save2database(data, "hs_const")

    def stock_company(self):
        """
        上市公司基本信息
        :return:
        """
        data = self.ts.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
        self.save2database(data, "stock_company")


if __name__ == '__main__':
    dat = TakeData()
    dat.trade_cal()
