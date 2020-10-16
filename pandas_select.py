# file name: pandas_select.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)
print(data["Cases"])
'''
output

IR    116635
CN     82933
IT    223885
DE    175223
Name: Cases, dtype: int64

'''
print(data.Cases) #alternative way to access a column

'''
output

IR    116635
CN     82933
IT    223885
DE    175223
Name: Cases, dtype: int64

'''
