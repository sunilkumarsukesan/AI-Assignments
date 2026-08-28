import numpy as np
from sklearn.linear_model import Ridge

# Sample data (noisy quadratic trend approximated by linear model for demo)
#X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
#y = np.array([1.2, 3.9, 9.1, 16.2, 24.8]) # roughly ~ x^2 with some noise

X = np.array([1, 2, 3]).reshape(-1, 1)
y = np.array([1, 2, 2]) # roughly ~ x^2 with some noise



alpha = 1.0 # regularization strength (lambda)

model = Ridge(alpha=alpha)
model.fit(X, y)

print ("--- Ridge model (univariate) --- ")
print(f"alpha (A): {alpha}")
print(f"Intercept: {model.coef_[0]:.4f}")
print(f"Coefficient for x: {model.coef_[0] :.4f}")
print(f"Coefficient for x: {model.coef_}")

# User input for prediction
try:
    x_input = int(input ("Enter an x value to predict: ") )
    y_hat = model.predict(np.array([[x_input]]))
    print(f"Predicted y for x={x_input} -> {y_hat}")
except ValueError:
    print("Please enter a valid numeric value.")