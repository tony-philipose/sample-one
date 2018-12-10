# insert into a mysql table in py

import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Assyst@123@localhost/assignments')

data = pd.DataFrame({'job' : ['hr', 'devo'],'mgr' : [1,2],'hire date' : ['01-02-2001', '02-04-2004'],'salary' : [444,4441],'dept id' : [3,1],'ename' : ['py1', 'py2']})

data.to_sql('employee', con=engine, if_exists='append',index=False,chunksize=1)

d = pd.read_sql_query('SELECT * FROM employee', engine)
print(d)
