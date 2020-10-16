#file name: pandas_multiple_select.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)

# select single column with Pandas dataframe

print(data[["Cases"]])
'''
output:
     Cases
IR  116635
CN   82933
IT  223885
DE  175223

'''
# Select multiple columns with Pandas dataframe
print(data[["Cases", "Recovered"]])

'''
output

     Cases  Recovered
IR  116635      91836
CN   82933      78209
IT  223885     120205
DE  175223     151700

'''
