#file name: subplot.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

x = np.linspace(0.,7.,10000)

fx = np.sin(x)
fy = np.sin(2*x)

# the first subplot:

plt.subplot(2,1,1) # this line would tell how our subplot should look like: in this case it has two rows and one coloum.
# the last parameter refers to the plot number which in principle starts from one, meaning that it counts subplots from left to right
# and from top to the bottom.
plt.plot(x,fx)
# the plot title of each subplot needs to be below subplot function and before the next one.
plt.title(
  r'plot of $\sin(x)$', fontsize=15
)

# the second subplot:

plt.subplot(2,1,2)
plt.plot(x,fy)
plt.title(
  r'plot of $\sin(2x)$', fontsize=15
)

plt.show() # this line is needed to show the plot at the end.
