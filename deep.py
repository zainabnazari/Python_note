#file name: try.py
from copy import deepcopy
x=[[0,1],2,3]
y=deepcopy(x)
x[0][1]=9

print("x=",x)
print("y=",y)

'''
output:
x= [[0, 9], 2, 3]
y= [[0, 1], 2, 3]

'''
