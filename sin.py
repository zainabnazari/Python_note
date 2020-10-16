#file name: sin.py
from matplotlib import rc # this line is for naming the plot on top of the frame.
rc('text', usetex=True)
import numpy as np
import math
import matplotlib.pyplot as plt


x = np.linspace(0.,17.,200) # here is to define the number of points, and the size of the x-axix
fx = np.sin(x) # here goes the function itself

plt.plot(x,fx)
# in the following line you see how we can write text as well as mathematiacl equations with the latex formating.
plt.title(
  r'plot of $\sin(x)$', fontsize=25
)


plt.show()
