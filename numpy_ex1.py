# file name: numpy_ex1.py
list1=[1,2,3,4]
list2=[1,2,3,4]
list3=[[1,2,3,4],[1,2,3,4]]
#print("list1*list2= ",list1*list2) # this will give error, the operation of multiplication on lists is not defined!
print("list1+list2= ",list1+list2)
print("list3+list1= ",list3+list1)
import numpy as np
numpyarray1=np.array([1,2,3,4])
numpyarray2=np.array([1,2,3,4])
numpyarray3=np.array([[1,2,3,4],[1,2,3,4]])
print("numpyarray1*numpyarray2= ", numpyarray1*numpyarray2)
print("numpyarray1+numpyarray2= ", numpyarray1+numpyarray2)
print("numpyarray3+numpyarray1= ", numpyarray3+numpyarray1)
print("numpyarray3*numpyarray1= ", numpyarray3*numpyarray1)

'''
output:

list1+list2=  [1, 2, 3, 4, 1, 2, 3, 4]
list3+list1=  [[1, 2, 3, 4], [1, 2, 3, 4], 1, 2, 3, 4]
numpyarray1*numpyarray2=  [ 1  4  9 16]
numpyarray1+numpyarray2=  [2 4 6 8]
numpyarray3+numpyarray1=  [[2 4 6 8]
 [2 4 6 8]]
numpyarray3*numpyarray1=  [[ 1  4  9 16]
 [ 1  4  9 16]]

'''
