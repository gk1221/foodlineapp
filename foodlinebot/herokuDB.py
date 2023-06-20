import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a foodielinebotzxcv').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()


sql = '''CREATE TABLE foodsheet(
           country CHAR(5),
           catagory VARCHAR (20) NOT NULL,
           food_1 VARCHAR (50) NOT NULL,
           food_2 VARCHAR (50) NOT NULL,
           food_3 VARCHAR (50) NOT NULL,
           food_4 VARCHAR (50) NOT NULL,
           food_5 VARCHAR (50) NOT NULL
        );'''
cursor.execute("SELECT column_name FROM information_schema.columns where table_name='foodsheet'")


for i in cursor.fetchall():
    print(i)