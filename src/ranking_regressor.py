# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:41:07 2021

@author: KHC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import export_graphviz
# from sklearn.externals.six import StringIO
from six import StringIO
from IPython.display import Image
#import pydotplus
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
#import xgboost as xgb
from sklearn.metrics import classification_report, accuracy_score


data =pd.read_csv('classifier_features.csv',  index_col=0)
data=data.drop(['name'],axis=1)
data=data.fillna(0)


x = data.drop(['cv_score'], axis=1)
y=data['cv_score']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x)


