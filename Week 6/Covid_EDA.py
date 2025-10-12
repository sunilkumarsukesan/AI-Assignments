import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import skew

class Covid_EDA:
    scaled_df = ""
    original_df = ""
    

    def __init__(self,filename):
        self.df = pd.read_csv(filename)
        self.df = self.df[['Confirmed','New cases']]
        self.original_df = self.df.copy()
        self.scaled_df = None
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
        print(f"{column_name} : Q1 -> {Q1}, Q3 -> {Q3}, IQR -> {IQR}")
        #lower_bound = Q1 - 1.5 * IQR
        #upper_bound = Q3 + 1.5 * IQR
        #outliers = self.df[(self.df[column_name]<lower_bound) | (self.df[column_name]>upper_bound)]
        #self.df = self.df.drop(outliers.index)
        self.df = self.df.drop(self.df[(self.df[column_name]< (Q1 - 1.5 * IQR)) | (self.df[column_name]> (Q3 + 1.5 * IQR))].index)
        print(self.df.shape)

    def normalize_using_standard_scaler(self):
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(self.df)
        print(type(scaled))
        self.scaled_df = pd.DataFrame(scaled, columns= self.df.columns)
        print(self.scaled_df)

    def plot_hist(self, columns):
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        fig.suptitle("Cleaned vs Scaled")

        for index, col in enumerate(columns):
            sns.histplot(self.df[col], bins=10, kde=True, color='blue', ax=axes[0, index])
            axes[index, 0].set_title(f'{col} (Cleaned)')
            axes[index, 0].set_ylabel('Frequency')

            sns.histplot(self.scaled_df[col], bins=10, kde=True, color='orange', ax=axes[1, index])
            axes[index, 1].set_title(f'{col} (Scaled)')
            axes[index, 1].set_ylabel('Frequency')

        plt.tight_layout()
        plt.show()


    def plot_heatmap(self):
        sns.heatmap(self.original_df.corr(), annot=True, cmap="coolwarm")
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
    eda.plot_hist(['Confirmed', 'New cases'])
    eda.plot_heatmap()
    eda.get_skew()