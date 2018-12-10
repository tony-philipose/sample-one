#read data from mysql table in python
import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Assyst@123@localhost/assignments')

df = pd.read_sql_query('SELECT * FROM employee', engine)
print(df)
