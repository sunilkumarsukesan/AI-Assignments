import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('./Practise/01 Machine Learning/Linear Regression/salary.csv')

X = data[['YearsExperience']]
Y = data['Salary']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print(f"MSE : {mean_squared_error(Y_test, Y_pred)}")
print(f"R2 Square : {r2_score(Y_test, Y_pred)}")

print(f"Equation is , y = {model.coef_} X + {model.intercept_}")


plt.scatter(X_test, Y_test, color = 'Blue', marker='X', label = 'Actual')
plt.plot(X_test, Y_pred, color = 'Red', label = 'Predicted')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

value = 9.9  # single input value
prediction = model.predict(np.array([[value]]))  # 2D array of shape (1,1)
print(prediction)
