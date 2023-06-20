import os
import psycopg2
from abc import ABC


class actdata(ABC):
    def __init__(self):
        # 本地用
        DATABASE_URL = os.popen(
            "heroku config:get DATABASE_URL -a foodielinebotzxcv"
        ).read()[:-1]
        # 雲端用1
        # DATABASE_URL = os.environ["DATABASE_URL"]
        # self.conn = psycopg2.connect(DATABASE_URL, sslmode="require")

        # 連接本地的資料庫
        self.conn = psycopg2.connect(
            database="linebot",
            user="postgres",
            password="zxcv125628",
            host="localhost",
            port="5432",
        )

        self.cursor = self.conn.cursor()

    def select(self):
        print("----- finding..")
        postgres_select_query = f"""SELECT * FROM roombot_diarywrite1"""

        self.cursor.execute(postgres_select_query)
        text = list(self.cursor.fetchall())
        """
        for i in self.cursor.fetchall():
            text += i[0] + " " + i[1] + "  " + i[2] + "\n"
        """
        print("----- success")
        return text

    def insert(self, row_list):
        postgres_update_query = (
            f"""INSERT INTO roombot_diarywrite1 VALUES (%s,%s,%s)"""
        )
        self.cursor.execute(postgres_update_query, row_list)
        self.conn.commit()

        return f"{self.cursor.rowcount} row inserted!!"

    def stock(self, stock_list):

        postgres_update_query = (
            f"""INSERT INTO foodlinebot_StockRecord (item, inout, price,count,earnper, note) 
            VALUES (%s,%s,%s,%s,%s, %s)"""
        )

        '''
        else:
            postgres_update_query = (
                f"""INSERT INTO foodlinebot_StockRecord (item, inout, price,count, note) 
                VALUES (%s,%s,%s,%s,%s)"""
            )'''

        self.cursor.execute(postgres_update_query, stock_list)
        self.conn.commit()

        return f"{self.cursor.rowcount} row inserted!!"

    def stock_select(self, item=None):
        if item:
            postgres_update_query = (
                "SELECT * FROM foodlinebot_StockRecord WHERE item={}".format(
                    item)
            )
        else:
            postgres_update_query = (
                "SELECT * FROM foodlinebot_StockRecord "
            )
        self.cursor.execute(postgres_update_query)

        text = list(self.cursor.fetchall())

        return text
