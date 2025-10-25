import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_squared_error, root_mean_squared_error, r2_score

"""
1. Load the Dataset
o Load the provided dataset using Pandas.
o Retain only the columns Square Footage and Price for model building.
"""
house_data_df = pd.read_csv("./Week 7/house_price_regression_dataset.csv")[['Square_Footage','House_Price']]

"""
2. Exploratory Data Analysis (EDA)
o Display the first few rows of the dataset.
o Check for missing or null values and handle them appropriately.
o Visualize the relationship between Square Footage and Price using a scatter
plot.
"""
print(house_data_df.head())
print(house_data_df.isnull().sum())
print(house_data_df.isna().sum())
sns.scatterplot(data=house_data_df,x='Square_Footage',y='House_Price')
plt.show()

"""
3. Feature and Target Selection
o Assign Square Footage as the independent variable (X).
o Assign Price as the dependent variable (Y).
"""
X = house_data_df[['Square_Footage']]
Y = house_data_df['House_Price']

"""
4. Train-Test Split
o Split the dataset into training and testing sets using an 80-20 ratio.
"""
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

"""
5. Model Building
o Create a Linear Regression model using LinearRegression from
sklearn.linear_model.
o Fit the model on the training data.
o Display the intercept (b₀) and coefficient (b₁) of the regression line.
"""
linear = LinearRegression()
linear.fit(X_train,Y_train)
print(f"Intercept, b0 : {linear.intercept_}")
print(f"Coefficient, b1 : {linear.coef_}")

"""
6. Prediction and Evaluation
o Predict the house prices for the test set.
o Calculate and print the following evaluation metrics:
 Mean Squared Error (MSE)
 Root Mean Squared Error (RMSE)
 R² Score (Coefficient of Determination)
"""
Y_Pred = linear.predict(X_test)
print(f"Mean Squared Error (MSE) : {mean_squared_error(Y_test, Y_Pred)}")
print(f"Root Mean Squared Error (RMSE) : {root_mean_squared_error(Y_test, Y_Pred)}")
print(f"R² Score (Coefficient of Determination) : {r2_score(Y_test, Y_Pred)}")

"""
7. Visualization
o Plot the regression line along with the actual data points.
o Visualize actual vs predicted prices to assess model performance.
"""
plt.scatter(X_test, Y_test, color = 'Blue', marker='X', label = 'Actual')
plt.plot(X_test, Y_Pred, color = 'Red', label = 'Predicted')
plt.xlabel('Square_Footage')
plt.ylabel('House_Price')
plt.legend()
plt.show()

#sns.regplot(x='Square_Footage', y='House_Price', data=house_data_df, ci=None, line_kws={'color': 'red'})
#plt.show()