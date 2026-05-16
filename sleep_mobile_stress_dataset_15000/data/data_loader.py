import pandas as pd

def load_data(file_path):
    """Loads the CSV dataset."""
    return pd.read_csv(file_path)
