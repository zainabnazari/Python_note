#file name: plot_list_data_4
import matplotlib.pyplot as plt
plt.plot([-1, 2, 5, 4], [1, 0, 9, 15]) #if we use plt.plot([-1, 2, 5, 4], [1, 0, 9, 15], 'b*') instead, it will not connect the points in the list.
plt.xlabel('x-lable') # here is how to lable the plot
plt.ylabel('y-label')
plt.show()
