import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
balance_data = pd.read_csv(
'C:\\Users\\akash\\Desktop\\sonar.csv',
                           sep= ',', header= None)
print ("Dataset Lenght:: ", len(balance_data))
print ("Dataset Shape:: ", balance_data.shape)
X = balance_data.values[:, 0:59]
Y = balance_data.values[:,60]
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
clf_gini = KNeighborsClassifier(n_neighbors=2,weights='distance')
clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)
print(y_pred)
#lse=(y_test-y_pred)
print(y_test)
print ("Accuracy is ", accuracy_score(y_test,y_pred)*100)
