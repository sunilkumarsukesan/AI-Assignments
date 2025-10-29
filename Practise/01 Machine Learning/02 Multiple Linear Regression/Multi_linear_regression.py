import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('./Practise/01 Machine Learning/02 Multiple Linear Regression/house_price_regression_dataset.csv')

X = data[['Square_Footage','Num_Bedrooms','Num_Bathrooms','Year_Built','Lot_Size','Garage_Size','Neighborhood_Quality']]
Y = data['House_Price']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print(f"MSE : {mean_squared_error(Y_test, Y_pred)}")
print(f"R2 Square : {r2_score(Y_test, Y_pred)}")

# Print the coefficients to match our
print(" --- Model Coefficients --- ")
print(f"Intercept (β0): {model.intercept_}")
print(f"Coefficients (B1, ß2): {model.coef_}")
#print(f"Model Equation: y = {model.intercept_: .1f} + {model. coef_[0]: .1f}*x1+ {model.coef_[1] :. 1f}*x2\n")

formula = "y = "

for index, coeff in enumerate(model.coef_):
    if coeff < 0:
        formula += f"{round(coeff, 2)}*x{index+1} - "
    else:
        formula += f"{round(coeff, 2)}*x{index+1} + "
    

formula = formula.rstrip(" + ")

formula += f" + {round(model.intercept_, 2)}"

print(formula)