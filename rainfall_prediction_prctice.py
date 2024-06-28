# -*- coding: utf-8 -*-
"""rainfall_prediction_prctice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W_CdUbRIWKQGWGL-W75TM7B9Oow4BmrP
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("//content//rainfall.csv")

df.head()

df.shape

df.date

df.info()

df.isnull().sum()

df.duplicated().sum()

df.dropna(inplace=True)

df.columns[2:]

df.describe()

df.describe(include='O').T

sns.countplot(data=df,x='weather_condition')

df.head()

df.groupby('temperature')['rainfall'].value_counts().reset_index()

df.corr

from sklearn.preprocessing import LabelEncoder

encoder=LabelEncoder()

encoder.fit_transform(df['weather_condition'])

x = df.drop(['weather_condition'], axis=1)
y = df['weather_condition']

df.head()

# prompt: ancode all velue

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
for column in df.columns:
  if df[column].dtype == 'object':
    df[column] = encoder.fit_transform(df[column])

df.head()

from sklearn.preprocessing import StandardScaler

scaler= StandardScaler()

x_cols=x.columns

x=scaler.fit_transform(x)

x=pd.DataFrame(x,columns=x_cols)

x.head()

from sklearn.feature_selection import SelectKBest, f_classif

kbest= SelectKBest(f_classif,k=5)

kbest.fit(x,y)

x=x[x.columns[kbest.get_support()]]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

def modelling(model):
  model = model
  model.fit(x_train,y_train)
  pred=model.predict(x_test)
  print(f"Accuracy: {accuracy_score(y_test,pred)*100}")
  print(classification_report(y_test,pred))
  plt.figure()
  sns.heatmap(confusion_matrix(y_test,pred), fmt='0.0f',annot=True)
  plt.show()

modelling(LogisticRegression())

modelling(RandomForestClassifier())



