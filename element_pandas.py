#file name: element_pandas.py
import pandas as pd
data = pd.read_csv("2020-05-15_Corona_Cases.csv", index_col=0)
print("One way:", data.loc["DE", "Recovered"])
# alternativly:
print("The other way: ", data["Recovered"].loc["DE"])
# or
print("Or: ", data.loc["DE"]["Recovered"])
'''
One way: 151700
The other way:  151700
Or:  151700
'''
