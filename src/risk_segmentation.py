import pandas as pd
from typing import Tuple


def segment_risk(df: pd.DataFrame, risk_col: str, threshold: float) -> pd.DataFrame:
    """
    Segment customers into low-risk and high-risk based on a threshold.
    Args:
        df (pd.DataFrame): Input data.
        risk_col (str): Column to use for risk segmentation.
        threshold (float): Threshold to separate low/high risk.
    Returns:
        pd.DataFrame: DataFrame with a new 'risk_segment' column.
    """
    df['risk_segment'] = df[risk_col].apply(lambda x: 'low' if x < threshold else 'high')
    return df 