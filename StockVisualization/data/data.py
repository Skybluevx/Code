"""
    数据源：
    Tushare大数据社区：https://tushare.pro/
"""
import sqlite3
import tushare


TOKEN = "59e9f1e90c209a64712527ef752795b9929028c07398611d69bf49e1"


class TakeData(object):

    def __init__(self):
        self.conn = sqlite3.connect("./data.db")
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()




if __name__ == '__main__':
    dat = TakeData()
