import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional


def eda_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate summary statistics for the DataFrame.
    Args:
        df (pd.DataFrame): Input data.
    Returns:
        pd.DataFrame: Summary statistics.
    """
    return df.describe(include='all')


def plot_distribution(df: pd.DataFrame, column: str, save_path: Optional[str] = None) -> None:
    """
    Plot the distribution of a column.
    Args:
        df (pd.DataFrame): Input data.
        column (str): Column to plot.
        save_path (Optional[str]): Path to save the plot.
    """
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f'Distribution of {column}')
    if save_path:
        plt.savefig(save_path)
    plt.show() 