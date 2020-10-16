#file name: where.py

import numpy as np
mylist = np.array([9,1,4,2,-4,1,-6,-1,4])
mylistAbsolute = np.where(mylist < 0, -mylist, mylist)#all the negative values are turned positive
print(mylistAbsolute)
"""
output:
[9 1 4 2 4 1 6 1 4]
"""