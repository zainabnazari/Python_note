# file name: save.py
# this is a way to save data using numpy
import numpy as np
x=np.array([[1,2,3,4,5],[1,2,3,4,5]])
np.savetxt('ourdata.txt',x) # it also works with .dat files.
