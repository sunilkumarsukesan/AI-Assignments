import os
import numpy as np
import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

print(os.getcwd())
data = pd.read_csv('./Capstone Project/QA Productivity/qa_team_productivity_large.csv')
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