import pandas as pd
from scipy import stats
from typing import Tuple, Dict


def ab_ttest(df: pd.DataFrame, group_col: str, value_col: str, group_a, group_b) -> Dict[str, float]:
    """
    Perform a t-test between two groups.
    Args:
        df (pd.DataFrame): Input data.
        group_col (str): Column to group by (e.g., 'gender').
        value_col (str): Column to test (e.g., 'claim_amount').
        group_a: Value for group A.
        group_b: Value for group B.
    Returns:
        Dict[str, float]: t-statistic and p-value.
    """
    a = df[df[group_col] == group_a][value_col].dropna()
    b = df[df[group_col] == group_b][value_col].dropna()
    t_stat, p_val = stats.ttest_ind(a, b, equal_var=False)
    return {"t_stat": t_stat, "p_value": p_val} 