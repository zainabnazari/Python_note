# file name: ravel2.py
import numpy as np
x=np.array([[1,2],[3,4]])
print("Initially looks: ", x)
print("Flattened version looks: ", x.ravel())

'''
output:
Initially looks:  [[1 2]
 [3 4]]
Flattened version looks:  [1 2 3 4]
'''
