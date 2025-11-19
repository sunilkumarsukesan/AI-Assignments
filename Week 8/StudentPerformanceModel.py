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
        #sns.pairplot(self.df)
        sns.histplot(data=self.df, x='Performance Index',bins = 10, kde = True)
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
        
    def visualization(self):

        # Define input features and target
        X = self.df[['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']]
        y = self.df['Performance Index']
        pairs = [
                    ('Hours Studied', 'Previous Scores'),
                    ('Previous Scores', 'Extracurricular Activities'),
                    ('Extracurricular Activities', 'Sleep Hours'),
                    ('Sleep Hours', 'Sample Question Papers Practiced')
                ]
        # Create 2x2 subplot figure
        fig = plt.figure(figsize=(18, 12))

        for i, (f1, f2) in enumerate(pairs, 1):
            ax = fig.add_subplot(2, 2, i, projection='3d')

            # Scatter actual points
            ax.scatter(X[f1], X[f2], y, color='blue', s=20, alpha=0.5, label='Actual')

            # Create meshgrid for surface
            x1_surf = np.linspace(X[f1].min(), X[f1].max(), 20)
            x2_surf = np.linspace(X[f2].min(), X[f2].max(), 20)
            x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)
            
            mean_values = self.df.mean()
            
            # Total number of points on the grid
            n_points = x1_surf.size
            
            # Build full input DataFrame with all 5 features
            input_data = pd.DataFrame({
                'Hours Studied': x1_surf.ravel() if f1 == 'Hours Studied' else np.full(n_points, mean_values['Hours Studied']),
                'Previous Scores': x2_surf.ravel() if f2 == 'Previous Scores' else np.full(n_points, mean_values['Previous Scores']),
                'Extracurricular Activities': np.full(n_points, mean_values['Extracurricular Activities']),
                'Sleep Hours': np.full(n_points, mean_values['Sleep Hours']),
                'Sample Question Papers Practiced': np.full(n_points, mean_values['Sample Question Papers Practiced'])
            })

            # Predict values for plane
            y_plane = self.model.predict(input_data)
            y_plane = y_plane.reshape(x1_surf.shape)
            
            # Plot regression plane
            ax.plot_surface(x1_surf, x2_surf, y_plane, color='red', alpha=0.3)

            # Labels & title
            ax.set_xlabel(f1)
            ax.set_ylabel(f2)
            ax.set_zlabel('Performance Index')
            ax.set_title(f'3D Regression: {f1} vs {f2} vs Performance Index')

        plt.tight_layout()
        plt.show()

    def predict_performance_index(self, hours_studied, previous_scores, extracurricular_activities, sleep_hours, sample_question_papers):
        extracurricular_activities = 1 if str(extracurricular_activities).strip().lower() == 'yes' else 0
        input_data = np.array([[hours_studied, previous_scores, extracurricular_activities, sleep_hours, sample_question_papers]])
        predicted_value = self.model.predict(input_data)
        print(f"Predicted Performance Index for \nhours_studied = {hours_studied}\nprevious_scores = {previous_scores}\nextracurricular_activities = {extracurricular_activities}\nsleep_hour = {sleep_hours}\nsample_question_papers = {sample_question_papers}\nPredicted value is : {predicted_value[0]:.2f}")

        
        
if __name__ == "__main__":
    obj = StudentPerformanceModel("./Week 8/Student_Performance.csv")
    obj.data_preprocessing()
    obj.visualize_data()
    obj.prepare_data_for_modelling()
    obj.model_training()
    obj.model_evaluation()
    obj.visualization()
    obj.predict_performance_index(8, 80, 'yes', 7, 5)