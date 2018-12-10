# python pgm for read a csv file and print it
import pandas as pd
df1 = pd.read_csv("https://s3.amazonaws.com/apache-zeppelin/tutorial/bank/bank.csv")
print(df1)
