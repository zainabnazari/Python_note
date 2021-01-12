#file_name: all_estimators.py
from sklearn.utils.testing import all_estimators

estimators = all_estimators()

for name, class_ in estimators:
    if True or hasattr(class_, 'predict_proba'):
        print(name)