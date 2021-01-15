"""
    数据源：
    Tushare大数据社区：https://tushare.pro/
"""
import sqlite3
import tushare


TOKEN = ""


class BasicData(object):

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

    def stock_basic(self, is_hs="N", list_status="L", exchange=""):
        """
        股票列表
        :param is_hs:是否沪深港通标的，N否 H沪股通 S深股通
        :param list_status: 上市状态： L上市 D退市 P暂停上市，默认L
        :param exchange: 交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)
        :return:
        """
        data = self.ts.stock_basic(
            exchange=exchange,
            is_hs=is_hs,
            list_status=list_status,
            fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,'
                   'curr_type,list_status,list_date,delist_date,is_hs')
        # print(data)
        self.save2database(dataframe=data, table_name="stock_basic")

    def trade_cal(self, exchange="", start_data="20190101", end_data="20200101", is_open=""):
        """
        交易日历
        :param exchange:交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源,IB 银行间,XHKG 港交所
        :param start_data:开始日期
        :param end_data:结束日期
        :param is_open:是否交易 '0'休市 '1'交易
        :return:
        """
        data = self.ts.trade_cal(exchange=exchange,
                                 start_date=start_data,
                                 end_date=end_data)
        self.save2database(dataframe=data, table_name="trade_cal")

    def namechange(self, ts_code="600848.SH", start_data="", end_data=""):
        """
        股票曾用名
        :param ts_code:TS代码
        :param start_data:公告开始日期
        :param end_data:公告结束日期
        :return:
        """
        data = self.ts.namechange(
            ts_code='600848.SH',
            fields='ts_code,name,start_date,end_date,change_reason')
        self.save2database(dataframe=data, table_name="namechange")

    def hs_const(self, hs_type="SH", is_new=""):
        """
        沪深股通成分股
        :param hs_type: 类型SH沪股通SZ深股通
        :param is_new: 是否最新 1 是 0 否 (默认1)
        :return:
        """
        data = self.ts.hs_const(hs_type=hs_type)
        self.save2database(data, "hs_const")

    def stock_company(self, is_code="", exchange="SZSE"):
        """
        上市公司基本信息
        :param is_code: 股票代码
        :param exchange: 交易所代码 ，SSE上交所 SZSE深交所
        :return:
        """
        data = self.ts.stock_company(
            exchange=exchange,
            fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
        self.save2database(data, "stock_company")

    def new_share(self, start_date="20180901", end_date="20191018"):
        """
        新股上市数据
        :param start_date: 上网发行开始日期
        :param end_date: 上网发行结束日期
        :return:
        """
        data = self.ts.new_share(start_date=start_date,
                                 end_date=end_date)
        self.save2database(data, "new_share")


class MarketData(BasicData):

    def __init__(self):
        super().__init__()

    def daily(self, ts_code="000001.SZ,600000.SH", trade_code="", start_data="20180701", end_data="20180718"):
        """
        日线行情
        :param ts_code: 股票代码（支持多个股票同时提取，逗号分隔）
        :param trade_code: 交易日期（YYYYMMDD）
        :param start_data: 开始日期(YYYYMMDD)
        :param end_data: 结束日期(YYYYMMDD)
        :return:
        """
        data = self.ts.daily(ts_code=ts_code,
                             start_date=start_data,
                             end_date=end_data)
        self.save2database(data, "daily")


if __name__ == '__main__':
    # dat1 = BasicData()
    dat2 = MarketData()
    dat2.daily()
