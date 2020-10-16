# file name: scatter_size.py
import matplotlib.pyplot as plt
import numpy as np
x=np.array([4.1,5,10,6,-3])
y=np.array([4,5.1,14,7,3])
oursize=np.array([100,400,30,16,8])
ourcolor=['red','blue', 'purple','yellow','green']
plt.scatter(x,y,s=10*oursize,c=ourcolor, alpha=0.5) # alpha changes the opacity of the colors,
#it varies from zero to one. # "s" referes to the size, and can also be written "size", "c" refers to color and
# can be written "color" as well.
plt.show()
