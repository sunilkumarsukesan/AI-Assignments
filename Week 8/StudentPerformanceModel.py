import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score

class StudentPerformanceModel:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.X_train = self.X_test = self.Y_train = self.Y_test = self.Y_Pred = None
        self.model = None

    
    def data_preprocessing(self):
        print(f"Dataframe head:\n {self.df.head()}")
        print(f"\nShape of the dataframe : {self.df.shape}")
        print(f"\nDataframe info : \n ")
        self.df.info()

    def visualize_data(self):
        sns.pairplot(self.df)
        plt.show()
        pass

    def prepare_data_for_modelling(self):
        self.df['Extracurricular Activities'] = self.df['Extracurricular Activities'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
        X = self.df.drop(columns=['Performance Index'])
        Y = self.df['Performance Index']
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size= 0.2, random_state=10)
        print()
        
    
    def model_training(self):
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.Y_train)
        
    
    def model_evaluation(self):
        self.Y_Pred = self.model.predict(self.X_test)
        print(f"MSE : {mean_squared_error(self.Y_test,self.Y_Pred)}")
        print(f"RMSE : {root_mean_squared_error(self.Y_test,self.Y_Pred)}")
        print(f"R Square : {r2_score(self.Y_test,self.Y_Pred)}")

        
        
if __name__ == "__main__":
    obj = StudentPerformanceModel("./Week 8/Student_Performance.csv")
    obj.data_preprocessing()
    obj.visualize_data()
    obj.prepare_data_for_modelling()
    obj.model_training()
    obj.model_evaluation()