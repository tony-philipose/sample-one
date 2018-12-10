#import values from csv to mysql table in python
# datatypes--> values (%d->int(255),%s->varchar(255),%f->decimal(25,4))
# 
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json
import csv

con = pymysql.connect(host='localhost', user='root', password='Assyst@123', db='pysample')
cursor = con.cursor()

file = "/home/local/ASSYST-COC/tony.p/Downloads/100 Sales Records.csv"
df1 = pd.read_csv(file)
df1

csv_data = pd.read_csv('/home/local/ASSYST-COC/tony.p/Downloads/100 Sales Records.csv')
csv_data

pd.read_csv(file).dtypes

data3 = df1[['Region','Country','Total Revenue']]
data3

for row in data3.iterrows():
    list = row[1].values
    print(list)
    cursor.execute("insert into csv100 (`Region`,`Country`,`Total Revenue`) values (%s, %s, %s)", tuple(list))

con.commit()
