# file name: pandas_column.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)
data["Serious critical"]=[2294, 8, 762, 1166]
print(data)
'''
output:

    Country   Cases   Dead  Recovered  Serious critical
IR     Iran  116635   6902      91836              2294
CN    China   82933   4633      78209                 8
IT    Italy  223885  31610     120205               762
DE  Germany  175223   7933     151700              1166

'''
data["Active cases"]=data["Cases"]-(data["Dead"]+data["Recovered"])

print(data)

'''
output:
    Country   Cases   Dead  Recovered  Serious critical
IR     Iran  116635   6902      91836              2294
CN    China   82933   4633      78209                 8
IT    Italy  223885  31610     120205               762
DE  Germany  175223   7933     151700              1166
    Country   Cases   Dead  Recovered  Serious critical  Active cases
IR     Iran  116635   6902      91836              2294         17897
CN    China   82933   4633      78209                 8            91
IT    Italy  223885  31610     120205               762         72070
DE  Germany  175223   7933     151700              1166         15590
'''
