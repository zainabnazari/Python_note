# file name: legendframeless.py
import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(-1,1,200)
fig, ax = plt.subplots()
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
ax.plot(x,y1,label='sin(x)', linewidth=5) # linewidth determines the width of a line. 
ax.plot(x,y2,label='cos(x)')
ax.plot(x,y3,label='tan(x)')

ax.legend(frameon=False)
plt.show()
