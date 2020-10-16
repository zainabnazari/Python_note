# file name: all_colour.py
import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(-1,1,200)
fig, ax = plt.subplots()
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
ax.plot(x,y1,label='sin(x)',color=(0.5,1.0,0.0))
ax.plot(x,y2,label='cos(x)',color='xkcd:macaroni and cheese')
ax.plot(x,y3,label='tan(x)',color='#48a7f9')

ax.legend(frameon=False)
plt.show()
