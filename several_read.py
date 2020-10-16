# file name: several_read.py
import glob as gl
file_names=gl.glob("dpc-covid19-ita-province-*")
print(file_names)
for name in file_names:
    print(name)
    print(open(name,"r").read())
'''
part of the output:
['dpc-covid19-ita-province-20200312.csv', 'dpc-covid19-ita-province-latest.csv', 'dpc-covid19-ita-province-20200311.csv']
dpc-covid19-ita-province-20200312.csv
data,stato,codice_regione,denominazione_regione,codice_provincia,denominazione_provincia,sigla_provincia,lat,long,totale_casi,note_it,note_en
2020-03-12T17:00:00,ITA,13,Abruzzo,069,Chieti,CH,42.35103167,14.16754574,20,,
2020-03-12T17:00:00,ITA,13,Abruzzo,066,L'Aquila,AQ,42.35122196,13.39843823,8,,
2020-03-12T17:00:00,ITA,13,Abruzzo,068,Pescara,PE,42.46458398,14.21364822,48,,
2020-03-12T17:00:00,ITA,13,Abruzzo,067,Teramo,TE,42.6589177,13.70439971,8,,
.
.
.
dpc-covid19-ita-province-latest.csv
data,stato,codice_regione,denominazione_regione,codice_provincia,denominazione_provincia,sigla_provincia,lat,long,totale_casi,note_it,note_en
2020-05-23T17:00:00,ITA,13,Abruzzo,069,Chieti,CH,42.35103167,14.16754574,817,,
2020-05-23T17:00:00,ITA,13,Abruzzo,066,L'Aquila,AQ,42.35122196,13.39843823,246,,
2020-05-23T17:00:00,ITA,13,Abruzzo,068,Pescara,PE,42.46458398,14.21364822,1508,,

.
.
.
dpc-covid19-ita-province-20200311.csv
data,stato,codice_regione,denominazione_regione,codice_provincia,denominazione_provincia,sigla_provincia,lat,long,totale_casi,note_it,note_en
2020-03-11T17:00:00,ITA,13,Abruzzo,069,Chieti,CH,42.35103167,14.16754574,9,,
2020-03-11T17:00:00,ITA,13,Abruzzo,066,L'Aquila,AQ,42.35122196,13.39843823,6,,
2020-03-11T17:00:00,ITA,13,Abruzzo,068,Pescara,PE,42.46458398,14.21364822,18,,
.
.
.

'''
