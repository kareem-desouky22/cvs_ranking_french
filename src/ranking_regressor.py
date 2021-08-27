# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:41:07 2021

@author: KHC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

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


results_folder=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data/results')
file = os.path.join(results_folder,'classifier_features.csv')

data =pd.read_csv(file,  index_col=0)
data=data.drop(['name'],axis=1)
data=data.fillna(0)


x = data.drop(['cv_score'], axis=1)
y=data['cv_score']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)


# The coefficients
print('Results')
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, y_pred))

# Plot outputs





# plt.plot(y_test, 'b')
# plt.plot(y_pred, 'y')
# plt.legend(['True', 'Pred'])
# plt.title('Predicted vs True')
# plt.show()

