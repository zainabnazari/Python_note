#file name: decision_tree_example.py
from sklearn.datasets import load_iris
from sklearn import tree
#loading the iris dataset, which contains different samples of the iris flower.
#The dataset is included in scikit-learn.
#https://en.wikipedia.org/wiki/Iris_flower_data_set
X, y = load_iris(return_X_y=True)
#We make a decision tree classifier:
clf = tree.DecisionTreeClassifier()
#The decision tree classifier learns. That means, it builds the decision tree:
clf = clf.fit(X, y)
#We plot the decision tree that the classifier has learnt:
tree.plot_tree(clf)
#We classify an instance:
clf.predict([[5.2, 3.9, 1.1, 0.3]])#some artificial flower.
'''
output: array([0])
#That means that our artificial flower belongs to the first class.
'''