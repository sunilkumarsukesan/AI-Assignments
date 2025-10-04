import pandas as pd

class pandas_util:

    def group_dataFrame(self, df, columns):
        return df.groupby(columns)

    def get_sum_from_grouped_df(self, grouped_df, columns):
        return grouped_df[columns].sum()
        
    def select_columns(self, df , columns):
        return df[[columns]]
    
    def get_sorted_index(self, df, col_name, ascending=True):       
        return df[col_name].sort_values(ascending=ascending).index

    def get_index_of_extreme(self, df, col_name, mode="max"):
        if mode == "max":
            return df[col_name].idxmax()
        elif mode == "min":
            return df[col_name].idxmin()
        else:
            raise ValueError("Mode must be either 'max' or 'min'")
        
    def get_non_outliers(self, df, col_name):
        mean_val = df[col_name].mean()
        std_val = df[col_name].std()
        upper = mean_val + 2 * std_val
        lower = mean_val - 2 * std_val
        return (df[col_name] >= lower) & (df[col_name] <= upper)