#file name: loc.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)
print("Or: ", data.loc[["DE", "IR"]][["Recovered"]])
