#inserto into mysql from json file
#https://thepythonguru.com/inserting-rows/
#https://www.youtube.com/watch?v=WbW0rHCX2UU

import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json
from pandas.io.json import json_normalize

con = pymysql.connect(host='localhost', user='root', password='Assyst@123', db='pysample')
cursor = con.cursor()

file = "/home/local/ASSYST-COC/tony.p/Downloads/example_1.json"
json_data = open(file).read()
json_obj = json.loads(json_data)
print(json_obj)

for i, item in enumerate(json_obj):
   
    cursor.execute("insert into users (company,person,userscol) values (%s, %s, %s)",(item["person"],item["year"],item["company"]))

con.commit()
con.close()
