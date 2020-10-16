# file name: plot_list_data_1.py
import matplotlib.pyplot as plt
import numpy as np
a=np.array([-1,2,10,6,-3])
#a=[-1,2,10,6,-3] or you can simply use the list.
plt.plot(a, "or") # "o" here stands for point and "r" here stands for the red color in the plot.
plt.show()
plt.clf() # you can use clf() function to clear the previous plot and go for the next (once you close the plot)!
plt.plot(a, "ob") # 'b' stands for blue.
plt.show()
