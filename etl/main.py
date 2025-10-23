import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(data):
    return data.dropna()

def save_data(data, file_path):
    data.to_csv(file_path, index=False)

if __name__ == "__main__":
    data = load_data("data/campeonato-brasileiro-full.csv")
    clean_data(data)