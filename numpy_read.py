#file name: numpy_read.py
import numpy as np
my_array = np.loadtxt("example_read_in.txt")
print(my_array)
print(my_array.reshape(-1,1))