import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

salary_df = pd.read_csv('./Practise/01 Machine Learning/02 Multiple Linear Regression/salary.csv')

X = salary_df[['YearsExperience','Rating']]
Y = salary_df['Salary']


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

model = LinearRegression()
model.fit(X_train, Y_train)


print("--- Model Coefficients ---")
print(f"Intercept (β0): {model.intercept_:.1f}")
print(f"Coefficients (β1, β2): {model.coef_}")


formula = "y = "

for index, coeff in enumerate(model.coef_):
    if coeff < 0:
        formula += f"{round(coeff, 2)}*x{index+1} - "
    else:
        formula += f"{round(coeff, 2)}*x{index+1} + "
    

formula = formula.rstrip(" + ")
formula += f" + {round(model.intercept_, 2)}"
print(formula)

y_pred = model.predict(X_test)

print("--- Model Performance Evaluation ---")
print(f"Mean Squared Error: {mean_squared_error(Y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(Y_test, y_pred):.2f}")


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the actual data points
ax.scatter(X_test['YearsExperience'], X_test['Rating'], Y_test, color='blue', s=100, label='Actual Data Points')

# Create a meshgrid to plot the regression plane
# We create a grid of x1 and x2 values
x1_surf = np.linspace(X['YearsExperience'].min(), X['YearsExperience'].max(), 10)  # creates 10 linear points from min to max
x2_surf = np.linspace(X['Rating'].min(), X['Rating'].max(), 10)
x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)

# Predict 'y' for each point on the grid using the model
# (This is the equation of the plane)
y_plane = model.predict(pd.DataFrame({'YearsExperience': x1_surf.ravel(), 'Rating': x2_surf.ravel()}))
y_plane = y_plane.reshape(x1_surf.shape)

# Plot the regression plane
ax.plot_surface(x1_surf, x2_surf, y_plane, color='red', alpha=0.3, label='Predicted Plane')

ax.set_xlabel('x1 (Total Years of Experience - equivalent)')
ax.set_ylabel('x2 (Rating)')
ax.set_zlabel('Salary')
ax.set_title('Salary Prediction (3D Regression Plane)')
ax.legend()

plt.show()

print("Predicted Salary: ", model.predict(np.array([[5, 2]])))
