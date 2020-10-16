#file name: classification_with_scikit_learn.py
import pandas as pd
df = pd.read_csv('Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt', sep='\t')

"""Split the dataset into training and testing:"""

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(df.loc[:,df.columns != "Class"], df.Class, random_state = 0)
#train_X are the attributes in the training set.
#val_X are the attributes in the testing set.
#train_y are the classes in the training set.
#val_y are the classes in the testing set.
print(train_X)
"""
      Distance_to_wall-180  ...  Distance_to_copter135
4234              0.984127  ...               8.000000
321               0.360733  ...               8.000000
4338              5.182590  ...               0.945480
6445              4.938473  ...               0.334903
6391              2.409339  ...               8.000000
...                    ...  ...                    ...
4931              2.561899  ...               8.000000
3264              2.680542  ...               8.000000
1653              5.908682  ...               0.912824
2607              4.669057  ...               2.427180
2732              4.076913  ...               1.282137

[5865 rows x 16 columns]
"""

print(train_y)
"""
4234    3
321     8
4338    3
6445    7
6391    3
       ..
4931    3
3264    3
1653    3
2607    3
2732    3
Name: Class, Length: 5865, dtype: int64
"""

"""Learn using a knn-Classifier:"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(train_X, train_y)
"""
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=5, p=2,
                     weights='uniform')
"""

"""Classify using the knn-Classifier:"""

predictions = neigh.predict(val_X)
print("Type of predictions: ", type(predictions))
print(predictions)
"""
Type of predictions:  <class 'numpy.ndarray'>
[6 4 3 ... 3 4 3]
"""

print("Type of val_y: ", type(val_y))
print(predictions == val_y)
"""
Type of val_y:  <class 'pandas.core.series.Series'>
1234    True
7519    True
5687    True
1835    True
1022    True
        ...
4643    True
6975    True
2381    True
5585    True
5597    True
Name: Class, Length: 1955, dtype: bool
"""

"""Check how good the prediction is:"""

accuracy = sum(predictions == val_y)/len(predictions)
print(accuracy)
"""
0.9329923273657289
"""

"""Use cross-validation"""
#This code validates how good 5NN is, by using cross-validation on the complete data set.
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
shuffled = shuffle(df)
score = cross_val_score(classifier, shuffled.loc[:,shuffled.columns != "Class"], shuffled.Class, cv=10)
print(score)
"""
[0.93222506 0.95268542 0.9488491  0.94245524 0.94501279 0.9398977
 0.95907928 0.93478261 0.95268542 0.95140665]
"""

"""Use cross-validation on the training set to find out the best value for k."""
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
dict = {k:np.mean(cross_val_score(KNeighborsClassifier(n_neighbors=k), train_X, train_y, cv=10)) for k in range(1,7)}
max_k = max(dict, key=dict.get)
print(dict)
print("Best k: ", max_k)
"""
[0.93606138 0.95396419 0.9398977  0.93734015 0.94629156 0.94501279
 0.94373402 0.94501279 0.94757033 0.95396419]
{1: 0.9536208289968663, 2: 0.9435612909977846, 3: 0.9437328116006072, 4: 0.9367440738178161, 5: 0.9294120041164945, 6: 0.917817211365711}
Best k:  1
"""
knn = KNeighborsClassifier(n_neighbors=max_k)
knn.fit(train_X, train_y)
predictions = knn.predict(val_X)
accuracy = sum(predictions == val_y)/len(predictions)
print(accuracy)
"""
0.9524296675191816
"""