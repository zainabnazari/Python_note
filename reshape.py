#file name: reshape.py
import numpy as np

myarray = np.array([[2,5,6],[3,4,7]])
print("myarray: \n",myarray)
print("sizeofmyarray:", myarray.shape) # this shows: (gives the number of rows and columns of myarray) the dimensionality and the size of each dimension. 
onecolumnsixrows = myarray.reshape(-1,1)#The size of the new array in each dimension is given. If you type -1, that dimension is going to be computed based on the number of elements in the original array.
print("onecolumnsixrows: \n",onecolumnsixrows)
onedimarray = myarray.reshape(-1)#It's also possible to change the dimensionality. This now is a one-dimensional array
print("onedimarray: \n",onedimarray)
threedimarray = myarray.reshape(2,1,-1)#The dimensionality can also be increased. Only one parameter can be -1, because otherwise it could not be inferred.
# the number of numbers inside parentheses determines the dimensionallity of the array, the -1 will automatically provide the adequate number,
# and the multiplication of the numbers (excluding -1, means including any proper multiplication) should match to the numbers of the elements of the array. 
print("threedimarray: \n",threedimarray)
"""
output:
myarray: 
 [[2 5 6]
 [3 4 7]]
sizeofmyarray: (2, 3)
onecolumnsixrows: 
 [[2]
 [5]
 [6]
 [3]
 [4]
 [7]]
onedimarray: 
 [2 5 6 3 4 7]
threedimarray: 
 [[[2 5 6]]

 [[3 4 7]]]
"""
