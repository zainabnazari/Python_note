# file name: plot_list_data_3.py
import matplotlib.pyplot as plt
plt.scatter([100, 2000, 5000, 400000], [1, 0, 9, 15])
plt.xscale('log') # if the range of the values is really big, the logarithmic scale is a good option to represent the data.
plt.xlabel('x-lable') # here is how to lable the plot
plt.ylabel('y-label')
plt.show()
