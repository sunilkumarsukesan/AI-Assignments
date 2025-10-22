
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import io

st.title("QA Team Productivity Analysis Dashboard")
st.write("""
This interactive dashboard allows you to assess tester productivity using your own dataset. Upload your CSV file to begin the analysis. All insights, statistics, and visualizations are generated dynamically from your data.
""")

uploaded_file = st.file_uploader("Upload your QA productivity CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(data.head())
    st.write("**Dataset Description:**")
    st.dataframe(data.describe())
    st.write("**Dataset Info:**")
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    st.write(f"Total unique tester IDs: {data['Tester_ID'].nunique()}")
    st.write("Null values per column:")
    st.write(data.isnull().sum())

    st.markdown("---")
    st.subheader("Handling Missing Values")
    data['Defect_Severity_Avg'].fillna(round(data['Defect_Severity_Avg'].mean(), 2), inplace=True)
    data['Automation_Coverage'].fillna(round(data['Automation_Coverage'].mean(), 2), inplace=True)
    data['Execution_Hours'].fillna(round(data['Execution_Hours'].mean(), 2), inplace=True)
    st.write("Missing values in numeric columns have been imputed with the mean value.")
    st.write(data.isnull().sum())

    st.markdown("---")
    st.subheader("Outlier Detection (IQR Method)")
    st.write("""
    Outliers can significantly affect the results of data analysis and modeling. Here, we use the Interquartile Range (IQR) method to detect outliers in key numeric columns. The histograms below show the distribution of each variable, helping us visually assess the spread and presence of outliers.
    """)
    for col in ['Defect_Severity_Avg', 'Automation_Coverage', 'Execution_Hours']:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_limit = Q1 - 1.5 * IQR
        upper_limit = Q3 + 1.5 * IQR
        outliers = data[(data[col] < lower_limit) | (data[col] > upper_limit)]
        st.write(f"**Outliers in {col}:** {list(outliers.index)}")
        fig, ax = plt.subplots()
        sns.histplot(data[col], bins=10, kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)
        st.caption(f"Histogram and KDE for {col}. Outliers are data points outside the range [{lower_limit:.2f}, {upper_limit:.2f}].")

    st.markdown("---")
    st.subheader("Feature Engineering")
    st.write("""
    To better understand tester productivity, we create new ratio features:
    - **Defects_per_Test**: Number of defects found per test case executed.
    - **Execution_per_Test**: Execution hours spent per test case executed.
    These features help normalize productivity metrics across testers with different workloads.
    """)
    data['Defects_per_Test'] = data['Defects_Found'] / data['Total_TestCases_Executed']
    data['Execution_per_Test'] = data['Execution_Hours'] / data['Total_TestCases_Executed']
    st.write("New features created: Defects_per_Test and Execution_per_Test.")
    st.dataframe(data[['Defects_per_Test', 'Execution_per_Test']].head())

    st.write("""
    We also standardize the main numeric columns using StandardScaler. This ensures all features are on a comparable scale, which is important for many machine learning algorithms.
    """)
    scaler = StandardScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(data[['Execution_Hours','Defect_Severity_Avg','Automation_Coverage']]), columns=['Execution_Hours','Defect_Severity_Avg','Automation_Coverage'])
    st.write("Standardized numeric columns:")
    st.dataframe(scaled_df.head())

    st.markdown("---")
    st.subheader("Exploratory Data Analysis & Visualization")
    st.write("""
    The following charts provide visual insights into tester productivity and process efficiency. Each visualization is accompanied by a brief interpretation to help you understand the underlying patterns in your data.
    """)

    # Bar Chart: Average closure time per module
    st.markdown("**Bar Chart: Average Closure Time per Module**")
    st.write("This chart shows the average time taken to close defects for each module. Modules with higher closure times may indicate more complex or problematic areas.")
    avgClosureTime = data.groupby("Module")["Avg_Closure_Time"].mean().reset_index(name="Avg Closure Time")
    fig, ax = plt.subplots()
    ax.bar(avgClosureTime["Module"], avgClosureTime["Avg Closure Time"])
    ax.set_xlabel("Module")
    ax.set_ylabel("Avg Closure Time")
    ax.set_title("Average Closure Time per Module")
    st.pyplot(fig)

    # Scatter Plot: Total TestCases Executed vs Execution Hours
    st.markdown("**Scatter Plot: Workload vs Execution Hours**")
    st.write("This scatter plot visualizes the relationship between the number of test cases executed and the total execution hours. A positive correlation suggests that more test cases require more effort, as expected.")
    fig, ax = plt.subplots()
    ax.scatter(data["Total_TestCases_Executed"], data["Execution_Hours"])
    ax.set_xlabel("Total TestCases Executed")
    ax.set_ylabel("Execution Hours")
    ax.set_title("Workload vs Execution Hours")
    st.pyplot(fig)

    # Histogram + KDE: Distribution of closure time and execution hours
    st.markdown("**Histograms: Execution Hours & Avg Closure Time**")
    st.write("These histograms show the distribution of execution hours and average closure time. The KDE (Kernel Density Estimate) curve helps visualize the probability distribution, highlighting skewness or multimodal patterns.")
    fig, subPlotLine = plt.subplots(1,2, figsize=(12,6))
    sns.histplot(data['Execution_Hours'].dropna(), bins=5, kde=True, ax=subPlotLine[0])
    subPlotLine[0].set_title("Execution Hours Distribution")
    sns.histplot(data['Avg_Closure_Time'].dropna(), bins=10, kde=True, ax=subPlotLine[1])
    subPlotLine[1].set_title("Avg Closure Time Distribution")
    st.pyplot(fig)

    # Correlation Heatmap
    st.markdown("**Correlation Heatmap**")
    st.write("This heatmap shows the correlation between numeric variables and average closure time. Strong correlations can help identify which factors most influence closure time, guiding process improvements.")
    correlation_with_closure = data.corr(numeric_only=True)[['Avg_Closure_Time']].drop(index='Avg_Closure_Time')
    fig, ax = plt.subplots()
    sns.heatmap(correlation_with_closure, annot=True, fmt=".2f", cmap='viridis', cbar=True, ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

    # Boxplot: Defect Severity vs Avg Closure Time
    st.markdown("**Boxplot: Defect Severity vs Avg Closure Time**")
    st.write("The boxplot compares the spread and central tendency of defect severity and average closure time. Outliers and the width of the boxes provide insight into variability and potential process issues.")
    fig, ax = plt.subplots()
    boxPlotData = data[["Defect_Severity_Avg","Avg_Closure_Time"]]
    ax.boxplot(boxPlotData.values,
               vert=True,
               patch_artist=True,
               notch=True,
               showmeans=True,
               boxprops=dict(facecolor="lightblue"),
               medianprops=dict(color="red", linewidth=2),
               meanprops=dict(marker="o", markerfacecolor="green", markersize=8),
               flierprops=dict(marker="x", color="orange"))
    ax.set_xticklabels(["Defect_Severity_Avg","Avg_Closure_Time"])
    ax.set_title("Boxplot: Defect Severity vs Avg Closure Time")
    st.pyplot(fig)

    st.markdown("---")
    st.subheader("Model Building: Linear Regression")
    st.write("""
    We use a simple linear regression model to predict average closure time based on the number of defects found. The plot below shows the actual vs. predicted values for the test set. A good fit indicates that defect count is a strong predictor of closure time.
    """)
    x = data[['Defects_Found']]
    y = data['Avg_Closure_Time']
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=10)
    model = LinearRegression()
    model.fit(xtrain, ytrain)
    ypredit = model.predict(xtest)
    fig, ax = plt.subplots()
    ax.scatter(xtest, ytest, marker='o', color = 'red', label='Testing Values', alpha=0.3)
    ax.plot(xtest, ypredit, color='blue', label = 'Predicted Values')
    ax.set_xlabel("Defects Found")
    ax.set_ylabel("Average Closure Time")
    ax.legend()
    ax.set_title("Linear Regression: Defects Found vs Avg Closure Time")
    st.pyplot(fig)

    st.success("Assessment complete! This dashboard demonstrates how Python and data analysis can be used to assess tester productivity using your dataset. Each chart and metric above provides actionable insights for QA process improvement.")

    st.markdown("---")
    st.subheader("Predict Average Closure Time for Custom Defect Count")
    st.write("""
    Enter the number of defects found to estimate the expected average closure time using the trained linear regression model above. This helps you forecast closure time for different workload scenarios.
    """)
    user_defects = st.number_input("Enter number of defects found:", min_value=0, value=0, step=1)
    if user_defects > 0:
        predicted_closure = model.predict(np.array([[user_defects]]))[0]
        st.info(f"For {user_defects} defects found, the predicted Average Closure Time is **{predicted_closure:.2f}** hours.")
    else:
        st.caption("Enter a value greater than 0 to get a prediction.")
else:
    st.info("Please upload a CSV file to begin the analysis.")
