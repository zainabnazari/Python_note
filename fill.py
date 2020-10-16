# plot name:fill.py
import matplotlib.pyplot as plt
x=[1900,1925, 1950, 1975, 2000]
y=[13.46, 15.79, 18.55, 20.45, 25.02]
plt.plot(x,y)
plt.fill_between(x,y,0,color="red")
plt.yticks([0, 5, 10, 15, 20, 25, 30], ['0', '1V', '2V', '3V', '4V', '5V', '6V'])
# similarly you can use xticks() function to rescsle and rename the steps on the x axes.
plt.show()
