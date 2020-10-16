#plot name: plot_error.py
import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(-5.0,5.,1000.0)
f = -x * (2.0 - 8.0 * math.exp(- (x**2)/6.0))
plt.plot(x, f)
plt.show()

'''
output:
TypeError: only size-1 arrays can be converted to Python scalars

'''
