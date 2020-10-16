#file name: numpy_and_math_error.py
import numpy as np
import math
myarray = np.array([1,2,3])
root = math.sqrt(myarray)
print(root)
"""
Output:
Traceback (most recent call last):
  File "numpy_and_math_error.py", line 5, in <module>
    root = math.sqrt(myarray)
TypeError: only size-1 arrays can be converted to Python scalars
"""