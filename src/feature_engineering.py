import pandas as pd
from typing import Optional


def add_claim_ratio(df: pd.DataFrame, claim_col: str, premium_col: str) -> pd.DataFrame:
    """
    Add a claim ratio feature to the DataFrame.
    Args:
        df (pd.DataFrame): Input data.
        claim_col (str): Column for claim amount.
        premium_col (str): Column for premium amount.
    Returns:
        pd.DataFrame: DataFrame with claim ratio.
    """
    df['claim_ratio'] = df[claim_col] / df[premium_col]
    return df


def add_profit_margin(df: pd.DataFrame, premium_col: str, claim_col: str) -> pd.DataFrame:
    """
    Add a profit margin feature to the DataFrame.
    Args:
        df (pd.DataFrame): Input data.
        premium_col (str): Premium column.
        claim_col (str): Claim column.
    Returns:
        pd.DataFrame: DataFrame with profit margin.
    """
    df['profit_margin'] = (df[premium_col] - df[claim_col]) / df[premium_col]
    return df


def add_vehicle_age(df: pd.DataFrame, year_col: str, current_year: Optional[int] = None) -> pd.DataFrame:
    """
    Add a vehicle age feature to the DataFrame.
    Args:
        df (pd.DataFrame): Input data.
        year_col (str): Column with vehicle year.
        current_year (Optional[int]): Current year (default: 2024).
    Returns:
        pd.DataFrame: DataFrame with vehicle age.
    """
    if current_year is None:
        current_year = 2024
    df['vehicle_age'] = current_year - df[year_col]
    return df 