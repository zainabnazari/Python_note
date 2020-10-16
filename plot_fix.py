#plot name: plot_fix.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5.0,5.,1000.0)
f = -x * (2.0 - 8.0 * np.exp(- (x**2)/6.0))
plt.plot(x, f)
plt.show()
