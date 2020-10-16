#file name: classifier.py
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
# in the following we read the data in:
df=pd.read_csv("Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt", sep='\t') # sep='\t' recognises the tab between each data value as seperator (rather than a comma).
# below the split between training and testing data happens:
#(train_X is the attributes of the training set, val_X is the attributes of the test set, train_y is the classes of the training set, and val_y is the classes of test set)
train_X, val_X, train_y, val_y = train_test_split(df.loc[:,df.columns != "Class"], df.Class, random_state = 0)
# creating the classifier objects and considers 5 neihboring data for each data point.
neigh = KNeighborsClassifier(n_neighbors=5)
# the actual training happens here as it teaches to the machine the classes associated to the attributes.
neigh.fit(train_X, train_y)
# here machine predicts the classes of those data points which it was not trained on.
predictions = neigh.predict(val_X)
# here is the accuracy of the machine's prediction.
accuracy = sum(predictions == val_y)/len(predictions)
print("accuracy: ", accuracy)
'''
output:
[[1 2]
 [3 4]]
[[1 2]
 [3 4]]
accuracy:  0.9329923273657289
'''
'''
importing the following package
from sklearn.model_selection import train_test_split
leads to the following output:
[[1 2]
 [3 4]]
[[1 2]
 [3 4]]
we are not sure about this output but maybe they haven't used the "main condition", so it might be the output of the test code of train_test_split.
'''
