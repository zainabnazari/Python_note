# file name: numpy_ex2.py
import numpy as np
x1=np.array([1,2,3,4])
x2=np.array([1,2,3,"C"])
print(type(x1[0]),type(x2[0]))
'''
output:

<class 'numpy.int64'> <class 'numpy.str_'>

'''
# now we make a change in x2
x2[3]=4
print(x2)
print(type(x2[3]))

'''
output:
['1' '2' '3' '4']
<class 'numpy.str_'>
'''
# you see even though we have changed the last element in x2 to integer,
# the type still remains as string.

x1[3]=7.7
print(x1)
print(type(x1[3]))

'''
output:
[1 2 3 7]
<class 'numpy.int64'>
'''
# you see above that the type of element at position 3 is still integer,
# despite the fact that we input a float number.
x1[3]="C"
print(x1)
print(type(x1[3]))

'''
output:
ValueError: invalid literal for int() with base 10: 'C'
'''
# as you see, the string cannot be converted to integer.
