# file name: ravel.py
import numpy as np
x=[[1,2],[3,4]]
print("Initially it looks:", x)
# when it gets flattened:
y=np.ravel(x)
print("Flattened version looks:", y)
'''
output:
Initially it looks: [[1, 2], [3, 4]]
Flattened version looks: [1 2 3 4]
'''
