import pandas as pd
import os

def load_data(file_name):
    return pd.read_csv(os.path.join("data", file_name))

if __name__ == "__main__":
    data = load_data("campeonato-brasileiro-full.csv")
    print(data.head())