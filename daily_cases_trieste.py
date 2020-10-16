# daily_cases_trieste.py
import matplotlib.pyplot as plt
import glob
import pandas as pd
import git

g = git.cmd.Git("./COVID-19") # this is to tell that ./COVID-19 is a git repository, and that the git commands that we apply on "g"
 #should be applied on that repository.
#This only works because we have already git cloned the repository to our local directory.
g.pull() # this is how to git pull the new data from the remote repository to our local repository.
list1=[]
# to read the csv files
for i in glob.glob('./COVID-19/dati-province/dpc-covid19-ita-province-20200*'):
   try: # this "try" and "except" is a check whether the files are all doing well!
   # (if some file is broken it won't be included in our list and the program continues )
       data=pd.read_csv(i, index_col="denominazione_provincia", parse_dates=True)
       store=data.loc["Trieste"][["totale_casi","data"]]
       list1+=[store]
   except:
       print("some error in file", i, "please fix it!")
list1=sorted(list1,key=lambda item:item['data'])
dlist=[]
clist=[]
for item in list1:
    dlist+=[item["data"]]
    clist+=[item['totale_casi']]
daily_new_cases=[]
for x in range(len(clist)-1):
    daily_new_cases+=[clist[x+1]-clist[x]]
# below we get rid of negative values for the new daily cases by setting it to the previous value of the previous day.
# This should have not been done as it basically ruin the actual data. We made it just to make the data look good for the moment.
for n, v in enumerate(daily_new_cases):
    if v<0:
        daily_new_cases[n]=daily_new_cases[n-1]
nlist=dlist[::10]
date=[]
for x in nlist:
    y=x.split("T")
    s=y[0].split("2020-")
    date+=[s[1]]
plt.bar(x=range(len(dlist)-1), height=daily_new_cases, color='grey')
dindex=list(range(len(dlist)))[::10]
plt.title("COVID-19, Trieste-2020", fontsize=15
)
plt.xlabel('Date: Month-Day')
plt.xticks(dindex,date, rotation=25)
plt.ylabel("New Cases")
plt.show()
