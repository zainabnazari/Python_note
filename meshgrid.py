# file name: meshgrid.py
import numpy as np
x=[1,2,3,4]
y=[5,6,7]
XX, YY=np.meshgrid(x,y)
print("This is XX values:\n", XX) # \n will take us to the next line
print("This is YY values:\n", YY)
'''
output:
This is XX values:
 [[1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]]
This is YY values:
 [[5 5 5 5]
 [6 6 6 6]
 [7 7 7 7]]

'''
