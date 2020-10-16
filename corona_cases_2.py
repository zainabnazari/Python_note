#file name: corona_cases_2.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)
print(data)
'''
output:

    Country   Cases   Dead  Recovered
IR     Iran  116635   6902      91836
CN    China   82933   4633      78209
IT    Italy  223885  31610     120205
DE  Germany  175223   7933     151700

'''
