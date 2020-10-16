#name of file: histogram.py
import matplotlib.pyplot as plt
x=[1,3,3,8,2,9,10,0,8,5]
fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)
#axs.hist(x, bins=5) 
axs.hist(x, bins='auto')
plt.show()
