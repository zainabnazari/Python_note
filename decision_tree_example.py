#file name: decision_tree_example.py
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn import tree
X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

plt.figure(figsize=(10,12))
plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)

tree.plot_tree(clf)
plt.show()
