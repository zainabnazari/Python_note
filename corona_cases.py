#file name: corona_cases.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv")
print(data)
'''
output:

  Unnamed: 0  Country   Cases   Dead  Recovered
0         IR     Iran  116635   6902      91836
1         CN    China   82933   4633      78209
2         IT    Italy  223885  31610     120205
3         DE  Germany  175223   7933     151700

'''
