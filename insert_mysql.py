# insert into a mysql table in py

import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Assyst@123@localhost/assignments')

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
print(df)

d = pd.read_sql_query('SELECT * FROM user', engine)
print(d)

df.to_sql('user', con=engine, if_exists='append',index=False,chunksize=1)

d = pd.read_sql_query('SELECT * FROM user', engine)
print(d)
