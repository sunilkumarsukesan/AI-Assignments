import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

class StudentPerformanceModel:

    def __init__(self, path):
        self.df = pd.read_csv(path)

    
    def data_preprocessing(self):
        print(f"Dataframe head:\n {self.df.head()}")
        print(f"\nShape of the dataframe : {self.df.shape}")
        print(f"\nDataframe info : \n ")
        self.df.info()

    def visualize_data(self):
        #sns.pairplot(self.df)
        #plt.show()
        pass

    def prepare_data_for_modelling(self):
        X = self.df.iloc[: (int(len(self.df.columns)-1))]
        Y = self.df.iloc[int(len(self.df.columns))-1:]
        #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state=10)
        print()



if __name__ == "__main__":
    obj = StudentPerformanceModel("./Week 8/Student_Performance.csv")
    obj.data_preprocessing()
    obj.visualize_data()
    obj.prepare_data_for_modelling()