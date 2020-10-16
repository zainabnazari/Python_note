# name of file: read2.py
# loading data (read data in) with loadtxt
import numpy as np
newarray=np.loadtxt('ourdata.txt')
for x in newarray:
    print(x**2)
