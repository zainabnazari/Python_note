# file name: margin.py
import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(-2,2,400)
fig, ax = plt.subplots()
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
ax.plot(x,y1,label='sin(x)')
ax.plot(x,y2,label='cos(x)')
ax.plot(x,y3,label='tan(x)')
plt.margins(0) # this makes the frame fit right to the data.
ax.legend()
plt.show()
