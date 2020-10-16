#file name: vstack.py
import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
print(np.vstack((x,y)))
'''
output:

[[1 2 3]
 [4 5 6]]

'''
x1=np.array([[11],[12],[13]])
y1=np.array([[14],[15],[16]])
print(np.vstack((x1,y1)))
'''
output:

[[11]
 [12]
 [13]
 [14]
 [15]
 [16]]
 
'''