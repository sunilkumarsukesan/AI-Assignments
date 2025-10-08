import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.stats import skew

class Covid_EDA:
    cleaned_df = ""
    scaled_df = ""

    def __init__(self,filename):
        self.df = pd.read_csv(filename)
        self.df = self.df[['Confirmed','New cases']]
        print(self.df.shape)


    def getAllBasicSatistics(self):
        print("Mean:\n",self.df.mean())
        print("Median:\n",self.df.median())
        print("Variance:\n", self.df.var())
        print("Standard deviation:\n", self.df.std())
        print("Correlation between confirmed and New cases:\n", self.df['Confirmed'].corr(self.df['New cases']))


    def detect_outliers_using_IQR(self, column_name):
        Q1 = self.df[column_name].quantile(0.25)
        Q3 = self.df[column_name].quantile(0.75)
        IQR = Q3 - Q1
        print(Q1, Q3, IQR)
        #lower_bound = Q1 - 1.5 * IQR
        #upper_bound = Q3 + 1.5 * IQR
        #outliers = self.df[(self.df[column_name]<lower_bound) | (self.df[column_name]>upper_bound)]
        #self.df = self.df.drop(outliers.index)
        self.cleaned_df = self.df.drop(self.df[(self.df[column_name]< (Q1 - 1.5 * IQR)) | (self.df[column_name]> (Q3 + 1.5 * IQR))].index)
        print(self.cleaned_df)

    def normalize_using_standard_scaler(self):
        scaler = StandardScaler()
        scaled = scaler.fit_transform(self.cleaned_df)
        print(type(scaled))
        self.scaled_df = pd.DataFrame(scaled, columns= self.cleaned_df.columns)
        print(self.scaled_df)

    def plot_hist(self, column_name):
        for df in [self.cleaned_df, self.scaled_df]:
            sns.histplot(df[column_name], bins=10, kde=True)
            plt.show()


    def plot_heatmap(self):
        sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

    def get_skew(self):
        print(skew(self.scaled_df['Confirmed']))
        print(skew(self.scaled_df['New cases']))
        
if __name__ == "__main__":
    eda = Covid_EDA('./Week 5/data/country_wise_latest.csv')
    eda.getAllBasicSatistics()
    eda.detect_outliers_using_IQR('Confirmed')
    eda.detect_outliers_using_IQR('New cases')
    eda.normalize_using_standard_scaler()
    eda.plot_hist('Confirmed')
    eda.plot_hist('New cases')
    eda.plot_heatmap()
    eda.get_skew()