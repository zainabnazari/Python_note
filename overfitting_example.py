#file name: overfitting_example.py
import numpy as np
import matplotlib.pyplot as plt

class1 = np.random.normal(-1, 1, 10)
class2 = np.random.normal(1, 1, 10)
plt.plot(class1, 'b*')
plt.plot(class2, 'r*')
plt.show()