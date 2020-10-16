# file name: read_several_pandas.py
import glob
import pandas as pd

for i in glob.glob('dpc-covid19-ita-province-20200*'): # it will take all the files with the prefix before *
    data=pd.read_csv(i)
    print(data)
'''
output:
                    data stato  codice_regione denominazione_regione  ...       long totale_casi note_it  note_en
0    2020-03-12T17:00:00   ITA              13               Abruzzo  ...  14.167546          20     NaN      NaN
1    2020-03-12T17:00:00   ITA              13               Abruzzo  ...  13.398438           8     NaN      NaN
2    2020-03-12T17:00:00   ITA              13               Abruzzo  ...  14.213648          48     NaN      NaN
3    2020-03-12T17:00:00   ITA              13               Abruzzo  ...  13.704400           8     NaN      NaN
4    2020-03-12T17:00:00   ITA              13               Abruzzo  ...   0.000000           0     NaN      NaN
..                   ...   ...             ...                   ...  ...        ...         ...     ...      ...
123  2020-03-12T17:00:00   ITA               5                Veneto  ...  12.245074         279     NaN      NaN
124  2020-03-12T17:00:00   ITA               5                Veneto  ...  12.338452         205     NaN      NaN
125  2020-03-12T17:00:00   ITA               5                Veneto  ...  10.993527         150     NaN      NaN
126  2020-03-12T17:00:00   ITA               5                Veneto  ...  11.545971         122     NaN      NaN
127  2020-03-12T17:00:00   ITA               5                Veneto  ...   0.000000         128     NaN      NaN

[128 rows x 12 columns]
                    data stato  codice_regione denominazione_regione  ...       long totale_casi note_it  note_en
0    2020-03-11T17:00:00   ITA              13               Abruzzo  ...  14.167546           9     NaN      NaN
1    2020-03-11T17:00:00   ITA              13               Abruzzo  ...  13.398438           6     NaN      NaN
2    2020-03-11T17:00:00   ITA              13               Abruzzo  ...  14.213648          18     NaN      NaN
3    2020-03-11T17:00:00   ITA              13               Abruzzo  ...  13.704400           5     NaN      NaN
4    2020-03-11T17:00:00   ITA              13               Abruzzo  ...   0.000000           0     NaN      NaN
..                   ...   ...             ...                   ...  ...        ...         ...     ...      ...
123  2020-03-11T17:00:00   ITA               5                Veneto  ...  12.245074         185     NaN      NaN
124  2020-03-11T17:00:00   ITA               5                Veneto  ...  12.338452         179     NaN      NaN
125  2020-03-11T17:00:00   ITA               5                Veneto  ...  10.993527         110     NaN      NaN
126  2020-03-11T17:00:00   ITA               5                Veneto  ...  11.545971          92     NaN      NaN
127  2020-03-11T17:00:00   ITA               5                Veneto  ...   0.000000          40     NaN      NaN

[128 rows x 12 columns]
'''
