# -*- coding: utf-8 -*-
"""CreditCardFraudDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IKtMHJKkNUrmdgs7aGeuLqlSrYy8iRre

# **Credit Card Fraud Detection**

> ### DATA CLEANING
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

import warnings
warnings.filterwarnings('ignore')

dst = pd.read_csv('/content/drive/MyDrive/DS projects/DataSets/creditcard.csv')
dst.head()

dst.describe()

"""> ### DATA VISUALIZATION"""

sns.countplot(x='Class', data=dst)
plt.title('No. of Fraud vs Non-fraud transactions')
plt.show

"""> ### DATA PROCESSING"""

print(dst['Class'].value_counts())

true_trans = dst[dst['Class']==0]
fraud_trans = dst[dst['Class']==1]

print(true_trans['Amount'].mean())

fraud_trans['Amount'].mean()

dst.Amount.describe()

true_sample = true_trans.sample(n=492)

new_dst = pd.concat([true_sample, fraud_trans], axis = 0)

new_dst.Class.value_counts()

"""> ### THE MODEL"""

y = new_dst["Class"] # target
x = new_dst.iloc[:,0:30]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size = 0.2, random_state = 42)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)

y_pred = rfc.predict(x_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("The accuracy is", accuracy_score(y_test, y_pred))
print("The precision is", precision_score(y_test, y_pred))
print("The recall is", recall_score(y_test, y_pred))
print("The F1 score is", f1_score(y_test, y_pred))