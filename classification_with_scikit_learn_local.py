#file name: classification_with_scikit_learn.py

from google.colab import files
uploaded = files.upload()

"""Load the dataset into a dataframe:"""

from google.colab import drive
drive.mount("/gdrive")

import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt'].decode('utf-8')), sep='\t')
df

"""Split the dataset into training and testing:"""

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(df.loc[:,df.columns != "Class"], df.Class, random_state = 0)

print(train_X)

print(train_y)

"""Learn using a knn-Classifier:"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(train_X, train_y)

"""Classify using the knn-Classifier:"""

predictions = neigh.predict(val_X)
print("Type of predictions: ", type(predictions))
print(predictions)

print("Type of val_y: ", type(val_y))
print(predictions == val_y)

"""Check how good the prediction is:"""

accuracy = sum(predictions == val_y)/len(predictions)
print(accuracy)

"""Use cross-validation"""

from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
shuffled = shuffle(df)
score = cross_val_score(classifier, shuffled.loc[:,shuffled.columns != "Class"], shuffled.Class, cv=10)
print(score)

from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
shuffled = shuffle(pd.concat([train_X, train_y], axis=1))
for k in range(1,50):
  classifier = KNeighborsClassifier(n_neighbors=k)
  score = cross_val_score(classifier, shuffled.loc[:,shuffled.columns != "Class"], shuffled.Class, cv=10)
  #print(score)
  print(np.median(score))

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(train_X, train_y)
predictions = knn.predict(val_X)
accuracy = sum(predictions == val_y)/len(predictions)
print(accuracy)