import os
import numpy as np
import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns

print(os.getcwd())
data = pd.read_csv('./Capstone Project/QA Productivity/qa_team_productivity_large.csv')
print(data.head())
print(data.describe())

# To get the unique values and count of the column
print(pd.unique(data['Tester_ID']))
print("Total unique tester id's : " , data['Tester_ID'].nunique())

#To get the null and non-null count
print("Null count -> " , data.isnull().sum())
data.info()

#Fill the missing values
data['Defect_Severity_Avg'].fillna(format(data['Defect_Severity_Avg'].mean(), ".2f"),inplace=True)
data['Automation_Coverage'].fillna(format(data['Automation_Coverage'].mean(), ".2f"),inplace=True)
data['Execution_Hours'].fillna(format(data['Execution_Hours'].mean(), ".2f"),inplace=True)
print("Null count -> " , data.isnull().sum())
data.to_csv('update_dataset.csv',index=False)
data.info()

sns.histplot(data, x = data['Defect_Severity_Avg'],kde=True)
plt.show()

