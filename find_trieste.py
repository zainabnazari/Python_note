#file name: find_trieste.py
import pandas as pd
data=pd.read_csv("dpc-covid19-ita-province-latest.csv")
trieste_row=data[data.denominazione_provincia=="Trieste"]
print(trieste_row)
'''
output:
                   data stato  codice_regione  denominazione_regione  ...       long totale_casi note_it  note_en
34  2020-05-23T17:00:00   ITA               6  Friuli Venezia Giulia  ...  13.768136        1372     NaN      NaN

[1 rows x 12 columns]
'''
# to find out the totale_casi of the trieste we can do the following:
print(trieste_row[["totale_casi"]])
'''
output:

    totale_casi
34         1372
'''
