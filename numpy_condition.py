#file name: numpy_condition
import numpy as np
x=[1,7,4, 90, 12.4, 56, 10, 2, 0, -5, 22, 34, 65, 10, -4, 17, 2]
y=np.array(x)
print(y<12)
print(y[y<12])

'''
output:
[ True  True  True False False False  True  True  True  True False False
 False  True  True False  True]
[ 1.  7.  4. 10.  2.  0. -5. 10. -4.  2.]
'''
