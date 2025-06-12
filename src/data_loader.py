import pandas as pd
from typing import Tuple, Optional


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_csv(filepath)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw data (handle missing values, duplicates, etc.).
    Args:
        df (pd.DataFrame): Raw data.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    # Add more cleaning steps as needed
    return df 