import os
import numpy as np
import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print(os.getcwd())
data = pd.read_csv('./QA Productivity/qa_team_productivity_large.csv')
print(data.head())
print(data.describe())

"""
2. Data Exploration
• Use .info(), .describe(), .isnull().sum() to inspect structure and completeness.
• Introduce a few missing values in Automation_Coverage and Defect_Severity_Avg to practice
imputation.
"""

# To get the unique values and count of the column
print(pd.unique(data['Tester_ID']))
print("Total unique tester id's : " , data['Tester_ID'].nunique())

#To get the null and non-null count
print("Null count -> " , data.isnull().sum())
data.info()

"""
3. Handling Missing Values
• Numeric columns: replace with mean() or median().
• If any categorical columns are added later (like Module), fill with mode.
"""

#Fill the missing values
data['Defect_Severity_Avg'].fillna(round(data['Defect_Severity_Avg'].mean(), 2),inplace=True)
data['Automation_Coverage'].fillna(round(data['Automation_Coverage'].mean(), 2),inplace=True)
data['Execution_Hours'].fillna(round(data['Execution_Hours'].mean(), 2),inplace=True)
data.info()

#Finding outliers using IQR - (applicable for Skewed/Uniform/Bounded(?))

#1. Defect Severity Avg
Q1 = data['Defect_Severity_Avg'].quantile(0.25)
Q3 = data['Defect_Severity_Avg'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = data[(data['Defect_Severity_Avg'] < lower_limit) | (data['Defect_Severity_Avg'] > upper_limit)]
print(outliers.index)
sns.histplot(data,x=data['Defect_Severity_Avg'],bins=10,kde=True)
plt.show()


#2. Automation_Coverage
Q1 = data['Automation_Coverage'].quantile(0.25)
Q3 = data['Automation_Coverage'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = data[(data['Automation_Coverage'] < lower_limit) | (data['Automation_Coverage'] > upper_limit)]
print(outliers.index)


#3. Execution_Hours
Q1 = data['Execution_Hours'].quantile(0.25)
Q3 = data['Execution_Hours'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = data[(data['Execution_Hours'] < lower_limit) | (data['Execution_Hours'] > upper_limit)]
print(outliers.index)


"""
5. Feature Engineering
• Create new ratio features:
o Defects_per_Test = Defects_Found / Total_TestCases_Executed
o Execution_per_Test = Execution_Hours / Total_TestCases_Executed
• Normalize numeric columns using StandardScaler, MinMaxScaler, and RobustScaler for
comparison.
"""

data['Defects_per_Test']= data['Defects_Found']/data['Total_TestCases_Executed']
print(data['Defects_per_Test'])

data['Execution_per_Test']= data['Execution_Hours']/data['Total_TestCases_Executed']
print(data['Execution_per_Test'])


scaler = StandardScaler()

scaled_df = pd.DataFrame(scaler.fit_transform(data[['Execution_Hours','Defect_Severity_Avg','Automation_Coverage']]),columns=['Execution_Hours','Defect_Severity_Avg','Automation_Coverage'])
print(scaled_df)

"""
EDA & Visualization 
Visualize productivity relationships using: 
• Correlation Heatmap — identify key dependencies between variables. 
• Boxplot: Defect_Severity_Avg vs Avg_Closure_Time.
• Bar Chart: Average closure time per module. 
• Scatter Plot: Total_TestCases_Executed vs Execution_Hours to visualize workload. 
• Histogram + KDE: Distribution of closure time and execution hours. 
Use both matplotlib and seaborn for plots.
"""

print("group by module")
avgClosureTime = data.groupby("Module")["Avg_Closure_Time"].mean()
#avgClosureTimeDF = pd.DataFrame(avgClosureTime, columns=["Module","Avg Closure Time"])
avgClosureTimeDF = avgClosureTime.reset_index(name="Avg Closure Time")
plt.bar(avgClosureTimeDF["Module"],avgClosureTimeDF["Avg Closure Time"])
plt.show()

plt.scatter(data["Total_TestCases_Executed"],data["Execution_Hours"])
plt.xlabel("Total TestCase Executed")
plt.ylabel("Execution Hours")
plt.show()

fig, subPlotLine = plt.subplots(1,2, figsize=(12,6))
sns.histplot(data['Execution_Hours'].dropna(), bins=5, kde=True, ax=subPlotLine[0])
sns.histplot(data['Avg_Closure_Time'].dropna(), bins=10, kde=True, ax=subPlotLine[1])
plt.show()

#correlation = data[['Defects_Found','Avg_Closure_Time']].corr()
correlation_with_closure = data.corr(numeric_only=True)[['Avg_Closure_Time']].drop(index='Avg_Closure_Time')
sns.heatmap(correlation_with_closure, annot=True, fmt=".0f", cmap='viridis', cbar=True)
plt.title('Correlation Heatmap')
plt.show()

boxPlotData = data[["Defect_Severity_Avg","Avg_Closure_Time"]]
plt.boxplot(boxPlotData,
            vert=True,
            patch_artist=True,
            notch=True,
            showmeans=True,
            boxprops=dict(facecolor="lightblue"),
            medianprops=dict(color="red", linewidth=2),
            meanprops=dict(marker="o", markerfacecolor="green", markersize=8),
            flierprops=dict(marker="x", color="orange"))
plt.show()


"""
Model Building (Linear Regression) 
Objective: Predict Avg_Closure_Time based on workload, severity, automation coverage, and 
execution effort.
"""

x = data[['Defects_Found']]
y = data['Avg_Closure_Time']
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=10)

model = LinearRegression()
model.fit(xtrain, ytrain)

ypredit = model.predict(xtest)

plt.scatter(xtest, ytest, marker='o', color = 'red', label='Testing Values', alpha=0.3)
plt.plot(xtest, ypredit, color='blue', label = 'Predicted Values')

plt.xlabel("Defects Found")
plt.ylabel("Average Closure Time")
plt.legend()
plt.show()