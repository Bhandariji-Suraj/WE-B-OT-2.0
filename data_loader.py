import pandas as pd

def load_data(file_path):
    """
    Load and preprocess the dataset.
    """
    data = pd.read_csv(file_path)
    return data
