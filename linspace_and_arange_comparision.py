#file name: linspace_and_arange_comparision.py

#This file makes the difference between linspace and arange clear. These two commands are often mixed up.
import numpy as np

print(np.linspace(4,20,3))#The last number indicates the number of substeps.
print(np.arange(4,20,3))#The last number indicates the step size between substeps.

"""
output:
[ 4. 12. 20.]
[ 4  7 10 13 16 19]
"""