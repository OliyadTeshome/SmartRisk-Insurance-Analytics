import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, chi2_contingency
from typing import Tuple, Dict

def compute_claim_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute Claim Frequency, Claim Severity, and Margin.
    """
    df = df.copy()
    df['HasClaim'] = df['TotalClaims'] > 0
    df['ClaimFrequency'] = df['HasClaim'].astype(int)
    df['ClaimSeverity'] = df['TotalClaims'] / df['HasClaim'].replace(0, np.nan)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df

def prepare_ttest_data(df: pd.DataFrame, group_col: str, metric_col: str, group_a: str, group_b: str) -> Tuple[pd.Series, pd.Series]:
    """
    Prepare data for t-test by extracting the specified metric for two groups.
    """
    group_a_data = df[df[group_col] == group_a][metric_col]
    group_b_data = df[df[group_col] == group_b][metric_col]
    return group_a_data, group_b_data

def perform_ttest(df: pd.DataFrame, group_col: str, metric_col: str, group_a: str, group_b: str) -> Dict:
    """
    Perform two-sample t-test between two groups for a specified metric.
    
    Args:
        df: DataFrame containing the data
        group_col: Column name containing the group labels
        metric_col: Column name containing the metric to test
        group_a: Name of the first group
        group_b: Name of the second group
    
    Returns:
        Dictionary containing t-statistic, p-value, and significance
    """
    group_a_data, group_b_data = prepare_ttest_data(df, group_col, metric_col, group_a, group_b)
    
    # Get sample sizes
    n_a = len(group_a_data.dropna())
    n_b = len(group_b_data.dropna())
    
    # Check if sample sizes are sufficient
    if n_a < 30 or n_b < 30:
        print(f"Warning: Small sample sizes detected - Group {group_a}: {n_a} samples, Group {group_b}: {n_b} samples")
        print("Consider using non-parametric tests or collecting more data")
    
    # Perform t-test
    t_stat, p_val = ttest_ind(group_a_data.dropna(), group_b_data.dropna(), equal_var=False)
    
    return {
        't_stat': t_stat,
        'p_value': p_val,
        'significant': p_val < 0.05,
        'group_a_mean': group_a_data.mean(),
        'group_b_mean': group_b_data.mean(),
        'group_a_size': n_a,
        'group_b_size': n_b
    }

def perform_chi2_test(df: pd.DataFrame, category_col: str, outcome_col: str) -> Dict:
    """
    Perform chi-squared test for independence between a categorical feature and binary outcome.
    """
    contingency = pd.crosstab(df[category_col], df[outcome_col])
    chi2, p, dof, expected = chi2_contingency(contingency)
    return {
        'chi2_stat': chi2,
        'p_value': p,
        'significant': p < 0.05,
        'degrees_of_freedom': dof
    }

def summarize_group_statistics(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Summarize Claim Frequency, Claim Severity, and Margin by group.
    """
    summary = df.groupby(group_col).agg({
        'ClaimFrequency': 'mean',
        'ClaimSeverity': 'mean',
        'Margin': 'mean',
        'TotalClaims': 'count'
    }).rename(columns={
        'TotalClaims': 'PolicyCount'
    }).reset_index()
    return summary

def ab_test_by_column(df: pd.DataFrame, column: str, metric: str) -> Tuple[Dict, pd.DataFrame]:
    """
    Run A/B test on a binary column for a specified metric.
    """
    if df[column].nunique() != 2:
        raise ValueError(f"{column} must have exactly 2 unique values to run A/B test")

    values = df[column].dropna().unique()
    group_a = df[df[column] == values[0]][metric]
    group_b = df[df[column] == values[1]][metric]
    test_result = perform_ttest(df, column, metric, values[0], values[1])
    return test_result, summarize_group_statistics(df, column)
