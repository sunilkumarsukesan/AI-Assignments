import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,4,9,16,25])


poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(x_poly,y)

y_pred = model.predict(x_poly)

plt.scatter(X, y, color='blue', label='Actual Data Points')
plt.plot(X, y_pred, color='red', label='Polynomial Regression Fit')
plt.title('Polynomial Regression Fit')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
print(model.predict(poly.transform([[15]])))