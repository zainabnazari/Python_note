# file name: row_pandas.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)
print(data.loc["DE"])
'''
output

Country      Germany
Cases         175223
Dead            7933
Recovered     151700
Name: DE, dtype: object

'''
