#file name: mean.py
import numpy as np # a code which finds the mean of a list:
p=np.asarray(eval(input("numbers?")))
y=0
z=0
for x in p:
   z=z+1
   y=y+x
   mean=y/z
print(mean)
