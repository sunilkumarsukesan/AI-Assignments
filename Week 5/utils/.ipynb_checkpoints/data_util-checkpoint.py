import pandas as pd
import os

class data_util:

    def read_a_csv(self, file_name):
        try:
            return pd.read_csv(file_name)
        except FileNotFoundError:
            raise Exception(f"File not found: {file_name}, current directory {os.getcwd()}")
        except Exception as e:
            raise Exception(f"Some other error occurred: {e}")
        
    def write_to_csv(self, df, file_name):
        try:
            df.to_csv(file_name, index=False)
            print (f"Saved file in {os.getcwd()}\{file_name}")
        except Exception as e:
            raise Exception(f"Some other error occurred while writing the file : {e}")
