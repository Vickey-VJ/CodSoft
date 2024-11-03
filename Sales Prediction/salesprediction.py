# -*- coding: utf-8 -*-
"""SalesPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jR7z7gXocMELaqJzSmXd22g8ec3E0OYu

# Sales Prediction - Advertising

> ## **Data Preparetion**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dst = pd.read_csv('/content/drive/MyDrive/DS projects/DataSets/salesprediction.csv')
print(dst.head())
print()
print('shape of the dataframe', dst.shape)
print()
dst.isna().sum()

dst.info()

dst.describe()

dst.corr()

"""> ## **Data Visualization**

>> ### Scatter Plot
"""

sns.scatterplot(x = dst['TV'],y =dst.Sales, hue = dst.Sales)
plt.title('TV vs Sales')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()

sns.scatterplot(x = dst['Radio'],y =dst.Sales, hue = dst.Sales)
plt.title('Radio vs Sales')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.show()

sns.scatterplot(x = dst['Newspaper'],y =dst.Sales, hue = dst.Sales)
plt.title('NewsPaper vs Sales')
plt.xlabel('NewsPaper')
plt.ylabel('Sales')
plt.show()

""">> ### Box Plot"""

sns.boxplot(x=dst['TV'])
plt.show()

sns.boxplot(x=dst['Radio'])
plt.show()

sns.boxplot(x=dst['Newspaper'])
plt.show()

sns.boxplot(x=dst['Sales'])
plt.show()

"""> ## **The Model**"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

x=dst.drop(['Sales'],axis = 1)
x.head()

y=dst['Sales']
y.head()

x1 = dst.iloc[:, :-1].values
y1 = dst.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size = 0.2, random_state = 42)
print('Shape of X_train: ', X_train.shape)
print('Shape of X_test: ', X_test.shape)
print('Shape of y_train: ', y_train.shape)
print('Shape of y_test: ', y_test.shape)

""">> Linear Regression"""

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_y_pred = lr.predict(X_test)
lr_r2 = r2_score(y_test, lr_y_pred)

print("Accuracy for Multiple Linear Regression is",round(lr_r2*100, 2), '%')

""">> Polynomial Regression"""

polynm_reg = PolynomialFeatures(degree = 3)
X_polynm = polynm_reg.fit_transform(X_train)
poly_regressor = LinearRegression()
poly_regressor.fit(X_polynm, y_train)

X_test_poly = polynm_reg.transform(X_test)
poly_y_pred = poly_regressor.predict(X_test_poly)

r2_poly_reg = r2_score(y_test, poly_y_pred)
print('Accuracy Score for Polynomial Regression is',round(r2_poly_reg*100, 2), '%')

""">> Decision Tree Regression"""

dt_regressor = DecisionTreeRegressor(random_state = 0)
dt_regressor.fit(X_train, y_train)

dt_y_pred = dt_regressor.predict(X_test)
r2_dt = r2_score(y_test, dt_y_pred)
print('Accuracy Score for Decision Tree Regression is',round(r2_dt*100, 2), '%')

""">> Random Forest Regression"""

rf_regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
rf_regressor.fit(X_train, y_train)

rf_y_pred = rf_regressor.predict(X_test)
r2_rf = r2_score(y_test, rf_y_pred)
print('Accuracy Score for Random Forest Regression is',round(r2_rf*100, 2), '%')