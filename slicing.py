# file name: slicing.py

import numpy as np

simpleArray = np.array([19,8,7,1,5,4])
firstElement = simpleArray[0]#Numpy arrays start indexing with 0.
lastElement = simpleArray[-1]#The second-to-last element would be simpleArray[-2].
withoutFirstAndLastElement = simpleArray[1:-1]# x:y means every element from position x (including) to position y (excluding). If x is not given, it takes elements from the start. If y is not given, it takes elements to the end.
myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
firstRow = myArray[0,:]
firstcolumn=myArray[:,0]
secondColumn = myArray[:,1]
oddRowsEvenColumns = myArray[1::2,0::2] # x:y:z means every element from x (including) to y (excluding) in steps of z. Like before, if x is not given, it takes elements from the start. If y is not given, it takes elements to the end.
print("Simple Array: ", simpleArray)
print("First Element: ", firstElement)
print("Last Element: ", lastElement)
print("The simple array without its first and last element: ", withoutFirstAndLastElement)
print("A two-dimensional array: ", myArray)
print("First Row: ", firstRow)
print("First Column: ",firstcolumn)
print("Second Column: ", secondColumn)
print("All values in odd rows and even columns: ", oddRowsEvenColumns)
"""
Output:
Simple Array:  [19  8  7  1  5  4]
First Element:  19
Last Element:  4
The simple array without its first and last element:  [8 7 1 5]
A two-dimensional array:  [[1 2 3]
 [4 5 6]
 [7 8 9]]
First Row:  [1 2 3]
First Column:  [1 4 7]
Second Column:  [2 5 8]
All values in odd rows and even columns:  [[4 6]]

"""
