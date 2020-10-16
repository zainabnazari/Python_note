# file name: arange.py
# This file contains the same commands as range.py, but using numpy.arange rather than range. The output is the same.
import numpy as np
print('this is the range of a given number 10, the numpy style')
x=np.arange(10)
for n in x:
    print(n)
print('this is the range of given starting number 1, and ending number 10')
y=np.arange(1,10)
for n in y:
    print(n)
print('this is the range of given starting number 1, and ending number 10,  with defined step=2')
z=np.arange(1,10,2)
for n in z:
    print(n)
	
#However, np.arange has an advantage over range: It produces an array, which we can print and work on further (for example slicing, concatenating, adding a value, etc.):
print(range(1,10,2))#output: range(1, 10, 2)
print(np.arange(1,10,2))#output: [1 3 5 7 9]
'''
output:
this is the range of a given number 10, the numpy style
0
1
2
3
4
5
6
7
8
9
this is the range of given starting number 1, and ending number 10
1
2
3
4
5
6
7
8
9
this is the range of given starting number 1, and ending number 10,  with defined step=2
1
3
5
7
9
range(1, 10, 2)
[1 3 5 7 9]

'''
