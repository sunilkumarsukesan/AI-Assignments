import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score, recall_score,f1_score,classification_report)
import os

print(os.getcwd())

df = pd.read_csv('./Practise/01 Machine Learning/04 Logistic Regression/sales_data.csv')
print(df.head())

le = LabelEncoder()

X_train, X_test, y_train, y_test = train_test_split( df[['Total Amount']], le.fit_transform(df['CardType']) , random_state= 42, test_size=0.2)

model = LogisticRegression(class_weight='balanced',random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(confusion_matrix(y_test,y_pred))

print(f"Scores : \nAccuracy : {accuracy_score(y_test,y_pred)}\nPrecision : {precision_score(y_test,y_pred)}\nRecall : {recall_score(y_test,y_pred)}\nF1 score : {f1_score(y_test,y_pred)}")

print(f"Classification report : {classification_report(y_test, y_pred, target_names=le.classes_)}")

print(f"Threshold is {-model.intercept_[0]/model.coef_[0][0]}")

input = pd.DataFrame({'Total Amount': [int(input("Enter the total amount : "))]})

print(f"CardType for the given input is {le.inverse_transform(model.predict(input))[0]}")

