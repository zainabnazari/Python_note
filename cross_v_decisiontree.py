#file name: cross_v_decisiontree.py
"""Set up the dataset"""
import pandas as pd
df = pd.read_csv('Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt', sep='\t')
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(df.loc[:,df.columns != "Class"], df.Class, random_state = 0)

"""Use cross-validation on the training set to find out the best value for the maximum depth of the tree (in an arbitrary range of depth).
We call this value 'k', to emphasize that the code is similar to the previous kNN code."""
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn import tree
import numpy as np
shuffled = shuffle(pd.concat([train_X, train_y], axis=1))#We actually don't need this shuffeling, because train_test_split already shuffles.
dict = {k:np.mean(cross_val_score(tree.DecisionTreeClassifier(max_depth=k), shuffled.loc[:,shuffled.columns != "Class"], shuffled.Class, cv=10)) for k in range(1,7)}
max_k = max(dict, key=dict.get)
print(max_k)
"""
output:
6
"""
#We see that the highest accuracy is reached for k=6 (in the first line).
#Now we test how good a decision tree of maximum depth 6 performs on the testing data set.
classifier = tree.DecisionTreeClassifier(max_depth=max_k)
classifier.fit(train_X, train_y)
predictions = classifier.predict(val_X)
accuracy = sum(predictions == val_y)/len(predictions)
print(accuracy)
"""
0.781074168797954
"""
