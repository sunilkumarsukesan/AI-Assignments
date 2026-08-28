import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


def main():
    # --------------------------------------------------
    # 1. Load Data
    # --------------------------------------------------
    print("Current Working Directory:", os.getcwd())

    df = pd.read_csv("./Week 17/sales_data.csv")
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    # --------------------------------------------------
    # 2. Initial Exploration
    # --------------------------------------------------
    print("\nCorrelation:")
    print(df[["Advertising_Spend", "Total Amount"]].corr())

    plt.scatter(df["Advertising_Spend"], df["Total Amount"], marker="x")
    plt.xlabel("Advertising Spend")
    plt.ylabel("Total Amount")
    plt.title("Advertising Spend vs Total Amount")
    plt.show()

    # --------------------------------------------------
    # 3. Light Filtering (business-safe)
    # --------------------------------------------------
    df = df[df["Advertising_Spend"] < 149000]

    print("\nCorrelation after filtering:")
    print(df[["Advertising_Spend", "Total Amount"]].corr())

    # --------------------------------------------------
    # 4. Distribution Analysis
    # --------------------------------------------------
    sns.histplot(df["Advertising_Spend"], bins=30, kde=True)
    plt.title("Advertising Spend Distribution")
    plt.show()

    sns.histplot(df["Total Amount"], bins=30, kde=True)
    plt.title("Total Amount Distribution")
    plt.show()

    # --------------------------------------------------
    # 5. Define X and y
    # --------------------------------------------------
    X = df[["Advertising_Spend"]]
    y = df["Total Amount"]

    # --------------------------------------------------
    # 6. Linear Regression (Baseline)
    # --------------------------------------------------
    lin_model = LinearRegression()
    lin_model.fit(X, y)

    y_pred_lin = lin_model.predict(X)

    mse_lin = mean_squared_error(y, y_pred_lin)
    r2_lin = r2_score(y, y_pred_lin)

    print("\nLinear Regression Results")
    print("MSE:", mse_lin)
    print("R2:", r2_lin)

    plt.scatter(X, y, marker="x", label="Actual Data")
    plt.plot(X, y_pred_lin, color="red", label="Linear Regression")
    plt.xlabel("Advertising Spend")
    plt.ylabel("Total Amount")
    plt.title("Linear Regression Fit")
    plt.legend()
    plt.show()

    # --------------------------------------------------
    # 7. Polynomial Regression (Degree 2)
    # --------------------------------------------------
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)

    poly_model = LinearRegression()
    poly_model.fit(X_poly, y)

    y_pred_poly = poly_model.predict(X_poly)

    mse_poly = mean_squared_error(y, y_pred_poly)
    r2_poly = r2_score(y, y_pred_poly)

    print("\nPolynomial Regression (Degree 2) Results")
    print("MSE:", mse_poly)
    print("R2:", r2_poly)

    # --------------------------------------------------
    # 8. Sort for Smooth Curve
    # --------------------------------------------------
    sort_idx = np.argsort(X.values.flatten())
    X_sorted = X.values[sort_idx]
    y_poly_sorted = y_pred_poly[sort_idx]

    # --------------------------------------------------
    # 9. Final Comparison Plot
    # --------------------------------------------------
    plt.scatter(X, y, marker="x", label="Actual Data")
    plt.plot(X, y_pred_lin, color="red", label="Linear Regression")
    plt.plot(X_sorted, y_poly_sorted, color="green", label="Polynomial Regression (Degree 2)")
    plt.xlabel("Advertising Spend")
    plt.ylabel("Total Amount")
    plt.title("Linear vs Polynomial Regression")
    plt.legend()
    plt.show()

    # --------------------------------------------------
    # 10. Comparison Table
    # --------------------------------------------------
    comparison = pd.DataFrame({
        "Model": ["Linear Regression", "Polynomial Regression (Degree 2)"],
        "MSE": [mse_lin, mse_poly],
        "R2 Score": [r2_lin, r2_poly]
    })

    print("\nModel Comparison:")
    print(comparison)

    # --------------------------------------------------
    # 11. User Input Prediction
    # --------------------------------------------------
    try:
        new_spend = float(input("\nEnter Advertising Spend: "))

        lin_pred = lin_model.predict([[new_spend]])
        poly_pred = poly_model.predict(poly.transform([[new_spend]]))

        print("\nPredictions")
        print("Linear Model Prediction:", lin_pred[0])
        print("Polynomial Model Prediction:", poly_pred[0])

    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()
