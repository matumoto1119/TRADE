import psycopg2
import yfinance as yf
import json
import pandas_datareader.data as pdr
import pandas as pd
import datetime
from datetime import timedelta
from io import StringIO

import matplotlib.pyplot as plt
import pprint
import timeit
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

connection_config = {
    "user": "postgres",
    "password": "Matu0048",
    "host": "localhost",
    "database": "stock",
}
# conn = psycopg2.connect("dbname=stock user=postgres password=Matu0048")
engine = create_engine(
    "postgresql://{user}:{password}@{host}/{database}".format(**connection_config),
    isolation_level="AUTOCOMMIT",
)


# with conn:
#     with conn.cursor() as cur:
# cur.execute("select max(日付) from price")
# c = cur.fetchone()

# conn.commit
with engine.connect() as conn:
    sql = """select * from price where コード=1333"""
    df = pd.read_sql_query(sql=text(sql), con=conn)
    print("9999" in df.nunique())


# start = c[0] + timedelta(days=1)
# end = datetime.date.today()

# df_data = pd.read_excel(
#     r"D:\Users\koudai\Documents\DATABASE\PostgreSQL\STOCK\data_j.xls"
# )

# yf.pdr_override()  # データ取得をdrからyfinanceへ変更

# for code in df_data["コード"]:
#     df = pdr.get_data_yahoo(f"{code}.T", start, end)
#     df["コード"] = code
#     df.reset_index(drop=False, inplace=True)
#     df.columns = ["日付", "始値", "高値", "安値", "終値", "調整後終値", "出来高", "コード"]
#     df.to_sql("price", con=engine, if_exists="append", index=False)
#     print(code)
